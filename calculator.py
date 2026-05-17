from typing import Union
import math


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Return the sum of two numbers."""
    try:
        return a + b
    except TypeError as e:
        raise TypeError("Both arguments must be numeric") from e


def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Return the difference of two numbers (a - b)."""
    try:
        return a - b
    except TypeError as e:
        raise TypeError("Both arguments must be numeric") from e


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Return the product of two numbers."""
    try:
        return a * b
    except TypeError as e:
        raise TypeError("Both arguments must be numeric") from e


def divide(a: Union[int, float], b: Union[int, float]) -> float:
    """Return the quotient of a divided by b.

    Raises ValueError if b is zero.
    """
    try:
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b
    except TypeError as e:
        raise TypeError("Both arguments must be numeric") from e


def power(base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
    """Return base raised to exponent power."""
    try:
        return base ** exponent
    except TypeError as e:
        raise TypeError("Both arguments must be numeric") from e


def sqrt(a: Union[int, float]) -> float:
    """Return the square root of a non-negative number.

    Raises ValueError if a is negative.
    """
    try:
        if a < 0:
            raise ValueError("Cannot compute square root of a negative number")
        return math.sqrt(a)
    except TypeError as e:
        raise TypeError("Argument must be numeric") from e


def percentage(total: Union[int, float], percent: Union[int, float]) -> float:
    """Return the percent% of total.

    Example: percentage(200, 10) returns 20.0
    """
    try:
        return (percent / 100.0) * total
    except TypeError as e:
        raise TypeError("Both arguments must be numeric") from e