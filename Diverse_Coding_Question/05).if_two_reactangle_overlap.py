"""
Given two rectangles, find if the given two rectangles overlap or not.
Note that a rectangle can be represented by two coordinates, top left and bottom right.
So mainly we are given following four coordinates.
Time complexity is 0(1)
"""

class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def overlap(l1,r1,l2,r2):

        if (l1.x >= r2.x or l2.x >= r1.x):
            return False

        if(l1.y <= r2.y or l2.y <= r1.y):
            return False

        return True

l1 = Point(0, 10)
r1 = Point(10, 0)
l2 = Point(5, 5)
r2 = Point(15, 0)

if(overlap(l1, r1, l2, r2)):
    print("Rectangles Overlap")
else:
    print("Rectangles Don't Overlap")
