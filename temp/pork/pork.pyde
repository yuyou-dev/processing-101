from math import *
import random
from Modules import *
from Mondrian3d import *

s = 0
v = 10
a = 0
root = None

def setup():
    global root
    size(1000,1000,P3D)
    smooth(8)
    maxBox = VisualBox(VisualPoint(-200,-200,-200),VisualPoint(200,200,200))
    root = Divider('full',VisualBox(VisualPoint(0,0,0),VisualPoint(1,1,1)),maxBox)
    root.divideNext()
    
def draw():
    global s,v,a,root
    a = -s / 100.0
    v = v + a
    s = s + v

    background(255)
    push()
    translate(500,500)
    translate(0,0,-1000)
    rotateX(frameCount / 500.0 * TAU)
    rotateY(frameCount / 200.0 * TAU)
    fill(255,255,0)
    
    
    fill(255)
    strokeWeight(5)
    b = root.displayAll()
    pop()
    
    
