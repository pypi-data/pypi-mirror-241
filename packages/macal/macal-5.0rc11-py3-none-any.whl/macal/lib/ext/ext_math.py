# Product:   Macal 2
# Author:    Marco Caspers
# Date:      16-10-2023
#

"""Macal 2 math library implementation"""

from typing import Any
from math import floor, ceil, cos, acos, sin, asin, tan, atan, pow, sqrt, log, log2, log10, exp, expm1

def math_round(rval: Any, digits = None) -> Any:
    """Implementation of round function"""
    if rval is None:
        raise Exception('Round requires at least one argument.')
    if digits is None:
        return round(rval)
    else:
        return round(rval, digits)


def math_floor(rval) -> Any:
    """Implementation of floor function"""
    return floor(rval)

def math_ceil(rval: Any) -> Any:
    """Implementation of ceil function"""
    return ceil(rval)

def math_cos(rval: Any) -> Any:
    """Implementation of cos function"""
    return cos(rval)

def math_acos(rval: Any) -> Any:
    """Implementation of acos function"""
    return acos(rval)

def math_sin(rval: Any) -> Any:
    """Implementation of sin function"""
    return sin(rval)

def math_asin(rval: Any) -> Any:
    """Implementation of asin function"""
    return asin(rval)

def math_tan(rval: Any) -> Any:
    """Implementation of tan function"""
    return tan(rval)

def math_atan(rval: Any) -> Any:
    """Implementation of atan function"""
    return atan(rval)

def math_sqrt(rval: Any) -> Any:
    """Implementation of sqrt function"""
    return sqrt(rval)

def math_log(rval: Any) -> Any:
    """Implementation of log function"""
    return log(rval)

def math_log2(rval: Any) -> Any:
    """Implementation of log2 function"""
    return log2(rval)

def math_log10(rval: Any) -> Any:
    """Implementation of log10 function"""
    return log10(rval)

def math_exp(rval: Any) -> Any:
    """Implementation of exp function"""
    return exp(rval)

def math_expm1(rval: Any) -> Any:
    """Implementation of expm1 function"""
    return expm1(rval)
