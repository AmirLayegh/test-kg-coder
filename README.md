# Knowledge Graph Extraction Demo Repository

This repository serves as a **demonstration and test codebase for Knowledge Graph (KG) extraction tools**. It contains intentionally simple Python code that showcases various types of code relationships and graph edges that knowledge graph extraction systems typically identify and model.

## Purpose

The primary purpose of this repository is to provide a clear, minimal example of how different code constructs create relationships that can be extracted into a knowledge graph. Rather than being a functional geometry library, this codebase is designed to demonstrate specific relationship patterns that KG extraction tools look for in codebases.

## Code Relationship Types Demonstrated

This repository demonstrates several key relationship types (graph edges) commonly found in code knowledge graphs:

### 1. **INHERITS_FROM** Edges
- `Circle` class inherits from `Shape` base class
- `Rectangle` class inherits from `Shape` base class
- Demonstrates class hierarchy relationships

### 2. **HAS_METHOD** Edges
- Classes define methods (e.g., `Shape.area()`, `Circle.area()`, `Rectangle.area()`)
- Shows the relationship between classes and their method definitions

### 3. **CALLS** Edges
Multiple types of function/method call relationships:
- **Cross-module calls**: `Rectangle.__init__()` calls `clamp()` from `math_utils.py`
- **Method-to-method calls**: `total_area()` function calls `Shape.area()` method on each shape
- **Constant usage**: `Circle.area()` uses the `PI` constant from `math_utils.py`

### 4. **USES_VAR** Edges
- `Rectangle.__init__()` uses `width` and `height` parameters
- `Circle.area()` references `self.radius` attribute
- Demonstrates variable usage and dependency relationships

### 5. **TestCase → Function** Edges
- `test_total_area()` in `test_shapes.py` calls and tests the `total_area()` function
- Shows how test cases create relationships with the functions they test

## Repository Structure

The codebase consists of three Python files in the `src/` directory, each serving a specific role in demonstrating different relationship types:

```
src/
├── math_utils.py    # Utility functions and constants for cross-module dependencies
├── shapes.py        # Core geometry classes demonstrating inheritance and method relationships
└── test_shapes.py   # Test cases showing TestCase → Function edges
```

### File Descriptions

#### `src/math_utils.py`
- **Purpose**: Provides utility functions and constants to demonstrate cross-module dependencies
- **Key Elements**:
  - `PI` constant: Used by `Circle.area()` to show constant usage relationships
  - `clamp()` function: Called by `Rectangle.__init__()` to show cross-module function calls

#### `src/shapes.py`
- **Purpose**: Contains the main geometry classes that demonstrate inheritance, method definitions, and various call relationships
- **Key Elements**:
  - `Shape` base class: Demonstrates abstract base class patterns
  - `Circle` and `Rectangle` classes: Show inheritance relationships and method implementations
  - `total_area()` function: Demonstrates function-to-method call patterns

#### `src/test_shapes.py`
- **Purpose**: Contains test cases that demonstrate TestCase → Function relationship edges
- **Key Elements**:
  - `test_total_area()`: Shows how test functions create relationships with the code they test

## Simple Geometry Domain Choice

The geometry domain (shapes, areas, mathematical operations) was chosen because:

1. **Simplicity**: Easy to understand without domain expertise
2. **Natural Relationships**: Geometric concepts naturally create inheritance hierarchies (Shape → Circle/Rectangle)
3. **Cross-module Dependencies**: Mathematical operations naturally require utility functions and constants
4. **Clear Boundaries**: Well-defined interfaces between different components

## How the Files Work Together

The three files create a web of relationships that demonstrate various KG extraction scenarios:

1. **Inheritance Chain**: `shapes.py` defines a base `Shape` class with concrete implementations
2. **Cross-module Dependencies**: `shapes.py` imports and uses utilities from `math_utils.py`
3. **Function Composition**: `total_area()` orchestrates calls to individual shape methods
4. **Test Coverage**: `test_shapes.py` exercises the functionality and creates test-to-code relationships

## Dependencies

- **numpy**: Used for mathematical operations (demonstrates external library usage)
- **pytest**: Used for testing framework (demonstrates test relationship patterns)
- **Standard Library**: `math`, `dataclasses` (shows standard library usage patterns)

## Usage for KG Extraction Tools

This repository can be used to:

1. **Test KG extraction algorithms** on a known, well-documented codebase
2. **Validate relationship detection** by comparing extracted relationships against the documented ones
3. **Benchmark extraction tools** using a simple, controlled example
4. **Demonstrate KG concepts** to developers learning about code knowledge graphs

The explicit comments and documentation in the code make it easy to verify that extraction tools are correctly identifying the intended relationships.
