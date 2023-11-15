#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      24-10-2023
#
# Copyright 2023 Westcon-Comstor
#

# This is the bytecode function for the compiler and the scope.

from __future__ import annotations

class BytecodeFunction:
    def __init__(self, name: str, memory_offset: int) -> BytecodeFunction:
        self.name: str = name
        self.memory_offset: int = memory_offset