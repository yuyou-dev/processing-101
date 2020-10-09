from math import *
import random


class Vec3d(object):
    x, y, z = 0, 0, 0
    def __init__(self,x = 0,y = 0,z = 0):
        self.x, self.y, self.z = x, y, z
        
    def copy(self):
        return Vec3d(self.x, self.y, self.z)

    def display(self):
        point(self.x, self.y, self.z)

class Vec2d(object):
    x, y = 0, 0

    def __init__(self,x = 0,y = 0):
        self.x, self.y = x, y

    def copy(self):
        return Vec2d(self.x, self.y)

    def add(self,x,y):
        self.x = self.x + x
        self.y = self.y + y

    def set(self,x,y):
        self.x, self.y = x, y

    def distance(self,v):
        x1, y1 = self.x, self.y
        x2, y2 = v.x, v.y
        return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


class Rect2d(object):
    v1, v2 = None, None
    def __init__(self,v1 = Vec2d(),v2 = Vec2d()):
        self.v1 = v1
        self.v2 = v2


class Line3d(object):
    p1, p2 = Vec3d(), Vec3d()
    def __init__(self, p1, p2):
        self.p1, self.p2 = p1, p2

    def copy(self):
        return Line3d(self.p1.copy(), self.p2.copy())

    def display(self):
        line(self.p1.x, self.p1.y, self.p1.z, self.p2.x, self.p2.y, self.p2.z)


class Line(object):
    p1, p2 = Vec2d(), Vec2d()
    def __init__(self,p1,p2):
        self.p1, self.p2 = p1, p2

    def copy(self):
        return Line(self.p1.copy(), self.p2.copy())

    def lerp(self,s):
        x = lerp(self.p1.x, self.p2.x,s)
        y = lerp(self.p1.y, self.p2.y,s)
        return Vec2d(x, y)

    def display(self):
        line(self.p1.x, self.p1.y, self.p2.x, self.p2.y)