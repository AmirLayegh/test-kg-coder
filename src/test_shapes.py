# ──────────────────────────── file: test_shapes.py ────────────────────────────
"""
Minimal pytest to generate TestCase → Function edges.
"""

import pytest

from shapes import Circle, Rectangle, total_area

def test_total_area():
    circle = Circle(radius=1.0)
    rect = Rectangle(width=2.0, height=3.0)
    expected = 3.141592653589793 + 6.0
    assert total_area([circle, rect]) == pytest.approx(expected)
