from math import *
import random
from Modules import *
            
class Controller(object):
    first = None
    selectedControlPoint = None
    selectedBezierPoint = None
    controlPoints = []
    status = 0
    current = None
    def __init__(self,first = None):
        self.first = first
    def display(self):
        self.start.displayBezierLine()
    def addPoint(self,x,y):
        if self.start == None:
            p = BezierPoint(x,y,None)
            self.current = p
            self.start = p
        else:
            p = BezierPoint(x,y,self.current)
            self.current = p
        self.controlPoints.append(p.cPrev)
        self.controlPoints.append(p.cNext)
    
prev = None
first = None
status = 0
controlPoints = []
selectedControlPoint = None
anotherControlLength = 0
controller = None
bezierPoints = []
def mouseMoved():
    global controlPoints,selectedControlPoint,status
    selected = False
    
    if status == 3:
        return
    status = 0
    for c in controlPoints:
        if abs(c.x - mouseX) < 3 and abs(c.y - mouseY) < 3:
            selected = True
            status = 2
            selectedControlPoint = c
    for b in bezierPoints:
        if abs(b.x - mouseX) < 3 and abs(b.y - mouseY) < 3:
            return
def mousePressed():
    global prev,first,status,controlPoints,selectedControlPoint,anotherControlLength,controller,bezierPoints
    
    if status == 2:
        anotherControlLength = selectedControlPoint.another.getControlLength()
        status = 3
        return
    
    if status == 0:
        status = 1
        if prev == None:
            prev = BezierPoint(mouseX,mouseY,None)
            controlPoints.append(prev.cPrev)
            controlPoints.append(prev.cNext)
            bezierPoints.append(prev)
            if first == None:
                first = prev
                first.displayBezierLine()
        else:
            current = BezierPoint(mouseX,mouseY,prev)
            bezierPoints.append(prev)
            controlPoints.append(current.cPrev)
            controlPoints.append(current.cNext)
            prev = current
def mouseDragged():
    global prev,status,selectedControlPoint,first,anotherControlLength
    if status == 1:
        if prev != None:
            if first != None:
                prev.setControlFirst(mouseX,mouseY)
                background(200)
                first.displayBezierLine()
    elif status == 3:
        selectedControlPoint.adjuct(mouseX,mouseY,anotherControlLength)
        background(200)
        first.displayBezierLine()
def mouseReleased():
    global prev,first,status
    if status == 1:
        prev.setControlFirst(mouseX,mouseY)
    status = 0
def setup():
    rectMode(CENTER)
    size(1000,1000,P3D)
    smooth(8)
    noFill()
    strokeWeight(5)
    stroke(0)
    global controller
    controller = Controller()
    
def draw():
    global status
