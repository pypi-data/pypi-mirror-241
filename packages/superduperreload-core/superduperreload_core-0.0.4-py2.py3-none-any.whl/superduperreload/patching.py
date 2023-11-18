# -*- coding: utf-8 -*-
import ctypes
import functools
import gc
import sys
from collections import defaultdict
from enum import Enum
from types import FunctionType, MethodType
from typing import Callable, Dict, List, Optional, Set, Sized, Tuple, Type, Union

from traitlets.config import SingletonConfigurable

from superduperreload.utils import isinstance2

if sys.maxsize > 2**32:
    WORD_TYPE: Union[Type[ctypes.c_int32], Type[ctypes.c_int64]] = ctypes.c_int64
    WORD_N_BYTES = 8
else:
    WORD_TYPE = ctypes.c_int32
    WORD_N_BYTES = 4


# Placeholder for indicating an attribute is not found
_NOT_FOUND: object = object()


_MOD_ATTRS = [
    "__name__",
    "__doc__",
    "__package__",
    "__loader__",
    "__spec__",
    "__file__",
    "__cached__",
    "__builtins__",
]


_FUNC_ATTRS = [
    "__closure__",
    "__code__",
    "__defaults__",
    "__doc__",
    "__dict__",
    "__globals__",
]


class _CPythonStructType(Enum):
    CLASS = "class"
    FUNCTION = "function"
    METHOD = "method"
    PARTIAL = "partial"
    PARTIALMETHOD = "partialmethod"


_MAX_FIELD_SEARCH_OFFSET = 50
_MAX_REFERRERS_FOR_PATCHING = 512
_MAX_REFERRER_LENGTH_FOR_PATCHING = 128

ClassCallableTypes: Tuple[Type[object], ...] = (
    FunctionType,
    MethodType,
    property,
    functools.partial,
    functools.partialmethod,
)

IMMUTABLE_PRIMITIVE_TYPES = (
    bytes,
    bytearray,
    float,
    frozenset,
    int,
    str,
    tuple,
)


class UnpatchableDict(dict):
    pass


class UnpatchableList(list):
    pass


class ObjectPatcher(SingletonConfigurable):
    _FIELD_OFFSET_LOOKUP_TABLE_BY_STRUCT_TYPE: Dict[str, Dict[str, int]] = {}

    def __init__(self, patch_referrers: bool, **kwargs) -> None:
        super().__init__(**kwargs)
        self._patched_obj_ids: Set[int] = set()
        self._remapped_classes: Dict[Type[object], Type[object]] = UnpatchableDict()
        self._patch_rules: List[Tuple[Callable, Callable]] = [
            (lambda a, b: isinstance2(a, b, type), self._patch_class),
            (lambda a, b: isinstance2(a, b, FunctionType), self._patch_function),
            (lambda a, b: isinstance2(a, b, MethodType), self._patch_method),
            (lambda a, b: isinstance2(a, b, property), self._patch_property),
            (lambda a, b: isinstance2(a, b, functools.partial), self._patch_partial),
            (
                lambda a, b: isinstance2(a, b, functools.partialmethod),
                self._patch_partialmethod,
            ),
        ]

        self._patch_referrers: bool = patch_referrers
        self._referrer_patch_rules: List[
            Tuple[Tuple[Type[Sized], ...], Callable[..., None]]
        ] = [
            ((list,), self._patch_list_referrer),
            ((dict, defaultdict), self._patch_dict_referrer),
        ]

    @classmethod
    def _infer_field_offset(
        cls,
        struct_type: "_CPythonStructType",
        obj: object,
        field: str,
        cache: bool = True,
    ) -> int:
        field_value = getattr(obj, field, _NOT_FOUND)
        if field_value is _NOT_FOUND:
            return -1
        if cache:
            offset_tab = cls._FIELD_OFFSET_LOOKUP_TABLE_BY_STRUCT_TYPE.setdefault(
                struct_type.value, {}
            )
        else:
            offset_tab = {}
        ret = offset_tab.get(field)
        if ret is not None:
            return ret
        obj_addr = ctypes.c_void_p.from_buffer(ctypes.py_object(obj)).value
        field_addr = ctypes.c_void_p.from_buffer(ctypes.py_object(field_value)).value
        if obj_addr is None or field_addr is None:
            offset_tab[field] = -1
            return -1
        ret = -1
        for offset in range(1, _MAX_FIELD_SEARCH_OFFSET):
            if (
                ctypes.cast(
                    obj_addr + WORD_N_BYTES * offset, ctypes.POINTER(WORD_TYPE)
                ).contents.value
                == field_addr
            ):
                ret = offset
                break
        offset_tab[field] = ret
        return ret

    @classmethod
    def _try_write_readonly_attr(
        cls,
        struct_type: "_CPythonStructType",
        obj: object,
        field: str,
        new_value: object,
        offset: Optional[int] = None,
    ) -> None:
        prev_value = getattr(obj, field, _NOT_FOUND)
        if prev_value is _NOT_FOUND:
            return
        if offset is None:
            offset = cls._infer_field_offset(struct_type, obj, field)
        if offset == -1:
            return
        obj_addr = ctypes.c_void_p.from_buffer(ctypes.py_object(obj)).value
        new_value_addr = ctypes.c_void_p.from_buffer(ctypes.py_object(new_value)).value
        if obj_addr is None or new_value_addr is None:
            return
        if prev_value is not None:
            ctypes.pythonapi.Py_DecRef(ctypes.py_object(prev_value))
        if new_value is not None:
            ctypes.pythonapi.Py_IncRef(ctypes.py_object(new_value))
        ctypes.cast(
            obj_addr + WORD_N_BYTES * offset, ctypes.POINTER(WORD_TYPE)
        ).contents.value = new_value_addr

    @classmethod
    def _try_patch_readonly_attr(
        cls,
        struct_type: "_CPythonStructType",
        old: object,
        new: object,
        field: str,
        new_is_value: bool = False,
    ) -> None:
        old_value = getattr(old, field, _NOT_FOUND)
        new_value = new if new_is_value else getattr(new, field, _NOT_FOUND)
        if old_value is _NOT_FOUND or new_value is _NOT_FOUND:
            return
        elif old_value is new_value:
            return
        elif old_value is not None:
            offset = cls._infer_field_offset(struct_type, old, field)
        else:
            assert not new_is_value
            assert new_value is not None
            offset = cls._infer_field_offset(struct_type, new, field)
        cls._try_write_readonly_attr(struct_type, old, field, new_value, offset=offset)

    def _patch_function(self, old: FunctionType, new: FunctionType) -> None:
        if old is new:
            return
        for name in _FUNC_ATTRS:
            if name == "__globals__":
                # switch order for __globals__ since we keep the old module.__dict__
                old, new = new, old
            try:
                setattr(old, name, getattr(new, name))
            except (AttributeError, TypeError, ValueError):
                self._try_patch_readonly_attr(
                    _CPythonStructType.FUNCTION, old, new, name
                )
            finally:
                if name == "__globals__":
                    old, new = new, old

    def _patch_method(self, old: MethodType, new: MethodType) -> None:
        if old is new:
            return
        self._patch_function(old.__func__, new.__func__)
        self._try_patch_readonly_attr(_CPythonStructType.METHOD, old, new, "__self__")

    @classmethod
    def _patch_instances(cls, old: Type[object], new: Type[object]) -> None:
        """Use garbage collector to find all instances that refer to the old
        class definition and update their __class__ to point to the new class
        definition"""
        if old is new:
            return

        refs = gc.get_referrers(old)

        for ref in refs:
            if type(ref) is old:
                object.__setattr__(ref, "__class__", new)

    def _patch_class_members(self, old: Type[object], new: Type[object]) -> None:
        for key in list(old.__dict__.keys()):
            old_obj = getattr(old, key)
            new_obj = getattr(new, key, _NOT_FOUND)
            if old_obj is new_obj:
                continue
            if new_obj is _NOT_FOUND and isinstance(old_obj, ClassCallableTypes):
                # obsolete attribute: remove it
                try:
                    delattr(old, key)
                except (AttributeError, TypeError):
                    pass
            elif not isinstance(old_obj, ClassCallableTypes) or not isinstance(
                new_obj, ClassCallableTypes
            ):
                try:
                    # prefer the old version for non-functions
                    setattr(new, key, old_obj)
                except (AttributeError, TypeError):
                    pass  # skip non-writable attributes
            else:
                try:
                    # prefer the new version for functions
                    setattr(old, key, new_obj)
                except (AttributeError, TypeError):
                    pass  # skip non-writable attributes

            self._patch_generic(old_obj, new_obj)
        for key in list(new.__dict__.keys()):
            if key not in list(old.__dict__.keys()):
                try:
                    setattr(old, key, getattr(new, key))
                except (AttributeError, TypeError):
                    pass  # skip non-writable attributes

    def _patch_class(self, old: Type[object], new: Type[object]) -> None:
        """Replace stuff in the __dict__ of a class, and upgrade
        method code objects, and add new methods, if any"""
        if old is new:
            return
        self._remapped_classes[old] = new
        self._patch_class_members(old, new)
        self._patch_instances(old, new)

    def _patch_subclass_mros(self, old: Type[object]) -> None:
        for cls in old.__subclasses__():
            new_bases = []
            for base in cls.__bases__:
                new_bases.append(self._remapped_classes.get(base, base))
            cls.__bases__ = tuple(new_bases)

            new_mro = []
            for base in cls.__mro__:
                new_mro.append(self._remapped_classes.get(base, base))
            self._try_patch_readonly_attr(
                _CPythonStructType.CLASS,
                cls,
                tuple(new_mro),
                "__mro__",
                new_is_value=True,
            )

    def _patch_mros(self) -> None:
        for old in self._remapped_classes.keys():
            self._patch_subclass_mros(old)
        self._remapped_classes.clear()

    def _patch_property(self, old: property, new: property) -> None:
        """Replace get/set/del functions of a property"""
        if old is new:
            return
        self._patch_generic(old.fdel, new.fdel)
        self._patch_generic(old.fget, new.fget)
        self._patch_generic(old.fset, new.fset)

    def _patch_partial(self, old: functools.partial, new: functools.partial) -> None:
        if old is new:
            return
        self._patch_function(old.func, new.func)  # type: ignore
        self._try_patch_readonly_attr(_CPythonStructType.PARTIAL, old, new, "args")
        self._try_patch_readonly_attr(_CPythonStructType.PARTIAL, old, new, "keywords")

    def _patch_partialmethod(
        self, old: functools.partialmethod, new: functools.partialmethod
    ) -> None:
        if old is new:
            return
        self._patch_method(old.func, new.func)  # type: ignore
        self._try_patch_readonly_attr(
            _CPythonStructType.PARTIALMETHOD, old, new, "args"
        )
        self._try_patch_readonly_attr(
            _CPythonStructType.PARTIALMETHOD, old, new, "keywords"
        )

    def _patch_generic(self, old: object, new: object) -> None:
        if old is new:
            return
        old_id = id(old)
        if old_id in self._patched_obj_ids:
            return
        self._patched_obj_ids.add(old_id)
        for type_check, patch in self._patch_rules:
            if type_check(old, new):
                patch(old, new)
                break

    def _patch_list_referrer(self, ref: List[object], old: object, new: object) -> None:
        for i, obj in enumerate(list(ref)):
            if obj is old:
                ref[i] = new

    def _patch_dict_referrer(
        self, ref: Dict[object, object], old: object, new: object
    ) -> None:
        # reinsert everything in the dict in iteration order, updating refs of 'old' to 'new'
        for k, v in dict(ref).items():
            if k is old:
                del ref[k]
                k = new
            if v is old:
                ref[k] = new
            else:
                ref[k] = v

    def _patch_referrers_generic(self, old: object, new: object) -> None:
        if not self._patch_referrers:
            return
        if isinstance(old, IMMUTABLE_PRIMITIVE_TYPES):
            return
        if isinstance(old, ClassCallableTypes):
            return
        referrers = gc.get_referrers(old)
        if len(referrers) > _MAX_REFERRERS_FOR_PATCHING:
            return
        for referrer in referrers:
            for types, referrer_patcher in self._referrer_patch_rules:
                if type(referrer) in types:
                    if len(referrer) <= _MAX_REFERRER_LENGTH_FOR_PATCHING:
                        referrer_patcher(referrer, old, new)
                    break
