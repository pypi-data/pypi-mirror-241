#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      24-10-2023
#
# Copyright 2023 Westcon-Comstor
#

# This is the bytecode variable.

from __future__ import annotations

import sys
from typing import Any, List

from .ast_nodetype import AstNodetype
from .bytecode_register import BytecodeRegister


class BytecodeVariable:
    def __init__(self, name: str, type: AstNodetype, value: Any) -> BytecodeVariable:
        self.name: str = name
        if not isinstance(type, AstNodetype):
            raise TypeError(f"Expected AstNodetype, got {type}")
        self.type: AstNodetype = type
        self.index: List[Any] = []
        self.value: Any = value
        self.stack_offset: int = 0
        self.uninitialized: bool = True
        self.undefined: bool = type == AstNodetype.UNDEFINED

    def is_assigned(self) -> bool:
        return not self.uninitialized

    def from_register(self, register: BytecodeRegister) -> None:
        self.value = register.value
        self.type = register.value_type
        self.uninitialized = False

    def to_register(self, register: BytecodeRegister) -> None:
        register.value = self.value
        register.value_type = self.type
        self.uninitialized = False

    def get_indexed_value(self) -> Any:
        value = self.value
        for index in self.index:
            value = value[index]
        return value

    def set_indexed_value(self, value: BytecodeRegister) -> None:
        if len(self.index) == 0:
            self.value = value
        elif len(self.index) == 1:
            self.value[self.index[0]] = value
        else:
            v = self.value
            for i in range(len(self.index) - 1):
                v = v[self.index[i]]
            v[self.index[-1]] = value

    def __str__(self) -> str:
        return f"{self.name} {self.type} {self.value}"

    def __repr__(self) -> str:
        return f"{self.name} {self.type} {self.value}"

    def error(self, message: str) -> None:
        print(f"Error: {message}")
        sys.exit(1)

    def __eq__(self, other: BytecodeVariable) -> bool:
        return self.type == other.type and self.value == other.value

    def __ne__(self, other: BytecodeVariable) -> bool:
        return self.type != other.type or self.value != other.value

    def __lt__(self, other: BytecodeVariable) -> bool:
        if self.type != other.type:
            self.error(f"Cannot compare {self.type} with {other.type}")
        return self.value < other.value

    def __le__(self, other: BytecodeVariable) -> bool:
        if self.type != other.type:
            self.error(f"Cannot compare {self.type} with {other.type}")
        return self.value <= other.value

    def __gt__(self, other: BytecodeVariable) -> bool:
        if self.type != other.type:
            self.error(f"Cannot compare {self.type} with {other.type}")
        return self.value > other.value

    def __ge__(self, other: BytecodeVariable) -> bool:
        if self.type != other.type:
            self.error(f"Cannot compare {self.type} with {other.type}")
        return self.value >= other.value

    def __add__(self, other: BytecodeVariable) -> BytecodeVariable:
        if self.type != other.type:
            self.error(f"Cannot add {self.type} with {other.type}")
        self.value += other.value
        return self

    def __sub__(self, other: BytecodeVariable) -> BytecodeVariable:
        if self.type != other.type:
            self.error(f"Cannot subtract {self.type} with {other.type}")
        self.value -= other.value
        return self

    def __mul__(self, other: BytecodeVariable) -> BytecodeVariable:
        if self.type != other.type:
            self.error(f"Cannot multiply {self.type} with {other.type}")
        self.value *= other.value
        return self

    def __truediv__(self, other: BytecodeVariable) -> BytecodeVariable:
        if self.type != other.type:
            self.error(f"Cannot divide {self.type} with {other.type}")
        if other.value == 0:
            self.error(f"Cannot divide by zero")
        self.value /= other.value
        return self

    def __mod__(self, other: BytecodeVariable) -> BytecodeVariable:
        if self.type != other.type:
            self.error(f"Cannot modulus {self.type} with {other.type}")
        self.value %= other.value
        return self

    def __pow__(self, other: BytecodeVariable) -> BytecodeVariable:
        if self.type != other.type:
            self.error(f"Cannot power {self.type} with {other.type}")
        self.value **= other.value
        return self

    def __and__(self, other: BytecodeVariable) -> BytecodeVariable:
        if self.type != other.type:
            self.error(f"Cannot and {self.type} with {other.type}")
        self.value &= other.value
        return self

    def __or__(self, other: BytecodeVariable) -> BytecodeVariable:
        if self.type != other.type:
            self.error(f"Cannot or {self.type} with {other.type}")
        self.value |= other.value
        return self

    def __xor__(self, other: BytecodeVariable) -> BytecodeVariable:
        if self.type != other.type:
            self.error(f"Cannot xor {self.type} with {other.type}")
        self.value ^= other.value
        return self

    def __invert__(self) -> BytecodeVariable:
        if self.type != AstNodetype.BOOLEAN:
            self.error(f"Cannot invert {self.type}")
        self.value = not self.value
        return self
