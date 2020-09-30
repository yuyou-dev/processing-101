from math import *
import random

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
    def dot(self,v):
        return self.x * v.x + self.y * v.y
    def cross(self,v):
        return self.x * v.y - self.y * v.x
    def perpendicular(self):
        return Vec2d(-self.y,self.x)
    def make(self,v):
        return Vec2d(v.x - self.x,v.y - self.y)
    def distance(self,v):
        x1 = self.x
        y1 = self.y
        x2 = v.x
        y2 = v.y
        return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
    
class Line2d(object):
    p1 = Vec2d()
    p2 = Vec2d()
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
    def copy(self):
        return Line2d(self.p1.copy(),self.p2.copy())
    def lerp(self,s):
        x = lerp(self.p1.x,self.p2.x,s)
        y = lerp(self.p1.y,self.p2.y,s)
        return Vec2d(x,y)
    def intersect(self,l):
        a = Vec2d(self.p2.x - self.p1.x,self.p2.y - self.p1.y)
        b = Vec2d(l.p2.x - l.p1.x,l.p2.y - l.p1.y)
        c = Vec2d(l.p1.x - self.p1.x,l.p1.y - self.p1.y)
        v1 = a.perpendicular()
        v2 = b.perpendicular()
        t = c.dot(v2) / a.dot(v2)
        u = -c.dot(v1) / b.dot(v1)
        if t > 0 and t < 1 and u > 0 and u < 1:
            v = Vec2d(self.p1.x,self.p1.y)
            v = v.add(a.mult(t))
            return Point(v.x,v.y)
        else:
            return None
    def check(self,x1,x2):
        if x1 < 0 and x2 > 0:
            return False
        if x1 > 0 and x2 < 0:
            return False
        return True
    def checkIntersect(self,l):
        vc = self.p1.make(self.p2)
        v1 = self.p1.make(l.p1)
        v2 = self.p1.make(l.p2)
        
        x1 = vc.cross(v1)
        x2 = vc.cross(v2)
        
        if self.check(x1,x2):
            return False
        
        vc = l.p1.make(l.p2)
        v1 = l.p1.make(self.p1)
        v2 = l.p1.make(self.p2)
        
        x1 = vc.cross(v1)
        x2 = vc.cross(v2)
        
        if self.check(x1,x2):
            return False
        
        return True
    def display(self):
        line(self.p1.x,self.p1.y,self.p2.x,self.p2.y)
        
class Poly(object):
    points = []
    def __init__(self,points):
        self.points = points
    def addPoint(self,v):
        self.points.append(v)
    def checkIntersect(self,p):
        for i in range(len(self.points)):
            pi1 = self.points[i]
            pi2 = self.points[(i + 1) % len(self.points)]
            l1 = Line2d(pi1,pi2)
            for j in range(len(p.points)):
                pj1 = p.points[j]
                pj2 = p.points[(i + 1) % len(p.points)]
                l2 = Line2d(pj1,pj2)
                if l1.checkIntersect(l2):
                    return True
        return False
    def display(self):
        beginShape()
        for v in self.points:
            vertex(v.x,v.y)
        endShape(CLOSE)
