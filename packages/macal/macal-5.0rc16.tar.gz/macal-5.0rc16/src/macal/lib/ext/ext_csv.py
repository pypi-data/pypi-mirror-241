# Product:   Macal 2
# Author:    Marco Caspers
# Date:      16-10-2023
#
# CSV Library external functions

from typing import Any
def headersToCsv(rec: Any) -> str:
    """Implementation of HeadersToCsv function"""
    separator = '","'
    return f'"{separator.join(rec)}"'

def valuesToCsv(rec: Any) -> str:
    """Implementation of ValuesToCsv function"""
    temp = []
    for fld in rec:
       temp.append(f'"{rec[fld]}"')
    separator = ','
    return separator.join(temp)

def arrayToCsv(arr: Any) -> str:
    """Implementation of ArrayToCsv function"""
    temp = []
    for fld in arr:
        temp.append(f'"{fld}"')
    separator = ','
    return separator.join(temp)
