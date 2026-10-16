# Triangle Classifier — CSC325 Module 6

Classifies a triangle from three side lengths as `Invalid`, `Equilateral`, `Isosceles`, or `Scalene`, with a `Right ` prefix for right triangles.

## How to run the tests

```bash
pip install -r requirements.txt
python -m pytest -v
```

## Why an equilateral triangle can never be right

In an equilateral triangle all three angles are 60°, so none of them can be 90°. Equivalently, with sides `s, s, s` the Pythagorean check would need `s² + s² = s²`, i.e. `2s² = s²`, which only holds for `s = 0` — and a zero side is invalid.

## Equivalence classes and boundaries

| Class | Example input | Expected |
|---|---|---|
| A side is zero | (0, 3, 4) | Invalid |
| A side is negative | (-1, 3, 4) | Invalid |
| Triangle inequality fails | (1, 2, 10) | Invalid |
| **Boundary:** degenerate (a + b = c) | (1, 2, 3) | Invalid |
| **Boundary:** just above degenerate | (2, 2, 3.999) | Isosceles |
| All sides equal | (3, 3, 3) | Equilateral |
| Exactly two sides equal | (5, 5, 8) | Isosceles |
| All sides different | (4, 5, 6) | Scalene |
| Right, integer sides | (3, 4, 5) | Right Scalene |
| Right, non-integer sides | (5, 5, 5·√2) | Right Isosceles |

Boundaries: side value `0` (invalid) vs. smallest positive value (valid); `a + b == c` (invalid) vs. `a + b > c` (valid); Pythagorean equality checked with `math.isclose`, not `==`.

## Copilot Review Log

<!-- TODO (Sinan): fill this in while writing test_triangle.py with Copilot -->

| Test | Copilot-suggested? | Kept / edited / rejected | Why |
|---|---|---|---|
| test_invalid_zero_side | Yes | Edited | Copilot expected "Invalid triangle"; the spec returns exactly "Invalid". |
| test_degenerate_triangle | Yes | Edited | Copilot expected "Degenerate"; per the spec, a degenerate triangle (1+2=3) is "Invalid". |
| test_equilateral | Yes | Kept | (5, 5, 5) → "Equilateral" matches the spec. |
| test_isosceles | Yes | Kept | (5, 5, 3) is valid, exactly two sides equal, not right → "Isosceles". |
| test_scalene | Yes | Kept | (4, 5, 6) has all sides different and is not right → "Scalene". |
| test_right_triangle_non_integer | Yes | Edited | Copilot used (3.0, 4.0, 5.0) expecting "Right". "Right" alone isn't a valid result (should be "Right Scalene"), and 3.0/4.0/5.0 are still integers. Changed to (5, 5, 5·√2) → "Right Isosceles" so the tolerance check is actually exercised. |

## Acceptance criteria

1. If the three sides do not form a valid triangle, classify_triangle() returns "Invalid" and does not crash.
2. If the three sides form a right triangle, the result returned by classify_triangle() contains the word "Right".
3. For at least 10 test cases covering valid, invalid, and decimal side lengths, classify_triangle() returns the expected classification for each test case.

## AI-use disclosure

<!-- TODO (Sinan): review and edit so it matches exactly what you did -->

- **Claude (Anthropic):** generated the initial `triangle.py` implementation, `requirements.txt`, and this README's structure and equivalence-class table. I reviewed the code against the spec table and verified it by running the test suite.
- **GitHub Copilot:** used for autocomplete while drafting `test_triangle.py`; each suggestion reviewed (see log above).
- `test_acceptance.py` and the acceptance criteria were written by me without AI tools.
