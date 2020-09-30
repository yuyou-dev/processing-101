from math import *
import random
from Modules import *

def drawSin():
    step = 3
    for x in range(0,width,step):
        y1 = sin(x / 30.0) * 100 + height / 2
        y2 = sin((x + step) / 30.0) * 100 + height / 2
        line(x,y1,x+step,y2) 
def setup():
    size(1000,1000,P3D)
    smooth(8)
    

    
def getSpherePoint(r,a,b):
    x = r * sin(a) * cos(b)
    y = r * cos(a) * cos(b)
    z = r * sin(b)
    return Vec3d(x,y,z)
    
def drawSphereSurface(r1,r2,x,y,aStart,aEnd,bStart,bEnd):
    push()
    translate(x,y)
    
    aStep = 10
    bStep = 10
    
    beginShape(QUAD_STRIP)
    for j in range(0,bStep + 1):
        a = aStart
        bs = map(j,0,bStep,bStart,bEnd)
        p1 = getSpherePoint(r1,a,bs)
        p2 = getSpherePoint(r2,a,bs)
        vertex(p1.x,p1.y,p1.z)
        vertex(p2.x,p2.y,p2.z)
    endShape()

    beginShape(QUAD_STRIP)
    for j in range(0,bStep + 1):
        a = aEnd
        bs = map(j,0,bStep,bStart,bEnd)
        p1 = getSpherePoint(r1,a,bs)
        p2 = getSpherePoint(r2,a,bs)
        vertex(p1.x,p1.y,p1.z)
        vertex(p2.x,p2.y,p2.z)
    endShape()
    
    beginShape(QUAD_STRIP)
    for i in range(0,aStep + 1):
        b = bEnd
        aas = map(i,0,aStep,aStart,aEnd)
        p1 = getSpherePoint(r1,aas,b)
        p2 = getSpherePoint(r2,aas,b)
        vertex(p1.x,p1.y,p1.z)
        vertex(p2.x,p2.y,p2.z)
    endShape()
    beginShape(QUAD_STRIP)
    for i in range(0,aStep + 1):
        b = bStart
        aas = map(i,0,aStep,aStart,aEnd)
        p1 = getSpherePoint(r1,aas,b)
        p2 = getSpherePoint(r2,aas,b)
        vertex(p1.x,p1.y,p1.z)
        vertex(p2.x,p2.y,p2.z)
    endShape()   
        
    for i in range(1,aStep + 1):
        beginShape(QUAD_STRIP)
        for j in range(0,bStep + 1):
            b = map(j,0,bStep,bStart,bEnd)
            aas = map(i,0,aStep,aStart,aEnd)
            aae = map(i - 1,0,aStep,aStart,aEnd)
            p1 = getSpherePoint(r2,aas,b)
            p2 = getSpherePoint(r2,aae,b)
            vertex(p1.x,p1.y,p1.z)
            vertex(p2.x,p2.y,p2.z)
        endShape()
    for i in range(1,aStep + 1):
        beginShape(QUAD_STRIP)
        for j in range(0,bStep + 1):
            b = map(j,0,bStep,bStart,bEnd)
            aas = map(i,0,aStep,aStart,aEnd)
            aae = map(i - 1,0,aStep,aStart,aEnd)
            p1 = getSpherePoint(r1,aas,b)
            p2 = getSpherePoint(r1,aae,b)
            vertex(p1.x,p1.y,p1.z)
            vertex(p2.x,p2.y,p2.z)
        endShape()
    pop()

def drawSphere(r,x0,y0):
    push()
    translate(x0,y0)
    stepLat = 20
    stepLong = 20
    for i in range(stepLat):
        for j in range(stepLong):
            a = map(i,0,stepLat,0,TAU / 2.0)
            b = map(j,0,stepLong,0,TAU)
            x = r * sin(a) * cos(b)
            y = r * cos(a) * cos(b)
            z = r * sin(b)
            strokeWeight(5)
            point(x,y,z)
    pop()
s = 0
v = 10
a = 0
def draw():
    global s,v,a
    a = -s / 100.0
    v = v + a
    s = s + v
    
    sc = map(s,-100,200,0,0.6)
    
    background(200)
    p1 = VisualPoint(100,100)
    p2 = VisualPoint(100,300)
    p3 = VisualPoint(300,300)
    p4 = VisualPoint(300,100)
    
    r = 100
    polyGroup = []
    for i in range(0,360,60):
        alpla = i / 360.0 * TAU
        y = r * sin(alpla)
        x = r * cos(alpla)
        #circle(x + 200,y + 200,20)
        polyGroup.append(VisualPoint(x,y))
    poly = Polygon(polyGroup)
    push()
    translate(200,200)
    poly.display()
    pop()
    
    for i in range(5):
        poly.divide(sc)
    push()
    translate(200,200)
    scale(sc + 0.7)
    poly.display()
    pop()
    drawSin()
    #print(s)
    push()
    translate(500,500)
    rotateX(frameCount / 500.0 * TAU)
    rotateY(frameCount / 800.0 * TAU)
    drawSphere(300,0,0)
    fill(255,255,0)
    
    pork = Pork(250,300,0,0,TAU / 10,TAU / 5,TAU / 20,TAU / 10)
    pork.display()
    #drawSphereSurface(250,300,0,0,TAU / 10,TAU / 5,TAU / 20,TAU / 10)
    pop()
    
    
