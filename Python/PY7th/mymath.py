import math

def triangle_area(base: float, height: float) -> float:
    return 0.5 * base * height

def circle_area(radius: float) -> float:
    return math.pi * radius ** 2

def rectangular_prism_volume(length: float, width: float, height: float) -> float:
    return length * width * height