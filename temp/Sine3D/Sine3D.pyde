from math import *
def normalDistribution(x):
    y = 1.0 / sqrt(TAU) * exp(- x * x / 2.0)
    return y
def setup():
    size(500,500,P3D)
    background(200)
    
    push()
    translate(width / 2,height / 2)
    box(30)
    pop()
    
    translate(0,height / 2.0)
    xRange = 1333
    r = 50
    times = 25
    dy = map(times,0,50,-99,99)
    dx = sqrt(100 * 100 - dy * dy)
    r = dx * 2.0
    scale = map(100 - abs(dy),0,100,0,1)
    dy = dy * 1.6
    beginShape()
    for i in range(0,width,1):
        x = map(i,0,width,-xRange,xRange)
        v = normalDistribution(x * 1.0/ r) * map(r,0,100,0,50)
        v2 = normalDistribution(dy * 1.0 / r * 8.0) * 1
        y = sin(i / (2.0 + noise(times) * 2))
        y = y * v * scale * v2
        vertex(i,y + dy)
        #vertex(i,height)
    endShape()
    
