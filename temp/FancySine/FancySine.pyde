from math import *
import random
def setup():
    size(500,500,P3D)
    background(200)
    translate(0,height / 2)
    for x in range(60,width - 60,5):
        y = sin(x / 20.0) * 30
        circle(x,y,5)
