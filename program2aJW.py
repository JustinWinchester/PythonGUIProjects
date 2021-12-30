# *************************************************************************************************
# Program:     2a
# Programmer:  Justin A Winchester!
# Date:        June 3, 2021
# Description: This program creates a class for a point on a coordinate plane.
# It has multiple functions that perform various operations or return information about a given point,
# such as it's position, it's position from the origin, or the quadrant that it resides in.

# **************************************************************************************************
import math
class Point:
    x=0
    y=0

    def goto(self, newx, newy):
        self.x = newx
        self.y = newy

    def position(self):
        print(f"({self.x},{self.y})")

    def fromOrigin(self):
        return math.sqrt((self.x**2 + self.y**2))

    def Quadrant(self):
        quad = {1:'Quadrant I', 2:'Quadrant II', 3:'Quadrant III', 4: 'Quadrant IV'}
        if self.x > 0 and self.y > 0:
            print(quad[1])
        elif self.x < 0 and self.y > 0:
            print(quad[2])
        elif self.x < 0 and self.y < 0:
            print(quad[3])
        elif self.x > 0 and self.y < 0:
            print(quad[4])
        elif self.x == 0:
            print("Point is on Y - Axis")
        elif self.y == 0:
            print("Point is on the X- Axis")

    def move(self, direction):
        if direction == "u":
            self.y += 1
        elif direction == "d":
            self.y -= 1
        elif direction == "l":
            self.x -= 1
        elif direction == "r":
            self.x += 1
        else:
            print("Sorry Invalid Direction! Please Enter 1 of the 4 selections:\n'u' 'd' 'l' 'r' ")

p = Point()
p.goto(5,3)
p.position()
print(p.x,p.y)
print(p.fromOrigin())
p.Quadrant()
p.move('u')
print(p.x,p.y)