# ───────────────────────────── file: math_utils.py ─────────────────────────────
"""
Utility math helpers used by the shapes package.
"""

import math

PI: float = math.pi  # global constant


def clamp(value: float, min_value: float, max_value: float) -> float:
    """
    Restrict *value* to the inclusive range ``[min_value, max_value]``.
    """
    return max(min_value, min(value, max_value))
