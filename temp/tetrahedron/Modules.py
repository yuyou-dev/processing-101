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
    def rotateZ(self,a):
        v = Vec3d()
        x = cos(a) * self.x - sin(a) * self.y
        y = sin(a) * self.x + cos(a) * self.y
        return Vec3d(x,y,self.z)
    def distance(self,p):
        dx = self.x - p.x
        dy = self.y - p.y
        dz = self.z - p.z
        return sqrt(dx * dx + dy * dy + dz * dz)
    def middle(self,p):
        dx = (self.x + p.x) / 2.0
        dy = (self.y + p.y) / 2.0
        dz = (self.z + p.z) / 2.0
        return Vec3d(dx,dy,dz)
    def display(self):
        point(self.x,self.y,self.z)
class Triangle(object):
    p1 = None
    p2 = None
    p3 = None
    def __init__(self,p1 = None,p2 = None,p3 = None):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def make(self,r):
        self.p1 = Vec3d(0,r,0)
        self.p2 = self.p1.rotateZ(TAU / 3)
        self.p3 = self.p1.rotateZ(TAU / 3 * 2)
    def center(self):
        dx = (self.p1.x + self.p2.x + self.p3.x) / 3
        dy = (self.p1.y + self.p2.y + self.p3.y) / 3
        dz = (self.p1.z + self.p2.z + self.p3.z) / 3
        return Vec3d(dx,dy,dz)
    def getEdgeLength(self):
        return self.p1.distance(self.p2)
    def display(self):
        beginShape(TRIANGLES)
        vertex(self.p1.x,self.p1.y,self.p1.z)
        vertex(self.p2.x,self.p2.y,self.p2.z)
        vertex(self.p3.x,self.p3.y,self.p3.z)
        endShape()
class Tetrahedron(object):
    p1 = None
    p2 = None
    p3 = None
    p4 = None
    children = None
    self = color(255)
    def __init__(self,p1 = None,p2 = None,p3 = None,p4 = None):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.children = []
        self.c = self.getColor()
    def getColor(self):
        colors = [color(13,127,190),color(245,10,10),color(251,228,20),color(255,255,255)]
        return colors[random.randint(0,3)]
    def make(self,p1,p2 = None,p3 = None):
        if type(p1) != Vec3d:
            rxy = p1
            bottom = Triangle()
            bottom.make(rxy)
            p4 = Vec3d(0,0,sqrt(6) / 3.0 * bottom.getEdgeLength())
            self.p1 = bottom.p1.copy()
            self.p2 = bottom.p2.copy()
            self.p3 = bottom.p3.copy()
            self.p4 = p4.copy()
        else:
            bottom = Triangle(p1,p2,p3)
            dz = sqrt(6) / 3.0 * bottom.getEdgeLength() + bottom.center().z
            center = bottom.center()
            self.p4 = Vec3d(center.x,center.y,dz)
            self.p1 = bottom.p1.copy()
            self.p2 = bottom.p2.copy()
            self.p3 = bottom.p3.copy()
    def divide(self,count):
        v1 = self.p1.middle(self.p2)
        v2 = self.p2.middle(self.p3)
        v3 = self.p3.middle(self.p1)
        s1 = Tetrahedron()
        s2 = Tetrahedron()
        s3 = Tetrahedron()
        s4 = Tetrahedron()
        s5 = Tetrahedron()
        s1.make(self.p1,v1,v3)
        s2.make(v1,self.p2,v2)
        s3.make(v3,v2,self.p3)
        s4.make(s1.p4.copy(),s2.p4.copy(),s3.p4.copy())
        s5.make(v1,v2,v3)
        group = [s1,s2,s3,s4,s5]
        if count > 1:
            for s in group:
                if random.random() > 0.3:
                    s.divide(count - 1)
        self.children = group
    def displayAll(self):
        if len(self.children) == 0:
            self.display()
        else:
            for child in self.children:
                child.displayAll()
            
    def display(self):
        t1 = Triangle(self.p1,self.p2,self.p3)
        t2 = Triangle(self.p1,self.p2,self.p4)
        t3 = Triangle(self.p1,self.p3,self.p4)
        t4 = Triangle(self.p2,self.p3,self.p4)
        fill(self.c)
        strokeWeight(2)
        t1.display()
        t2.display()
        t3.display()
        t4.display()
        
