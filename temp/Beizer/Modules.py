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
    def set(self,x,y):
        self.x = x
        self.y = y
class ControlPoint(Vec2d):
    parent = None
    another = None
    def __init__(self,x,y,parent):
        super(ControlPoint,self).__init__(x,y)
        self.parent = parent
    def peer(self,another):
        self.another = another
        another.another = self
    def getControlLength(self):
        x1 = self.parent.x
        y1 = self.parent.y
        x2 = self.x
        y2 = self.y
        return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
    def adjuct(self,x,y,d2):
        self.x = x
        self.y = y
        d1 = self.getControlLength()
        px = d2 / d1 * (self.parent.x - x) + self.parent.x
        py = d2 / d1 * (self.parent.y - y) + self.parent.y
        self.another.set(px,py)
class BezierPoint(Vec2d):
    next = None
    prev = None
    cPrev = None
    cNext = None
    def __init__(self,x,y,prev):
        super(BezierPoint,self).__init__(x,y)
        self.prev = prev
        if(prev != None):prev.next = self
        self.cPrev = ControlPoint(x,y,self)
        self.cNext = ControlPoint(x,y,self)
        self.peer()
    def peer(self):
        self.cPrev.peer(self.cNext)
    def setNextControlPoint(self,x,y):
        self.cNext.set(x,y)
    def setPrevControlPoint(self,x,y):
        self.cPrev.set(x,y)
    def setControlFirst(self,x,y):
        self.setNextControlPoint(x,y)
        px = 2 * self.x - self.cNext.x
        py = 2 * self.y - self.cNext.y
        self.setPrevControlPoint(px,py)
    def getPoint(self):
        return self.copy()
    def displayPoint(self):
        point(self.x,self.y)
    def displayControlLine(self):
        stroke(0,132,244)
        strokeWeight(1)
        fill(255)
        line(self.cPrev.x,self.cPrev.y,self.cNext.x,self.cNext.y)
        circle(self.cPrev.x,self.cPrev.y,5)
        circle(self.cNext.x,self.cNext.y,5)
        rect(self.x,self.y,8,8)
    def displayLine(self):
        if self.prev != None:
            line(self.prev.x,self.prev.y,self.x,self.y)
        else:return
    def displayBezierLine(self):
        if self.prev != None:
            p1 = self.prev.getPoint()
            p2 = self.getPoint()
            c1 = self.prev.cNext.copy()
            c2 = self.cPrev.copy()
            stroke(0,132,244)
            strokeWeight(1)
            noFill()
            bezier(p1.x,p1.y,c1.x,c1.y,c2.x,c2.y,p2.x,p2.y)
        if self.next != None:
            self.next.displayBezierLine()
        self.displayControlLine()
