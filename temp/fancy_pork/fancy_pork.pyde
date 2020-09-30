add_library('sound')
from math import *
import random
from Modules import *

pork0 = None
porkGroup = []
audio = None
amp = None
waveform = None
fft = None
samples = 200
sum = []
current = []
colors = []
barWidth = None
def setup():
    global audio,amp,waveform,samples,fft,sum,barWidth,colors
    
    size(1000,1000,P3D)
    smooth(8)
    global porkGroup,pork0
    r1 = 300
    r2 = 400
    x = width / 2
    y = height / 2
    aStart = 0
    aEnd = TAU / 4
    bStart = 0
    bEnd = TAU / 16
    for i in range(24):
        pork = Pork(r1,r2,x,y,aStart,aEnd,bStart,bEnd)
        porkGroup.append(pork)
        
    file = SoundFile(this,'audio1.mp3')
    file.play()
    bands = 512
    fft = FFT(this, bands)
    fft.input(file);
    barWidth = width * 1.0/64;
    for i in range(64):
        colors.append(getColor())
        sum.append(0.0)
        current.append(0.0)
def getColor():
    colors = [color(13,127,190),color(245,10,10),color(251,228,20),color(255,255,255)]
    return colors[random.randint(0,3)]
def draw():
    background(255)
    global amp,audio,waveform,samples,fft,sum,barWidth,colors
    fft.analyze()
    fill(color(13,127,190))
    translate(0,0)
    strokeWeight(3)
    for i in range(64):
        sum[i] = 0.0
        sum[i] = sum[i] + (fft.spectrum[i] - sum[i]) * 0.2
        
        if current[i] > sum[i]:
            c = (current[i] - sum[i]) * 0.05
            current[i] = current[i] - c
        else:
            current[i] = sum[i]
            
        if i < 24:
            showPork(i,current[i])
        fill(colors[i],map(current[i]*height*3,0,50,0,255))
        rect(i*barWidth, height, barWidth, map(-current[i]*height*3,0,100,-100,50))
        rect(i*barWidth, 0, barWidth, -map(-current[i]*height*3,0,100,-100,50))
def showPork(i,val):
    global porkGroup
    pork = porkGroup[i]
    if i < 12:
        push()
        translate(500,500)
        translate(0,0,-1000)
        rotateY(frameCount / 300.0)
        #rotateY(TAU / 4)
        rotateX(TAU / 4)
        rotateX(frameCount / 450.0)
        l = 12
        
        r1 = map(val,0,0.05,450,470)
        r2 = 450
        bEnd = (i * 1.0 ) /l * TAU / 2.0 + TAU / 4
        bStart = (i * 1.0 +1) /l * TAU / 2.0 + TAU / 4
        aStart = -map(val,0,0.05,0,TAU / 2)  + i * 1.0 / l * TAU 
        aEnd = map(val,0,0.05,0,TAU / 2)  + i * 1.0 / l * TAU 
        type = '3'   
        pork.update(r1,r2,500,500,aStart,aEnd,bStart,bEnd)
        pork.display(type)
        pop()
    else:
        push()
        translate(500,500)
        translate(0,0,-1000)
        rotateY(frameCount / 300.0)
        rotateX(frameCount / 250.0)
        l = 12
        r1 = map(sin(frameCount / 30.0),-1,1,0,325)
        r2 = 330
        
        ii = i - 12
        
        aStart = ii * 1.0 / l * TAU / 2.0 + TAU / 4
        aEnd = (ii * 1.0 + map(sin(frameCount / 20.0),-1,1,0,1)) /l * TAU / 2.0 + TAU / 4
        bStart = map(frameCount  + (ii * 1.0) / l * 100,0,100, 0,TAU) + map(sin(frameCount / 20.0),-1,1,0,TAU)
        bEnd = map((frameCount  + (ii * 1.0) / l * 100),0,100,0,TAU)  
        type = '1'   
        pork.update(r1,r2,500,500,aStart,aEnd,bStart,bEnd)
        pork.display(type)
        pop()
