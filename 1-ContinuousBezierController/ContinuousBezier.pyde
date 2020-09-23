from math import *
import random
from Modules import *

prev, first = None, None
status = 0
controlPoints = []
anotherControlLength = 0
bezierPoints = []
selectedItem = None
selectedPoint = None
continuousBezierLineGroup = []
selectedBezier = None
def drawBeziers():
    global continuousBezierLineGroup
    background(255)
    for continuousBezierLine in continuousBezierLineGroup:
        continuousBezierLine.first.displayBezierLine()
def mouseMoved():
    global controlPoints,status,anotherControlLength
    global selectedItem
    global first
    global continuousBezierLineGroup,selectedBezier
    if status == 4:
        return
    status = 1
    selectedItem = None
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
def mousePressed():
    global prev,first,status,controlPoints,anotherControlLength,controller,bezierPoints
    global selectedItem,selectedPoint
    global continuousBezierLineGroup,selectedBezier
    if selectedPoint != None:
        selectedPoint.release()
    selectedPoint = None
    if selectedItem == None:
        b = BezierPoint(mouseX,mouseY,prev)
        controlPoints.extend([b.cPrev, b.cNext])
        bezierPoints.append(b)
        if first == None:
            first = b
            first.isFirst = True
            newBezier = ContinuousBezierLine(first)
            continuousBezierLineGroup.append(newBezier)
            selectedBezier = newBezier
        drawBeziers()
        prev = b
        b.parent = first.parent
        status = 4
    if status == 3:
        selectedPoint = selectedItem
        selectedPoint.select()
        drawBeziers()
    if status == 100:
        selectedPoint = selectedItem
        selectedPoint.select()
        first.prev, prev.next = prev, first
        drawBeziers()
        first, prev = None, None

def mouseDragged():
    global prev,anotherControlLength,selectedItem,continuousBezierLineGroup
    if selectedItem != None:
        selectedItem.adjust(mouseX,mouseY,anotherControlLength)
    else:
        prev.setControlFirst(mouseX,mouseY)
    drawBeziers()
def mouseReleased():
    global status,selectedItem
    status ,selectedItem = 0, None
def setup():
    rectMode(CENTER)
    size(1000,1000)
    background(255)
    smooth(8)
    noFill()
def draw():
    global status
def keyPressed():
    global status,selectedItem,first,controlPoints,bezierPoints,prev,first,selectedPoint
    global continuousBezierLineGroup,selectedBezier
    print(key == BACKSPACE)
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
            drawBeziers()