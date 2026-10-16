"""Triangle classifier for CSC325 Module 6."""

import math

# Relative tolerance used for the Pythagorean check (floating-point safe).
RIGHT_ANGLE_TOLERANCE = 1e-9


def is_valid_triangle(a, b, c) -> bool:
    """Return True if a, b, c can form a (non-degenerate) triangle.

    Invalid when any side is <= 0, or when the triangle inequality fails.
    The degenerate case (two sides sum exactly to the third) is invalid.
    Non-numeric input is treated as invalid instead of raising an error.
    """
    try:
        if a <= 0 or b <= 0 or c <= 0:
            return False
        return a + b > c and a + c > b and b + c > a
    except TypeError:
        return False


def _is_right(a, b, c) -> bool:
    """True if the sides satisfy the Pythagorean theorem (within tolerance)."""
    x, y, z = sorted((a, b, c))
    return math.isclose(x * x + y * y, z * z, rel_tol=RIGHT_ANGLE_TOLERANCE)


def classify_triangle(a, b, c) -> str:
    """Classify a triangle by its sides.

    Returns "Invalid", "Equilateral", "Isosceles", or "Scalene",
    prefixed with "Right " when the triangle is a right triangle.
    """
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    if a == b == c:
        kind = "Equilateral"
    elif a == b or b == c or a == c:
        kind = "Isosceles"
    else:
        kind = "Scalene"

    if _is_right(a, b, c):
        return "Right " + kind
    return kind
