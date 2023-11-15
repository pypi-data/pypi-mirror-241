#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      24-10-2023
#
# Copyright 2023 Westcon-Comstor
#


# This is a method to bypass the limitation of Python that you can't pass a variable by reference.
# In this case we need to pass an address by reference, because the action that we take in the function
# needs to increase the address by the size of the data type that we are reading, so that the next time
# we read the address will be the next address in memory.

from __future__ import annotations
from .conversion import convertToHexAddr

class Address:
    def __init__(self, address: int = 0) -> Address:
        self.address: int = address

    def __str__(self) -> str:
        return f"{convertToHexAddr(self.address)}"

    def __repr__(self) -> str:
        return f"{convertToHexAddr(self.address)}"

    def __add__(self, other: int) -> Address:
        self.address += other
        return self

    def __sub__(self, other: int) -> Address:
        self.address -= other
        return self