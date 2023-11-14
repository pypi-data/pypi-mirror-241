# Stubs for fractions
# See https://docs.python.org/3/library/fractions.html
#
# Note: these stubs are incomplete. The more complex type
# signatures are currently omitted. Also see numbers.pyi.

from typing import Optional, TypeVar, Union, overload, Any
from numbers import Real, Integral, Rational
from decimal import Decimal
import sys

_ComparableNum = Union[int, float, Decimal, Real]


@overload
def gcd(a: int, b: int) -> int: ...
@overload
def gcd(a: Integral, b: int) -> Integral: ...
@overload
def gcd(a: int, b: Integral) -> Integral: ...
@overload
def gcd(a: Integral, b: Integral) -> Integral: ...


class Fraction(Rational):
    @overload
    def __init__(self,
                 numerator: Union[int, Rational] = ...,
                 denominator: Optional[Union[int, Rational]] = ...,
                 *,
                 _normalize: bool = ...) -> None: ...
    @overload
    def __init__(self, value: float, *, _normalize: bool = ...) -> None: ...
    @overload
    def __init__(self, value: Decimal, *, _normalize: bool = ...) -> None: ...
    @overload
    def __init__(self, value: str, *, _normalize: bool = ...) -> None: ...

    @classmethod
    def from_float(cls, f: float) -> Fraction: ...
    @classmethod
    def from_decimal(cls, dec: Decimal) -> Fraction: ...
    def limit_denominator(self, max_denominator: int = ...) -> Fraction: ...

    @property
    def numerator(self) -> int: ...
    @property
    def denominator(self) -> int: ...

    def __add__(self, other): ...
    def __radd__(self, other): ...
    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    def __mul__(self, other): ...
    def __rmul__(self, other): ...
    def __truediv__(self, other): ...
    def __rtruediv__(self, other): ...
    if sys.version_info < (3, 0):
        def __div__(self, other): ...
        def __rdiv__(self, other): ...
    def __floordiv__(self, other) -> int: ...
    def __rfloordiv__(self, other) -> int: ...
    def __mod__(self, other): ...
    def __rmod__(self, other): ...
    def __divmod__(self, other): ...
    def __rdivmod__(self, other): ...
    def __pow__(self, other): ...
    def __rpow__(self, other): ...

    def __pos__(self) -> Fraction: ...
    def __neg__(self) -> Fraction: ...
    def __abs__(self) -> Fraction: ...
    def __trunc__(self) -> int: ...
    if sys.version_info >= (3, 0):
        def __floor__(self) -> int: ...
        def __ceil__(self) -> int: ...
        def __round__(self, ndigits: Optional[Any] = ...): ...

    def __hash__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: _ComparableNum) -> bool: ...
    def __gt__(self, other: _ComparableNum) -> bool: ...
    def __le__(self, other: _ComparableNum) -> bool: ...
    def __ge__(self, other: _ComparableNum) -> bool: ...
    if sys.version_info >= (3, 0):
        def __bool__(self) -> bool: ...
    else:
        def __nonzero__(self) -> bool: ...

    # Not actually defined within fractions.py, but provides more useful
    # overrides
    @property
    def real(self) -> Fraction: ...
    @property
    def imag(self) -> Fraction: ...
    def conjugate(self) -> Fraction: ...
