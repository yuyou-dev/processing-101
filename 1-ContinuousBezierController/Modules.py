from math import *
import random

class Vec2d(object):
    x, y = 0, 0
    def __init__(self, x = 0, y = 0):
        self.x, self.y = x, y
    def copy(self):
        return Vec2d(self.x, self.y)
    def add(self, x, y):
        self.x = self.x + x
        self.y = self.y + y
    def set(self, x, y):
        self.x, self.y = x, y


class ContinuousBezierLine(object):
    first = None
    selected = False
    def __init__(self, first):
        self.first, first.parent = first, self
    def select(self):
        self.selected = True


class ControlPoint(Vec2d):
    parent = None
    another = None
    def __init__(self, x, y, parent):
        super(ControlPoint, self).__init__(x, y)
        self.parent = parent
    def peer(self, another):
        self.another, another.another = another, self
    def delete(self):
        self.parent = None
        self.another.parent = None
        self.another.another = None
        self.another = None
    def getControlLength(self):
        x1, y1 = self.parent.x, self.parent.y
        x2, y2 = self.x, self.y
        return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
    def adjust(self, x , y, d2):
        self.x, self.y = x, y
        d1 = self.getControlLength()
        px = d2 / d1 * (self.parent.x - x) + self.parent.x
        py = d2 / d1 * (self.parent.y - y) + self.parent.y
        self.another.set(px, py)


class BezierPoint(Vec2d):
    next, prev, parent = None, None, None
    cPrev, cNext = None, None
    selected = False
    isFirst = False
    def __init__(self, x, y, prev):
        super(BezierPoint, self).__init__(x, y)
        self.prev = prev
        if prev != None:
            prev.next = self
        self.cPrev = ControlPoint(x, y, self)
        self.cNext = ControlPoint(x, y, self)
        self.peer()
    def peer(self):
        self.cPrev.peer(self.cNext)
    def delete(self):
        if self.prev != None:
            self.prev.next = self.next
            if self.isFirst:
                self.prev.isFirst = True
                self.parent.first = self.prev
        if self.next != None:
            self.next.prev = self.prev
        self.cPrev.delete()
    def adjust(self, x, y, d):
        dx = x - self.x
        dy = y - self.y
        self.cPrev.add(dx, dy)
        self.cNext.add(dx, dy)
        self.x, self.y = x, y
    def select(self):
        self.selected = True
        self.parent.select()
    def release(self):
        self.selected = False
    def setNextControlPoint(self, x, y):
        self.cNext.set(x, y)
    def setPrevControlPoint(self, x, y):
        self.cPrev.set(x, y)
    def setControlFirst(self, x, y):
        self.setNextControlPoint(x, y)
        px = 2 * self.x - self.cNext.x
        py = 2 * self.y - self.cNext.y
        self.setPrevControlPoint(px, py)
    def getPoint(self):
        return self.copy()
    def displayPoint(self):
        point(self.x, self.y)
    def displayControlLine(self):
        stroke(13, 127, 190)
        strokeWeight(1)
        fill(255)
        line(self.cPrev.x, self.cPrev.y, self.x, self.y)
        line(self.x, self.y, self.cNext.x, self.cNext.y)
        circle(self.cPrev.x, self.cPrev.y, 5)
        circle(self.cNext.x, self.cNext.y, 5)
        if self.selected:
            fill(0, 132, 244)
        else:
            fill(255, 255, 255)
        rect(self.x, self.y, 16, 16)
    def displayLine(self):
        if self.prev != None:
            line(self.prev.x, self.prev.y, self.x, self.y)
        else:
            return
    def displayBezierLine(self, isFirst = False):
        if self.prev != None:
            p1 = self.prev.getPoint()
            p2 = self.getPoint()
            c1 = self.prev.cNext.copy()
            c2 = self.cPrev.copy()
            noFill()
            stroke(0, 0, 0, 100)
            strokeWeight(12)
            off = 5
            bezier(p1.x, p1.y + off, c1.x, c1.y + off, c2.x, c2.y + off, p2.x, p2.y + off)
            stroke(0, 0, 0)
            strokeWeight(12)
            bezier(p1.x, p1.y, c1.x, c1.y, c2.x, c2.y, p2.x, p2.y)
            stroke(251, 228, 20)
            strokeWeight(8)
            bezier(p1.x, p1.y, c1.x, c1.y, c2.x, c2.y, p2.x, p2.y)
        if self.next != None:
            if isFirst == False:
                if self.next.isFirst == False:
                    self.next.displayBezierLine()
        self.displayControlLine()