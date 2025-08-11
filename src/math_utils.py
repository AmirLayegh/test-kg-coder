# ───────────────────────────── file: math_utils.py ─────────────────────────────
"""
Knowledge Graph Extraction Demonstration: Cross-Module Dependencies

This module serves as a utility library to demonstrate cross-module dependencies 
and relationships in knowledge graph extraction. It provides mathematical functions 
and constants that are imported and used by other modules, specifically shapes.py.

KG Extraction Purpose:
- Demonstrates IMPORTS relationships: shapes.py imports from this module
- Shows CALLS edges: functions in shapes.py call functions defined here
- Illustrates constant usage: PI constant is referenced across module boundaries
- Creates cross-module dependency patterns that KG extraction tools identify

The simple mathematical utilities (clamp function, PI constant) are intentionally 
basic to keep the focus on the relationship patterns rather than complex logic.

Cross-Module Relationships Demonstrated:
1. shapes.Rectangle.__init__() -> CALLS -> clamp() (cross-module function call)
2. shapes.Circle.area() -> USES_VAR -> PI (cross-module constant usage)
3. shapes module -> IMPORTS -> math_utils module (module dependency)
"""

import math

PI: float = math.pi  # global constant


def clamp(value: float, min_value: float, max_value: float) -> float:
    """
    Restrict *value* to the inclusive range ``[min_value, max_value]``.
    """
    return max(min_value, min(value, max_value))

