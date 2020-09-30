from math import *
import random
from Modules import *

t2 = None
def setup():
    global t2
    size(1000,1000,P3D)
    background(255)
    smooth(8)
    t = Triangle()
    t.make(100)
    translate(width / 2,height / 2)
    t.display()

    t2 = Tetrahedron()
    t2.make(300)
    t2.divide(3)
    
def draw():
    global t2
    background(255)
    translate(width / 2,height / 2,-1000)
    rotateX(frameCount / 1000.0 * TAU)
    rotateY(frameCount / 1000.0 * TAU)
    #t2.display()
    t2.displayAll()
