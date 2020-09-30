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
    strokeWeight(5)
    background(255)
    push()
    translate(500,500,-1000)
    rotateX(angle)
    rotateY(angle)
    
    fill(255,255,255,255)
    
    push()
    rotateX(angle * 10)
    rotateY(angle * 5)
    fill(map(sin(frameCount / 120.0 * TAU),-1,1,0,255),map(cos(frameCount / 120.0 * TAU),-1,1,0,255),map(sin(frameCount / 120.0 * TAU),-1,1,255,0))
    box(map(sin(frameCount / 100.0 * TAU),-1,1,100,200))
    pop()
    push()
    translate(-width / 2,-width / 2,200)
    m1.display()
    pop()
    
    push()
    rotateX(TAU / 2)
    translate(-width / 2,-width / 2,200)
    m2.display()
    pop()
    
    push()
    rotateX(TAU / 2)
    rotateY(TAU / 4)
    translate(-width / 2,-width / 2,200)
    m3.display()
    pop()
    
    push()
    rotateX(TAU / 2)
    rotateY(TAU / 4 + TAU / 2)
    translate(-width / 2,-width / 2,200)
    m4.display()
    pop()
    
    push()
    rotateX(TAU / 4)
    translate(-width / 2,-width / 2,200)
    m5.display()
    pop()
    
    push()
    rotateX(TAU / 4 + TAU / 2)
    translate(-width / 2,-width / 2,200)
    m6.display()
    pop()
    
    pop()
    
