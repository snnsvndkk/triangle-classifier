# Triangle Classifier — CSC325 Module 6

Classifies a triangle from three side lengths as `Invalid`, `Equilateral`, `Isosceles`, or `Scalene`, with a `Right ` prefix for right triangles.

## How to run the tests

```bash
pip install -r requirements.txt
pytest -v
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
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

## Acceptance criteria

<!-- TODO (Sinan): write 2–3 measurable criteria from the stained-glass customer's request (no AI for this part) -->

1.
2.
3.

## AI-use disclosure

<!-- TODO (Sinan): review and edit so it matches exactly what you did -->

- **Claude (Anthropic):** generated the initial `triangle.py` implementation, `requirements.txt`, and this README's structure and equivalence-class table. I reviewed the code against the spec table and verified it by running the test suite.
- **GitHub Copilot:** used for autocomplete while drafting `test_triangle.py`; each suggestion reviewed (see log above).
- `test_acceptance.py` and the acceptance criteria were written by me without AI tools.
