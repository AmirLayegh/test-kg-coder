# ─────────────────────────────── file: shapes.py ───────────────────────────────
"""
Simple geometry objects that demonstrate classes, inheritance, attributes,
and cross-module calls for KG extraction.
"""

from __future__ import annotations

from dataclasses import dataclass
import numpy as np

from math_utils import PI, clamp


class Shape:  # ──> Base class (tests :INHERITS_FROM edge)
    """Abstract geometric shape."""

    def area(self) -> float:
        """Return area in square units."""
        raise NotImplementedError


@dataclass
class Circle(Shape):
    """A circle defined by its radius."""
    radius: float

    def area(self) -> float:  # HAS_METHOD; CALLS constant PI
        return PI * self.radius**2


class Rectangle(Shape):
    """Axis-aligned rectangle (width × height)."""

    width: float
    height: float

    def __init__(self, width: float, height: float):
        # USES_VAR width/height; CALLS clamp from another module
        self.width = clamp(width, 0.0, np.inf)
        self.height = clamp(height, 0.0, np.inf)

    def area(self) -> float:
        return self.width * self.height


def total_area(shapes: list[Shape]) -> float:
    """
    Sum the areas of an iterable of shapes.
    Demonstrates a CALLS edge from a free function to class methods.
    """
    return sum(s.area() for s in shapes)
