from __future__ import annotations

from dataclasses import dataclass, field, replace
from typing import *

from typing_extensions import Self, Never


A = TypeVar("A")
O = TypeVar("O")
A2 = TypeVar("A2")


@dataclass(frozen=True, repr=False)
class Setter(Generic[O, A]):
    value: A
    attribute: Attribute[O, A]

    def __lt__(self: Self, obj: O) -> O:
        new_obj = replace(obj)
        object.__setattr__(new_obj, self.attribute.name, self.value)
        return new_obj

    def __or__(self: Self, other: Setter[A, A2]) -> Setter[O, A2]:
        raise NotImplementedError()

    def __repr__(self) -> str:
        return f"{repr(self.attribute)} << {repr(self.value)}"


@dataclass(frozen=True, repr=False)
class Attribute(Generic[O, A]):
    cls: type[O]
    name: str

    def __lshift__(self, value: A) -> Setter[O, O]:
        return Setter(value, self)

    def __mul__(self, other: Attribute[A, A2]) -> Attribute[O, A2]:
        raise NotImplementedError()

    def __repr__(self) -> str:
        return f"{self.cls.__name__}.{self.name}"


class Lens(Generic[A]):
    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        origin = get_origin(source_type)
        if origin is None:
            origin = source_type
            a = Any
        else:
            a = get_args(source_type)[0]

        return core_schema.no_info_after_validator_function(lambda v: v, handler(a))

    def __set_name__(self, owner: type[O], name: str) -> None:
        self.name = name

    @overload
    def __get__(self: Self, obj: None, owner: type[O]) -> Attribute[O, A]:
        ...

    @overload
    def __get__(self, obj: O, owner: type[O]) -> A:
        ...

    def __get__(self, obj: object | None, owner: type[O]) -> Attribute[O, A] | A:
        if obj is None:
            return Attribute(owner, self.name)
        else:
            return cast(A, obj.__dict__[self.name])

    def __set__(self: Self, obj: O, value: A) -> None:
        print("set", obj, value)
        obj.__dict__[self.name] = value


# Attribute composition
# Argument application
# Setter composition
# Target application
