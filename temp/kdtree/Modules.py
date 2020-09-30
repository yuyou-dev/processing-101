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
class VisualPoint(Vec2d):
    next = None
    prev = None
    first = False
    parent = None
    def __init__(self,x,y):
        super(VisualPoint,self).__init__(x,y)
    def divide(self,s):
        next = self.next
        lNext = Line(self.copy(),self.next.copy())
        lPrev = Line(self.copy(),self.prev.copy())
        vNext = lNext.lerp(s)
        vPrev = lPrev.lerp(s)
        pNext = VisualPoint(vNext.x,vNext.y)
        pPrev = VisualPoint(vPrev.x,vPrev.y)
        if self.first == True:
            self.first = False
            pPrev.first = True
            pPrev.parent = self.parent
            self.parent.first = pPrev
        self.addNext(pNext)
        self.addPrev(pPrev)
        self.remove()
        if next.first != True:
            next.divide(s)
    def addNext(self,p):
        self.next.prev = p
        p.next = self.next
        self.next = p
        p.prev = self
    def addPrev(self,p):
        self.prev.next = p
        p.prev = self.prev
        p.next = self
        self.prev = p
    def remove(self):
        self.next.prev = self.prev
        self.prev.next = self.next
    def display(self):
        if self.next != None:
            x1 = self.x
            y1 = self.y
            x2 = self.next.x
            y2 = self.next.y
            line(x1,y1,x2,y2)
            if self.next.first != True:
                self.next.display()
class Polygon(object):
    first = Vec2d()
    def __init__(self,points):
        self.first = points[0]
        self.first.next = self.first
        self.first.prev = self.first
        self.first.first = True
        self.first.parent = self
        
        for i in range(1,len(points)):
            prev = points[i - 1]
            p = points[i]
            prev.addNext(p)
    def divide(self,s):
        self.first.divide(s)
    def display(self):
        self.first.display()

class Pork(object):
    r1 = 0
    r2 = 0
    x = 0
    y = 0
    aStart = 0
    aEnd = 0
    bStart = 0
    bEnd = 0
    def __init__(self,r1,r2,x,y,aStart,aEnd,bStart,bEnd):
        self.r1 = r1
        self.r2 = r2
        self.x = x
        self.y = y
        self.aStart = aStart
        self.bStart = bStart
        self.aEnd = aEnd
        self.bEnd = bEnd
    def getSpherePoint(self,r,a,b):
        x = r * sin(a) * cos(b)
        y = r * cos(a) * cos(b)
        z = r * sin(b)
        return Vec3d(x,y,z)
    def display(self,c = color(255,255,0)):
        fill(c)
        aStart = self.aStart
        aEnd = self.aEnd
        bStart = self.bStart
        bEnd = self.bEnd
        r1 = self.r1
        r2 = self.r2
        x = self.x
        y = self.y
        push()
        translate(x,y)
        aStep = 10
        bStep = 10
        beginShape(QUAD_STRIP)
        for j in range(0,bStep + 1):
            a = aStart
            bs = map(j,0,bStep,bStart,bEnd)
            p1 = self.getSpherePoint(r1,a,bs)
            p2 = self.getSpherePoint(r2,a,bs)
            vertex(p1.x,p1.y,p1.z)
            vertex(p2.x,p2.y,p2.z)
        endShape()
    
        beginShape(QUAD_STRIP)
        for j in range(0,bStep + 1):
            a = aEnd
            bs = map(j,0,bStep,bStart,bEnd)
            p1 = self.getSpherePoint(r1,a,bs)
            p2 = self.getSpherePoint(r2,a,bs)
            vertex(p1.x,p1.y,p1.z)
            vertex(p2.x,p2.y,p2.z)
        endShape()
        
        beginShape(QUAD_STRIP)
        for i in range(0,aStep + 1):
            b = bEnd
            aas = map(i,0,aStep,aStart,aEnd)
            p1 = self.getSpherePoint(r1,aas,b)
            p2 = self.getSpherePoint(r2,aas,b)
            vertex(p1.x,p1.y,p1.z)
            vertex(p2.x,p2.y,p2.z)
        endShape()
        beginShape(QUAD_STRIP)
        for i in range(0,aStep + 1):
            b = bStart
            aas = map(i,0,aStep,aStart,aEnd)
            p1 = self.getSpherePoint(r1,aas,b)
            p2 = self.getSpherePoint(r2,aas,b)
            vertex(p1.x,p1.y,p1.z)
            vertex(p2.x,p2.y,p2.z)
        endShape()   
            
        for i in range(1,aStep + 1):
            beginShape(QUAD_STRIP)
            for j in range(0,bStep + 1):
                b = map(j,0,bStep,bStart,bEnd)
                aas = map(i,0,aStep,aStart,aEnd)
                aae = map(i - 1,0,aStep,aStart,aEnd)
                p1 = self.getSpherePoint(r2,aas,b)
                p2 = self.getSpherePoint(r2,aae,b)
                vertex(p1.x,p1.y,p1.z)
                vertex(p2.x,p2.y,p2.z)
            endShape()
        for i in range(1,aStep + 1):
            beginShape(QUAD_STRIP)
            for j in range(0,bStep + 1):
                b = map(j,0,bStep,bStart,bEnd)
                aas = map(i,0,aStep,aStart,aEnd)
                aae = map(i - 1,0,aStep,aStart,aEnd)
                p1 = self.getSpherePoint(r1,aas,b)
                p2 = self.getSpherePoint(r1,aae,b)
                vertex(p1.x,p1.y,p1.z)
                vertex(p2.x,p2.y,p2.z)
            endShape()
        pop()
            
        
        
    
