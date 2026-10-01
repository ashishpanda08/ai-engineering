from dataclasses import dataclass


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(3, 4)
print(p1)  # <__main__.Point object at 0x7f8a3c0d5f90>


p1 = Point(3, 4)
p2 = Point(3, 4)
print(p1 == p2)  # False !!

"""
Even though they have identical data, Python says they're not equal. Why?
Because by default, == checks if they're the same object in memory, not
whether their data matches. p1 and p2 are two separate objects that happen to
hold the same values — Python doesn't know you consider that "equal" unless
you tell it.

What __repr__ and __eq__ actually are

They're dunder methods ("double underscore" methods) — special methods Python
calls behind the scenes for built-in operations:

__repr__ → called when you print() an object or look at it in a console
__eq__ → called when you use == between two objects
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


"""
Now print(p1) gives Point(x=3, y=4) and p1 == p2 gives True. But you had to
write that yourself, every time, for every class.

What dataclass does

@dataclass looks at the fields you declared (x: int, y: int) and auto-writes
__init__, __repr__, and __eq__ for you, based on those fields
"""


@dataclass
class Point:
    x: int
    y: int


p1 = Point(3, 4)
p2 = Point(3, 4)
print(p1)  # Point(x=3, y=4)  ← free, correct repr
print(p1 == p2)  # True             ← free, correct equality

"""
Same result, zero manual code. That's the whole value proposition of
@dataclass: for simple data-holding objects, it saves you from writing the
same three boring methods over and over.

Make sense now? If so, go ahead and try today's contact-list exercise — you'll
likely want Contact as a dataclass specifically because you'll want print
(contact) to actually show the name/phone/email.
"""
