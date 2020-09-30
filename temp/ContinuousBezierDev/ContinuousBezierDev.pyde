from math import *
import random
from Modules import *

prev = None
first = None
status = 0
controlPoints = []
anotherControlLength = 0
bezierPoints = []
selectedItem = None
selectedPoint = None
continuousBezierLineGroup = []
selectedBezier = None
def mousePressed():
    global prev,first,status,controlPoints,anotherControlLength,controller,bezierPoints
    global selectedItem,selectedPoint
    global continuousBezierLineGroup,selectedBezier
    for b in bezierPoints:
        if abs(b.x - mouseX) < 16 and abs(b.y - mouseY) < 16:
            status = 3
            selectedItem = b
            if selectedItem == first:
                status = 100
    for c in controlPoints:
        if abs(c.x - mouseX) < 3 and abs(c.y - mouseY) < 3:
            status = 2
            selectedItem = c
            anotherControlLength = c.another.getControlLength()
            
    if selectedPoint != None:
        selectedPoint.release()
    selectedPoint = None
    if selectedItem == None:
        b = BezierPoint(mouseX,mouseY,prev)
        controlPoints.append(b.cPrev)
        controlPoints.append(b.cNext)
        bezierPoints.append(b)
        if first == None:
            first = b
            first.isFirst = True
            newBezier = ContinuousBezierLine(first)
            continuousBezierLineGroup.append(newBezier)
            selectedBezier = newBezier
        for continuousBezierLine in continuousBezierLineGroup:
            continuousBezierLine.first.displayBezierLine()
        prev = b
        b.parent = first.parent
        status = 4
    if status == 3:
        selectedPoint = selectedItem
        selectedPoint.select()
        background(255)
        for continuousBezierLine in continuousBezierLineGroup:
            continuousBezierLine.first.displayBezierLine()
    if status == 100:
        selectedPoint = selectedItem
        selectedPoint.select()
        first.prev = prev
        prev.next = first
        first.displayBezierLine()
        first = None
        prev = None
def mouseDragged():
    global prev,status,first,anotherControlLength
    global selectedItem
    global continuousBezierLineGroup,selectedBezier
    if selectedItem != None:
        if status == 2:
            anotherControlLength = selectedItem.another.getControlLength()
            selectedItem.adjust(mouseX,mouseY,anotherControlLength)
        elif status == 3 or status == 100:
            selectedItem.adjust(mouseX,mouseY)
    else:
        prev.createAndMoveControlPoint(mouseX,mouseY)
    background(255)  
    for continuousBezierLine in continuousBezierLineGroup:
        continuousBezierLine.first.displayBezierLine()
def mouseReleased():
    global status,selectedItem
    status = 0
    selectedItem = None
def setup():
    rectMode(CENTER)
    size(1000,1000)
    background(255)
    smooth(8)
    noFill()
def draw():
    global status
def keyPressed():
    global status,selectedItem,controlPoints,bezierPoints,prev,first,selectedPoint
    global continuousBezierLineGroup,selectedBezier
    if key == BACKSPACE:
        if selectedPoint != None:
            if selectedPoint == first:
                first = selectedPoint.next
                first.isFirst = True
            if selectedPoint == prev:
                prev = selectedPoint.prev
            selectedPoint.delete()
            controlPoints.remove(selectedPoint.cPrev)
            controlPoints.remove(selectedPoint.cNext)
            bezierPoints.remove(selectedPoint)
            selectedPoint = None
            background(255)
            for continuousBezierLine in continuousBezierLineGroup:
                continuousBezierLine.first.displayBezierLine()
