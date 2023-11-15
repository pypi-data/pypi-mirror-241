#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      24-10-2023
#
# Copyright 2023 Westcon-Comstor
#

# This module contains the conversion utilities for the Macal language.

from typing import Any, Optional

from .ast_nodetype import AstNodetype
from .lex_token import LexToken

def convertToHex(value: int, digits: int = 4, prefix: str = '') -> str:
    if isinstance(value, int):
        return f'{prefix}{value:0{digits}X}'
    return f'{value}'.strip()

def typeFromOpcode(opcode: int) -> Optional[AstNodetype]:
    return next((type for type in AstNodetype if type.value == opcode), None)

def isType(opcode: int) -> bool:
    for type in AstNodetype:
        if type.value == opcode:
            return True
    return False

def convertToValue(token: LexToken) -> Any:
    if token.token_type == AstNodetype.INTEGER:
        return int(token.value)
    elif token.token_type == AstNodetype.FLOAT:
        return float(token.value)
    elif (token.token_type == AstNodetype.STRING
            or token.token_type == AstNodetype.STRING_INTERPOLATION_STRING_PART
            or token.token_type == AstNodetype.STRING_INTERPOLATION_END):
        #return token.value
        return token.value[1:-1]
    elif token.token_type == AstNodetype.BOOLEAN:
        return token.value == 'true'
    elif token.token_type == AstNodetype.BOOLEAN_TRUE:
        return True
    elif token.token_type == AstNodetype.BOOLEAN_FALSE:
        return False
    elif token.token_type == AstNodetype.NIL:
        return None
    else:
        raise Exception(f"convertToValue(): Unknown type {token.token_type}")

def compareTypes(type1: AstNodetype, type2: AstNodetype) -> bool:
    if type1 == type2:
        return True
    # handle the oddball cases
    if type1 == AstNodetype.STRING_INTERPOLATION_STRING_PART or type1 == AstNodetype.STRING_INTERPOLATION_END:
        type1 = AstNodetype.STRING
    if type2 == AstNodetype.STRING_INTERPOLATION_STRING_PART or type2 == AstNodetype.STRING_INTERPOLATION_END:
        type2 = AstNodetype.STRING
    return type1 == type2

def operandToStr(type: AstNodetype) -> str:
    if type == AstNodetype.OPERATOR_ADDITION:
        return '+'
    elif type == AstNodetype.OPERATOR_SUBTRACTION:
        return '-'
    elif type == AstNodetype.OPERATOR_MULTIPLICATION:
        return '*'
    elif type == AstNodetype.OPERATOR_DIVISION:
        return '/'
    elif type == AstNodetype.OPERATOR_MODULUS:
        return '%'
    elif type == AstNodetype.OPERATOR_POWER:
        return '^'
    elif type == AstNodetype.COMPARETOR_EQUAL:
        return '=='
    elif type == AstNodetype.COMPARETOR_NOT_EQUAL:
        return '!='
    elif type == AstNodetype.COMPARETOR_LESS_THAN:
        return '<'
    elif type == AstNodetype.COMPARETOR_LESS_THAN_EQUAL:
        return '<='
    elif type == AstNodetype.COMPARETOR_GREATER_THAN:
        return '>'
    elif type == AstNodetype.COMPARETOR_GREATER_THAN_EQUAL:
        return '>='
    elif type == AstNodetype.AND_STATEMENT:
        return 'and'
    elif type == AstNodetype.OR_STATEMENT:
        return 'or'
    elif type == AstNodetype.NOT_STATEMENT:
        return 'not'
    elif type == AstNodetype.XOR_STATEMENT:
        return 'xor'
    elif type == AstNodetype.BITWISE_AND:
        return '&'
    elif type == AstNodetype.BITWISE_OR:
        return '|'
    elif type == AstNodetype.BITWISE_NOT:
        return '~'
    elif type == AstNodetype.OPERATOR_ASSIGNMENT:
        return '='
    elif type == AstNodetype.OPERATOR_INCREMENT:
        return '++'
    elif type == AstNodetype.OPERATOR_DECREMENT:
        return '--'
    elif type == AstNodetype.OPERATOR_ASSIGNMENT_INC:
        return '+='
    elif type == AstNodetype.OPERATOR_ASSIGNMENT_DEC:
        return '-='
    elif type == AstNodetype.OPERATOR_ASSIGNMENT_MUL:
        return '*='
    elif type == AstNodetype.OPERATOR_ASSIGNMENT_DIV:
        return '/='
    elif type == AstNodetype.OPERATOR_ASSIGNMENT_MOD:
        return '%='
    elif type == AstNodetype.OPERATOR_ASSIGNMENT_POW:
        return '^='
    elif type == AstNodetype.OPERATOR_ASSIGNMENT_NEG:
        return '~='
    else:
        return 'unknown'

def typeFromValue(value: Any) -> AstNodetype:
    # BOOLEAN BEFORE INTEGER as BOOLEAN is a subclass of INTEGER
    if isinstance(value, bool):
        return AstNodetype.BOOLEAN
    elif isinstance(value, int):
        return AstNodetype.INTEGER
    elif isinstance(value, float):
        return AstNodetype.FLOAT
    elif isinstance(value, str):
        return AstNodetype.STRING
    elif value is None or value == 'nil' or value == AstNodetype.NIL:
        return AstNodetype.NIL
    elif isinstance(value, list):
        return AstNodetype.ARRAY
    elif isinstance(value, dict):
        return AstNodetype.RECORD
    else:
        raise Exception(f"typeFromValue(): Unknown type {type(value)}")

def convertToHexAddr(addr: int) -> str:
    return f'0x{addr:08X}'

def typeToStr(type: AstNodetype):
    return type.name
