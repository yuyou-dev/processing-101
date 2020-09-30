from math import *
import random
class Vec3d(object):
    x = 0
    y = 0
    z = 0
    def __init__(self,x = 0,y = 0,z = 0):
        self.x = x
        self.y = y
        self.z = z
    def copy(self):
        return Vec3d(self.x,self.y,self.z)
    def display(self):
        point(self.x,self.y,self.z)
class Vec2d(object):
    x = 0
    y = 0
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
    def copy(self):
        return Vec2d(self.x,self.y)
    def add(self,x,y):
        self.x = self.x + x
        self.y = self.y + y
    def set(self,x,y):
        self.x = x
        self.y = y
    def distance(self,v):
        x1 = self.x
        y1 = self.y
        x2 = v.x
        y2 = v.y
        return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
class Line3d(object):
    p1 = Vec3d()
    p2 = Vec3d()
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
    def copy(self):
        return Line3d(self.p1.copy(),self.p2.copy())
    def display(self):
        #strokeWeight(5)
        line(self.p1.x,self.p1.y,self.p1.z,self.p2.x,self.p2.y,self.p2.z)
class Line(object):
    p1 = Vec2d()
    p2 = Vec2d()
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
    def copy(self):
        return Line(self.p1.copy(),self.p2.copy())
    def lerp(self,s):
        x = lerp(self.p1.x,self.p2.x,s)
        y = lerp(self.p1.y,self.p2.y,s)
        return Vec2d(x,y)
    def display(self):
        line(self.p1.x,self.p1.y,self.p2.x,self.p2.y)
