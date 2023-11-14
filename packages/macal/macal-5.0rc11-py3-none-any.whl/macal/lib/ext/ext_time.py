# Product:   Macal 2
# Author:    Marco Caspers
# Date:      16-10-2023
#

"""Macal time library implementation"""

from datetime import datetime
import time


NUM_SECONDS_FIVE_MINUTES = 300
NUM_SECONDS_ONE_HOUR = 3600
TIME_FORMAT = '%Y%m%d%H%M%S'
ISO_TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
ISO_TIME_tzFORMAT = "%Y-%m-%dT%H:%M:%S.0Z"
__stopwatch__ = 0

def DateToUnix(var: str) -> int:
    """Convert a date_string of format YYYYMMDDhhmmss to unix time integer.
       Assumes the date string object is UTC time."""
    dt = datetime.strptime(var, TIME_FORMAT)
    epoch = datetime(1970, 1, 1)
    return int((dt - epoch).total_seconds())

def IsoToUnix(var: str) -> int:
    """Convert a date_string of format %Y-%m-%dT%H:%M:%S.%f to unix time integer.
       Assumes the date string object is in iso format."""
    dt = datetime.strptime(var, ISO_TIME_FORMAT)
    epoch = datetime(1970, 1, 1)
    return int((dt - epoch).total_seconds())

def DateFromUnix(var: int) -> str:
    """Converts time in seconds since UNIX EPOCH to UTC Time format"""
    return time.strftime(TIME_FORMAT, time.gmtime(var))

def IsoFromUnix(var: str) -> None:
    """Converts time in seconds since UNIX EPOCH to UTC Time format"""
    return time.strftime(ISO_TIME_tzFORMAT, time.gmtime(var))

def UtcNow() -> str:
    return datetime.utcnow().strftime("%Y%m%d%H%M%S")

def UtcIsoNow() -> str:
    return "{}Z".format(datetime.utcnow().isoformat())

def IsoNow() -> str:
    return datetime.now().isoformat()

def Now() -> str:
    return datetime.now().strftime("%Y%m%d%H%M%S")

def PerfCounter() -> float:
    return time.perf_counter()

