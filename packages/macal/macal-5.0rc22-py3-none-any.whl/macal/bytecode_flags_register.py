#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      24-10-2023
#
# Copyright 2023 Westcon-Comstor
#


from typing import Any, List

from .bytecode_register import BytecodeRegister


class BytecodeFlagsRegister(BytecodeRegister):
    def __init__(self, name: str, opcode: int) -> BytecodeRegister:
        super().__init__(name, opcode)
        self.carry: bool = False
        self.zero: bool = False
        self.sign: bool = False
        self.overflow: bool = False
        self.direction: bool = False
        self.interrupt: bool = False
        self.trap: bool = False
        self.supervisor: bool = False
        self.negative: bool = False
        self.index: bool = False
        self.parity: bool = False

    def __str__(self) -> str:
        return f"CF {self._get_bit(0)} PF {self._get_bit(2)} ZF {self._get_bit(6)} SF {self._get_bit(7)} TF {self._get_bit(8)} DF {self._get_bit(10)} OF {self._get_bit(11)} IDX {self._get_bit(32)}"

    def __repr__(self) -> str:
        return self.__str__()

    def _get_bit(self, bit: int) -> str:
        return "1" if (self.value & (1 << bit)) != 0 else "0"

    def _set_bit(self, bit: int, value: bool) -> None:
        if value:
            self.value |= 1 << bit
        else:
            self.value &= ~(1 << bit)

    def get_value(self):
        self._set_bit(0, self.carry)
        self._set_bit(1, True)  # bit 1 is always true in EFLAGS
        self._set_bit(2, self.parity)
        self._set_bit(6, self.zero)
        self._set_bit(7, self.sign)
        self._set_bit(8, self.trap)
        self._set_bit(10, self.direction)
        self._set_bit(11, self.overflow)
        self._set_bit(32, self.index)
        return self.value

    def clear(self) -> None:
        self.carry = False  # bit 0 (status)
        self._set_bit(1, True)  # bit 1 is always true in EFLAGS
        self.parity = False  # bit 2 (status)
        # bit 3 is reserved
        # self._auxiliary_carry = False # bit 4 (status)
        # bit 5 is reserved
        self.zero = False  # bit 6 (status)
        self.sign = False  # bit 7 (status)
        self.trap = False  # bit 8 (single step) (control)
        # self._interrupt = False # bit 9 (interrupt enable) (control)
        self.direction = False  # bit 10 (direction) (control)
        self.overflow = False  # bit 11 (overflow) (status)
        self.index = False  # bit 32 (status) (not a real flag, but used as such for the time being)
        # for RFLAGS bits 32-63 are reserved and must be 0

    def reset(self) -> None:
        self.clear()
