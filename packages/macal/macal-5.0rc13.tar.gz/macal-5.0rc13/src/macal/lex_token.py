#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      24-10-2023
#
# Copyright 2023 Westcon-Comstor
#

# Lex token definitions for Macal

from __future__ import annotations
from .ast_node import AstNode
from .ast_nodetype import AstNodetype

class LexToken(AstNode):
    def __init__(self, type, value, lineno, offset, lexpos) -> LexToken:
        super().__init__()
        self.token_type  : AstNodetype = type
        self.value : str = value
        self.lineno: int = lineno
        self.offset: int = offset
        self.lexpos: int = lexpos

    def __str__(self) -> str:
        s = self.value
        if self.token_type in (AstNodetype.STRING, AstNodetype.STRING_INTERPOLATION_STRING_PART, AstNodetype.STRING_INTERPOLATION_END, AstNodetype.WHITESPACE):
            s = self.value.strip()
        return f"LexToken({self.token_type}, {s}, {self.lineno}, {self.offset} {self.lexpos})"

    def __repr__(self) -> str:
        return self.__str__()

    @staticmethod
    def FromToken(token: LexToken) -> LexToken:
        return LexToken(token.token_type, token.value, token.lineno, token.lexpos, token.lexpos)