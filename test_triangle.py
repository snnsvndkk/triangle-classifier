import math
from triangle import classify_triangle

def test_invalid_zero_side():
    assert classify_triangle(0, 5, 7) == "Invalid"

def test_degenerate_triangle():
    assert classify_triangle(1, 2, 3) == "Invalid"

def test_equilateral():
    assert classify_triangle(5, 5, 5) == "Equilateral"

def test_isosceles():
    assert classify_triangle(5, 5, 3) == "Isosceles"

def test_scalene():
    assert classify_triangle(4, 5, 6) == "Scalene"

def test_right_triangle_non_integer():
    assert classify_triangle(5, 5, 5 * math.sqrt(2)) == "Right Isosceles"

