
from triangle import classify_triangle

def test_criterion_1_invalid_does_not_crash():
    # Invalid triangle should return "Invalid"
    assert classify_triangle(0, 4, 5) == "Invalid"
    assert classify_triangle(1, 2, 10) == "Invalid"

def test_criterion_2_right_triangle_flagged():
    # A 3-4-5 triangle should be identified as right
    result = classify_triangle(3, 4, 5)
    assert "right" in result.lower()


def test_criterion_3_correct_for_many_inputs():
    test_cases = [
        (3, 4, 5, "Right Scalene"),
        (5, 12, 13, "Right Scalene"),
        (3, 3, 3, "Equilateral"),
        (5, 5, 8, "Isosceles"),
        (4, 5, 6, "Scalene"),
        (0, 4, 5, "Invalid"),
        (1, 2, 10, "Invalid"),
        (-1, 4, 5, "Invalid"),
        (1.5, 2.0, 2.5, "Right Scalene"),
        (6, 8, 10, "Right Scalene"),
    ]

    for a, b, c, expected in test_cases:
        result = classify_triangle(a, b, c)
        assert result == expected
