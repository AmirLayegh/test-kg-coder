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


class Shape:  # KG EDGE: Base class - Creates INHERITS_FROM edges to subclasses
    """
    Abstract geometric shape base class.
    
    KG Extraction Note: This class serves as the parent in inheritance relationships.
    Circle and Rectangle classes inherit from this base class, creating INHERITS_FROM 
    edges in the knowledge graph: Circle -> INHERITS_FROM -> Shape, 
    Rectangle -> INHERITS_FROM -> Shape.
    """

    def area(self) -> float:  # KG EDGE: HAS_METHOD - Shape class defines area method
        """
        Return area in square units.
        
        KG Extraction Note: This method definition creates a HAS_METHOD edge
        from Shape class to area method in the knowledge graph.
        """
        raise NotImplementedError


@dataclass
class Circle(Shape):  # KG EDGE: INHERITS_FROM - Circle inherits from Shape
    """
    A circle defined by its radius.
    
    KG Extraction Note: This class demonstrates multiple relationship types:
    1. INHERITS_FROM edge: Circle -> INHERITS_FROM -> Shape
    2. HAS_METHOD edge: Circle -> HAS_METHOD -> area (method definition)
    3. USES_VAR edge: area method -> USES_VAR -> radius (attribute access)
    """
    radius: float  # KG EDGE: HAS_ATTRIBUTE - Circle class has radius attribute

    def area(self) -> float:  # KG EDGE: HAS_METHOD - Circle defines area method
        """
        Calculate circle area using π * r².
        
        KG Extraction Note: This method creates multiple edges:
        - CALLS edge: area method -> CALLS -> PI (cross-module constant usage)
        - USES_VAR edge: area method -> USES_VAR -> self.radius (attribute access)
        """
        return PI * self.radius**2  # KG EDGE: CALLS PI constant from math_utils module


class Rectangle(Shape):  # KG EDGE: INHERITS_FROM - Rectangle inherits from Shape
    """
    Axis-aligned rectangle defined by width × height.
    
    KG Extraction Note: This class demonstrates several relationship types:
    1. INHERITS_FROM edge: Rectangle -> INHERITS_FROM -> Shape
    2. HAS_METHOD edges: Rectangle -> HAS_METHOD -> __init__, area
    3. Cross-module CALLS edges: __init__ method calls clamp() from math_utils
    4. USES_VAR edges: Methods access width/height parameters and attributes
    """

    width: float   # KG EDGE: HAS_ATTRIBUTE - Rectangle class has width attribute
    height: float  # KG EDGE: HAS_ATTRIBUTE - Rectangle class has height attribute

    def __init__(self, width: float, height: float):  # KG EDGE: HAS_METHOD - Rectangle defines __init__
        """
        Initialize rectangle with clamped dimensions.
        
        KG Extraction Note: This constructor demonstrates cross-module function calls:
        - CALLS edge: __init__ method -> CALLS -> clamp (from math_utils module)
        - USES_VAR edges: __init__ -> USES_VAR -> width, height parameters
        - External library usage: references np.inf from numpy
        """
        # KG EDGES: CALLS clamp function from math_utils module (cross-module dependency)
        # KG EDGES: USES_VAR width/height parameters
        self.width = clamp(width, 0.0, np.inf)
        self.height = clamp(height, 0.0, np.inf)

    def area(self) -> float:  # KG EDGE: HAS_METHOD - Rectangle defines area method
        """
        Calculate rectangle area as width × height.
        
        KG Extraction Note: This method creates USES_VAR edges to self.width 
        and self.height attributes.
        """
        return self.width * self.height  # KG EDGE: USES_VAR - accesses width/height attributes


def total_area(shapes: list[Shape]) -> float:
    """
    Sum the areas of an iterable of shapes.
    Demonstrates a CALLS edge from a free function to class methods.
    """
    return sum(s.area() for s in shapes)





