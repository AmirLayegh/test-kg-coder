# ─────────────────────────────── file: shapes.py ───────────────────────────────
"""
Knowledge Graph Extraction Demonstration: Geometry Classes

This module is specifically designed as a demonstration codebase for knowledge graph 
extraction tools. It showcases various code relationship types that KG extraction 
systems identify and model as graph edges.

The simple geometry domain (shapes, areas) provides clear examples of:
- Class inheritance hierarchies (INHERITS_FROM edges)
- Method definitions and calls (HAS_METHOD, CALLS edges)  
- Cross-module dependencies (CALLS edges between modules)
- Variable usage patterns (USES_VAR edges)
- Function-to-method call relationships

Each code construct is intentionally designed to demonstrate specific relationship
types that would appear in a code knowledge graph.
"""

from __future__ import annotations

from dataclasses import dataclass
import numpy as np

# KG EDGE: IMPORTS - Creates dependency relationships between modules
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


