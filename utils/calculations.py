from math import sqrt
from typing import List


def calculate_midpoint(x1: float, y1: float, x2: float, y2: float) -> List:
    return [(x1 + x2) / 2, (y1 + y2) / 2]

def calculate_points_segment(x1: float, y1: float, x2: float, y2: float) -> float:
    return sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))


