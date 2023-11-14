# Stubs for math
# See: http://docs.python.org/2/library/math.html

from typing import Tuple, Iterable, SupportsFloat, SupportsInt

import sys

e: float
pi: float
if sys.version_info >= (3, 5):
    inf: float
    nan: float
if sys.version_info >= (3, 6):
    tau: float

def acos(x: SupportsFloat) -> float: ...
def acosh(x: SupportsFloat) -> float: ...
def asin(x: SupportsFloat) -> float: ...
def asinh(x: SupportsFloat) -> float: ...
def atan(x: SupportsFloat) -> float: ...
def atan2(y: SupportsFloat, x: SupportsFloat) -> float: ...
def atanh(x: SupportsFloat) -> float: ...
if sys.version_info >= (3,):
    def ceil(x: SupportsFloat) -> int: ...
else:
    def ceil(x: SupportsFloat) -> float: ...
def copysign(x: SupportsFloat, y: SupportsFloat) -> float: ...
def cos(x: SupportsFloat) -> float: ...
def cosh(x: SupportsFloat) -> float: ...
def degrees(x: SupportsFloat) -> float: ...
def erf(x: SupportsFloat) -> float: ...
def erfc(x: SupportsFloat) -> float: ...
def exp(x: SupportsFloat) -> float: ...
def expm1(x: SupportsFloat) -> float: ...
def fabs(x: SupportsFloat) -> float: ...
def factorial(x: SupportsInt) -> int: ...
if sys.version_info >= (3,):
    def floor(x: SupportsFloat) -> int: ...
else:
    def floor(x: SupportsFloat) -> float: ...
def fmod(x: SupportsFloat, y: SupportsFloat) -> float: ...
def frexp(x: SupportsFloat) -> Tuple[float, int]: ...
def fsum(iterable: Iterable) -> float: ...
def gamma(x: SupportsFloat) -> float: ...
if sys.version_info >= (3, 5):
    def gcd(a: int, b: int) -> int: ...
def hypot(x: SupportsFloat, y: SupportsFloat) -> float: ...
if sys.version_info >= (3, 5):
    def isclose(a: SupportsFloat, b: SupportsFloat, rel_tol: SupportsFloat = ..., abs_tol: SupportsFloat = ...) -> bool: ...
def isinf(x: SupportsFloat) -> bool: ...
if sys.version_info >= (3,):
    def isfinite(x: SupportsFloat) -> bool: ...
def isnan(x: SupportsFloat) -> bool: ...
def ldexp(x: SupportsFloat, i: int) -> float: ...
def lgamma(x: SupportsFloat) -> float: ...
def log(x: SupportsFloat, base: SupportsFloat = ...) -> float: ...
def log10(x: SupportsFloat) -> float: ...
def log1p(x: SupportsFloat) -> float: ...
if sys.version_info >= (3, 3):
    def log2(x: SupportsFloat) -> float: ...
def modf(x: SupportsFloat) -> Tuple[float, float]: ...
def pow(x: SupportsFloat, y: SupportsFloat) -> float: ...
def radians(x: SupportsFloat) -> float: ...
if sys.version_info >= (3, 7):
    def remainder(x: SupportsFloat, y: SupportsFloat) -> float: ...
def sin(x: SupportsFloat) -> float: ...
def sinh(x: SupportsFloat) -> float: ...
def sqrt(x: SupportsFloat) -> float: ...
def tan(x: SupportsFloat) -> float: ...
def tanh(x: SupportsFloat) -> float: ...
def trunc(x: SupportsFloat) -> int: ...
