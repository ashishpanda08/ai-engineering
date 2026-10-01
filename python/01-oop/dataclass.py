"""
Dataclass: classes that hold data.
- It writes __init__ and some other stuff by itself.

"""

from dataclasses import dataclass


# without dataclass:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point = Point(10, 20)
print(point.x, point.y)


# with dataclass
@dataclass
class DataPoint:
    x: int
    y: int


datapoint = DataPoint(10, 20)
print(datapoint.x, datapoint.y)
