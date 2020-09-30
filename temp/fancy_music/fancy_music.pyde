add_library('sound')
from math import *
import random
from Modules import *

porkGroup = []
def setup():
    size(1000,1000,P3D)
    global porkGroup
    r1 = 300
    r2 = 400
    x = width / 2
    y = height / 2
    aStart = 0
    aEnd = TAU / 4
    bStart = 0
    bEnd = TAU / 16
    for i in range(8):
        pork = Pork(r1,r2,x,y,aStart,aEnd,bStart,bEnd)
        porkGroup.append(pork)
    smooth(8)
def draw():
    background(255)
    global porkGroup

    push()
    translate(500,500)
    translate(0,0,-1000)
    
    rotateX(frameCount / 500.0 * TAU)
    rotateY(TAU / 2)
    rotateX(TAU / 4)
    rotateZ(frameCount / 300.0 * TAU)
    
    l = len(porkGroup)
    for i in range(l):
        
        pork = porkGroup[i]
        type = '1'
        r1 = 0
        r2 = 380
        aStart = i * 1.0 / l * TAU / 2.0 + TAU / 4
        aEnd = (i * 1.0 + map(sin(frameCount / 20.0),-1,1,0,0.5)) /l * TAU / 2.0 + TAU / 4
        bStart = map(frameCount  + (i * 1.0) / l * 100,0,100, 0,TAU) + map(sin(frameCount / 20.0),-1,1,0,TAU)
        bEnd = map((frameCount  + (i * 1.0) / l * 100),0,100,0,TAU)  
        pork.update(r1,r2,500,500,aStart,aEnd,bStart,bEnd)
        pork.display(type)

    pop()
