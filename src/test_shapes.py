# ──────────────────────────── file: test_shapes.py ────────────────────────────
"""
Knowledge Graph Extraction Demonstration: Test Case Relationships

This module demonstrates how test cases create relationship edges in knowledge graphs,
specifically TestCase → Function relationships that KG extraction tools identify.

KG Extraction Purpose:
- Shows TestCase → Function edges: test functions call and validate production code
- Demonstrates cross-module test dependencies: imports from shapes module
- Illustrates how testing frameworks create relationships between test code and application code
- Creates patterns that show how tests exercise and validate specific functionality

TestCase → Function Relationships Demonstrated:
1. test_total_area() -> CALLS -> total_area() (test-to-function relationship)
2. test_total_area() -> CALLS -> Circle() constructor (test-to-class relationship)  
3. test_total_area() -> CALLS -> Rectangle() constructor (test-to-class relationship)
4. test_total_area() -> USES -> pytest.approx() (test framework usage)

This pattern shows how KG extraction tools can identify:
- Which functions are tested by which test cases
- Test coverage relationships in the codebase
- Dependencies between test modules and production modules
- Testing framework usage patterns

The minimal test case is intentionally simple to clearly demonstrate the 
relationship patterns without complex testing logic obscuring the KG concepts.
"""

import pytest

from shapes import Circle, Rectangle, total_area

def test_total_area():
    circle = Circle(radius=1.0)
    rect = Rectangle(width=2.0, height=3.0)
    expected = 3.141592653589793 + 6.0
    assert total_area([circle, rect]) == pytest.approx(expected)

