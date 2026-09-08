"""Mortar shot calculator: distance and compass bearing between two grid points.

Grid convention (matches games like ArmA/DayZ):
  - +x is east, +y is north.
  - Compass bearing: 0/360 = north, 90 = east, 180 = south, 270 = west.
  - One grid unit equals 100 meters, e.g. (100, 0) -> (101, 0) is 100 meters apart.
"""

import math

METERS_PER_UNIT = 100


def distance(x1, y1, x2, y2):
    """Return the distance in meters between grid points A(x1,y1) and B(x2,y2)."""
    dx = x2 - x1
    dy = y2 - y1
    return math.hypot(dx, dy) * METERS_PER_UNIT


def bearing(x1, y1, x2, y2):
    """Return the compass bearing in degrees (0-360) from A(x1,y1) to B(x2,y2)."""
    dx = x2 - x1
    dy = y2 - y1
    if dx == 0 and dy == 0:
        raise ValueError("Points A and B are identical; bearing is undefined")
    angle = math.degrees(math.atan2(dx, dy))
    return angle % 360


def calculate_shot(x1, y1, x2, y2):
    """Return (distance_in_meters, bearing_in_degrees) from A(x1,y1) to B(x2,y2)."""
    return distance(x1, y1, x2, y2), bearing(x1, y1, x2, y2)


def main():
    print("Mortar shot calculator")
    x1 = float(input("A x: "))
    y1 = float(input("A y: "))
    x2 = float(input("B x: "))
    y2 = float(input("B y: "))

    dist, brg = calculate_shot(x1, y1, x2, y2)
    print(f"Distance: {dist:.2f} m")
    print(f"Bearing:  {brg:.2f} deg")


if __name__ == "__main__":
    main()
