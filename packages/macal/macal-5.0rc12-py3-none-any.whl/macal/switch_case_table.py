#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      24-10-2023
#
# Copyright 2023 Westcon-Comstor
#


# Switch Case Table

from __future__ import annotations

class SwitchCaseTable:
    def __init__(self, address: int, labels: dict) -> SwitchCaseTable:
        self.address: int = address
        self.labels: dict = labels