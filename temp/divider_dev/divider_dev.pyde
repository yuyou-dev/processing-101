from math import *
import random
from MotionRect import *

def setup():
    global m1,m2,m3,m4,m5,m6
    size(1000,1000,P3D)
    rectMode(CORNERS)
    m1 = RectManager(Divider('full',2,0.5,0.5))
    m1.createDivider(MotionRect(Vec2d(300,300),Vec2d(700,700)))
    
    m2 = RectManager(Divider('full',2,0.5,0.5))
    m2.createDivider(MotionRect(Vec2d(300,300),Vec2d(700,700)))
    
    m3 = RectManager(Divider('full',2,0.5,0.5))
    m3.createDivider(MotionRect(Vec2d(300,300),Vec2d(700,700)))

    m4 = RectManager(Divider('full',2,0.5,0.5))
    m4.createDivider(MotionRect(Vec2d(300,300),Vec2d(700,700)))
    
    m5 = RectManager(Divider('full',2,0.5,0.5))
    m5.createDivider(MotionRect(Vec2d(300,300),Vec2d(700,700)))
    
    m6 = RectManager(Divider('full',2,0.5,0.5))
    m6.createDivider(MotionRect(Vec2d(300,300),Vec2d(700,700)))
def draw():
    angle = frameCount % 800 / 800.0 * TAU
    c = color(255,0,0)
    strokeWeight(5)
    line(0,0,1000,1000)
    background(200)
    
    push()
    translate(0,0,0)
    rotateX(angle)
    
    push()
    translate(0,0,200)
    m1.display()
    pop()
    
    push()
    rotateX(TAU / 2.0)
    translate(0,-1000,200)
    m2.display()
    pop()
    
    push()
    rotateX(TAU / 4.0)
    translate(0,-500,-500 + 200)
    m3.display()
    pop()
    
    push()
    rotateX(TAU / 4.0 - TAU / 2.0)
    translate(0,-500,500 + 200)
    m4.display()
    pop()
    
    push()
    rotateY(TAU / 4.0)
    translate(-500,0,500 + 200)
    m5.display()
    pop()
    
    push()
    rotateY(TAU / 4.0 - TAU / 2.0)
    translate(-500,0,-500 + 200)
    m6.display()
    pop()
    
    pop()
