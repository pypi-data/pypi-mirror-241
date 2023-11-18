#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      24-10-2023
#
# Copyright 2023 Westcon-Comstor
#

# This is the bytecode register.

from __future__ import annotations

import sys
from typing import Any

from .ast_nodetype import AstNodetype
from .macal_conversions import compareTypes, typeFromValue


class BytecodeRegister:
    def __init__(self, name: str, opcode: int) -> BytecodeRegister:
        self.name: str = name  # register name
        self.opcode: int = opcode  # register opcode, this is used in the vm to identify the register
        self.value: Any = 0
        self.value_type: AstNodetype = AstNodetype.INTEGER
        self._do_raise: bool = True  # raise an exception if an error occurs

    def reset(self) -> None:
        self.value_type = AstNodetype.INTEGER
        self.value = 0

    def error(self, message: str) -> None:
        msg = f"Register Error: {message}"
        if self._do_raise:
            raise Exception(msg)
        print(msg)
        sys.exit(1)

    def __str__(self) -> str:
        return f"{self.name} {self.value_type.name} {self.value} {self.opcode}"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: BytecodeRegister) -> BytecodeRegister:
        self.value = self.value_type == other.value_type and self.value == other.value
        self.value_type = AstNodetype.BOOLEAN
        return self

    def __ne__(self, other: BytecodeRegister) -> BytecodeRegister:
        self.value = self.value_type != other.value_type or self.value != other.value
        self.value_type = AstNodetype.BOOLEAN
        return self

    def __lt__(self, other: BytecodeRegister) -> BytecodeRegister:
        if self.value_type != other.value_type:
            self.error(f"Cannot compare {self.value_type} with {other.value_type}")
        self.value = self.value < other.value
        self.value_type = AstNodetype.BOOLEAN
        return self

    def __le__(self, other: BytecodeRegister) -> BytecodeRegister:
        if self.value_type != other.value_type:
            self.error(f"Cannot compare {self.value_type} with {other.value_type}")
        self.value = self.value <= other.value
        self.value_type = AstNodetype.BOOLEAN
        return self

    def __gt__(self, other: BytecodeRegister) -> BytecodeRegister:
        if self.value_type != other.value_type:
            self.error(f"Cannot compare {self.value_type} with {other.value_type}")
        self.value = self.value > other.value
        self.value_type = AstNodetype.BOOLEAN
        return self

    def __ge__(self, other: BytecodeRegister) -> BytecodeRegister:
        if self.value_type != other.value_type:
            self.error(f"Cannot compare {self.value_type} with {other.value_type}")
        self.value = self.value >= other.value
        self.value_type = AstNodetype.BOOLEAN
        return self

    def __expand_to_float__(self, other: BytecodeRegister) -> bool:
        # expand to float if one of the types is float.
        if (self.value_type == AstNodetype.FLOAT or other.value_type == AstNodetype.FLOAT) and (
            self.value_type == AstNodetype.INTEGER or other.value_type == AstNodetype.INTEGER
        ):
            self.value_type = AstNodetype.FLOAT
            self.value = float(self.value)
            other.value = float(other.value)
            return True
        return False

    def toStr(self, value: Any) -> str:
        if isinstance(value, bool):
            return "true" if value else "false"
        if value is None or value == AstNodetype.NIL:
            return "nil"
        return str(value)

    def __expand_to_string__(self, other: BytecodeRegister) -> bool:
        if self.value_type in (
            AstNodetype.STRING,
            AstNodetype.NIL,
            AstNodetype.STRING_INTERPOLATION_STRING_PART,
            AstNodetype.STRING_INTERPOLATION_END,
        ) or other.value_type in (
            AstNodetype.STRING,
            AstNodetype.NIL,
            AstNodetype.STRING_INTERPOLATION_STRING_PART,
            AstNodetype.STRING_INTERPOLATION_END,
        ):
            self.value_type = AstNodetype.STRING
            self.value = self.toStr(self.value)
            other.value = self.toStr(other.value)
            return True
        return False

    def __add__(self, other: BytecodeRegister) -> BytecodeRegister:
        if not compareTypes(self.value_type, other.value_type):
            if not (self.__expand_to_float__(other) or self.__expand_to_string__(other)):
                self.error(f"Cannot add {self.value_type} with {other.value_type}")
        self.value += other.value
        return self

    def __sub__(self, other: BytecodeRegister) -> BytecodeRegister:
        if self.value_type != other.value_type:
            if not self.__expand_to_float__(other):
                self.error(f"Cannot subtract {self.value_type} with {other.value_type}")
        self.value -= other.value
        return self

    def __mul__(self, other: BytecodeRegister) -> BytecodeRegister:
        if self.value_type != other.value_type:
            if not self.__expand_to_float__(other):
                self.error(f"Cannot multiply {self.value_type} with {other.value_type}")
        self.value *= other.value
        return self

    def __truediv__(self, other: BytecodeRegister) -> BytecodeRegister:
        if self.value_type != other.value_type:
            if not self.__expand_to_float__(other):
                self.error(f"Cannot divide {self.value_type} with {other.value_type}")
        self.value /= other.value
        self.value_type = typeFromValue(self.value)
        return self

    def __mod__(self, other: BytecodeRegister) -> BytecodeRegister:
        if self.value_type != other.value_type:
            if not self.__expand_to_float__(other):
                self.error(f"Cannot modulus {self.value_type} with {other.value_type}")
        self.value %= other.value
        return self

    def __pow__(self, other: BytecodeRegister) -> BytecodeRegister:
        if self.value_type != other.value_type:
            if not self.__expand_to_float__(other):
                self.error(f"Cannot power {self.value_type} with {other.value_type}")
        self.value **= other.value
        return self

    def __and__(self, other: BytecodeRegister) -> BytecodeRegister:
        if self.value_type != other.value_type:
            self.error(f"Cannot AND {self.value_type} with {other.value_type}")
        self.value = self.value and other.value
        self.value_type = AstNodetype.BOOLEAN
        return self

    def __or__(self, other: BytecodeRegister) -> BytecodeRegister:
        if self.value_type != other.value_type:
            self.error(f"Cannot OR {self.value_type} with {other.value_type}")
        self.value = self.value or other.value
        self.value_type = AstNodetype.BOOLEAN
        return self

    def __xor__(self, other: BytecodeRegister) -> BytecodeRegister:
        if self.value_type != other.value_type:
            self.error(f"Cannot XOR {self.value_type} with {other.value_type}")
        if self.name == other.name:
            self.value = int(0)
            self.value_type = AstNodetype.INTEGER
            return self
        self.value = self.value ^ other.value
        return self

    def __bool__(self) -> BytecodeRegister:
        if self.value_type != AstNodetype.BOOLEAN:
            self.error(f"Cannot invert {self.value_type}")
        self.value = not self.value
        return self

    def __neg__(self) -> BytecodeRegister:
        if self.value_type != AstNodetype.INTEGER and self.value_type != AstNodetype.FLOAT:
            self.error(f"Cannot negate {self.value_type}")
        self.value = -self.value
        return self

    def fromRegister(self, register: BytecodeRegister) -> None:
        self.value_type = register.value_type
        self.value = register.value

    def set(self, type: AstNodetype, value: Any) -> None:
        self.value_type = type
        self.value = value
