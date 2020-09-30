add_library('sound')
from math import *
import random
from Modules import *
from MotionRect import *

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
fBox = None

def setup():
    global audio,amp,waveform,samples,fft,sum,barWidth,colors,fBox
    
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
    for i in range(8):
        pork = Pork(r1,r2,x,y,aStart,aEnd,bStart,bEnd)
        porkGroup.append(pork)
        
    file = SoundFile(this,'audio1.mp3')
    file.play()
    bands = 512
    fft = FFT(this, bands)
    fft.input(file);
    barWidth = width * 1.0/128;
    for i in range(128):
        colors.append(getColor())
        sum.append(0.0)
        current.append(0.0)
    fBox = FancyBox()
    fBox.create()
def getColor():
    colors = [color(13,127,190),color(245,10,10),color(251,228,20),color(255,255,255)]
    return colors[random.randint(0,3)]
def draw():
    print(millis())
    background(255)
    global amp,audio,waveform,samples,fft,sum,barWidth,colors,fBox
    
    fft.analyze()
    fill(color(13,127,190))
    push()
    
    strokeWeight(3)
    for i in range(128):
        sum[i] = 0.0
        sum[i] = sum[i] + (fft.spectrum[i] - sum[i]) * 0.2
        
        if current[i] > sum[i]:
            c = (current[i] - sum[i]) * 0.05
            current[i] = current[i] - c
        else:
            current[i] = sum[i]
            
        if i < 8:
            showPork(i,current[i])
        fill(colors[i],map(current[i]*height*3,0,50,0,255))
        rect(i*barWidth, height, barWidth, map(-current[i]*height*3,0,100,-100,50))
        rect(i*barWidth, 0, barWidth, -map(-current[i]*height*3,0,100,-100,50))
    pop()
    push()
    translate(-400,0)
    
    fBox.display(current)
    pop()
def showPork(i,val):
    global porkGroup
    pork = porkGroup[i]
    fc = millis() / 35
    
    
    
    push()
    translate(400,0)
    translate(500,500)
    translate(0,0,-1000)
    rotateY(fc / 300.0)
    rotateX(fc / 250.0)
    if millis() % 105000 < 700 * 20:
        style1(i,pork)
    elif millis() % 105000  < 700 * 40:
        style2(i,pork)
    elif millis() % 105000  < 700 * 80:
        style3(i,pork)
    elif millis() % 105000  < 700 * 110:
        style4(i,pork)
    elif millis() % 105000  < 700 * 150:
        style3(i,pork)
    pop()
def style1(i,pork):
    fc = millis() / 35
    l = 8
    #r1 = map(sin(fc / 30.0),-1,1,0,325)
    r1 = 0
    r2 = 300
    bStart = i * 1.0 / l * TAU / 2.0 + TAU / 4
    bEnd = (i * 1.0 + map(sin(fc / 20.0),-1,1,0,1)) /l * TAU / 2.0 + TAU / 4
    aStart = map(fc  + (i * 1.0) / l * 100,0,100, 0,TAU) + map(sin(fc / 20.0),-1,1,0,TAU)
    aEnd = map((fc  + (i * 1.0) / l * 100),0,100,0,TAU)  
    type = '3'   
    pork.update(r1,r2,500,500,aStart,aEnd,bStart,bEnd)
    pork.display(type)
def style2(i,pork):
    fc = millis() / 35
    l = 8
    r1 = map(sin(fc / 30.0),-1,1,0,290)
    #r1 = 0
    r2 = 300
    bStart = i * 1.0 / l * TAU / 2.0 + TAU / 4
    bEnd = (i * 1.0 + map(sin(fc / 20.0),-1,1,0,1)) /l * TAU / 2.0 + TAU / 4
    aStart = map(fc  + (i * 1.0) / l * 100,0,100, 0,TAU) + map(sin(fc / 20.0),-1,1,0,TAU)
    aEnd = map((fc  + (i * 1.0) / l * 100),0,100,0,TAU)  
    type = '1'   
    pork.update(r1,r2,500,500,aStart,aEnd,bStart,bEnd)
    pork.display(type)
def style3(i,pork):
    fc = millis() / 35
    l = 8
    r1 = map(sin(fc / 30.0),-1,1,0,290)
    r1 = 0
    r2 = 300
    aStart = i * 1.0 / l * TAU / 2.0 + TAU / 4
    aEnd = (i * 1.0 + map(sin(fc / 20.0),-1,1,0,1)) /l * TAU / 2.0 + TAU / 4
    bStart = map(fc  + (i * 1.0) / l * 100,0,100, 0,TAU) + map(sin(fc / 20.0),-1,1,0,TAU)
    bEnd = map((fc  + (i * 1.0) / l * 100),0,100,0,TAU)  
    type = '1'   
    pork.update(r1,r2,500,500,aStart,aEnd,bStart,bEnd)
    pork.display(type)
def style4(i,pork):
    fc = millis() / 35
    l = 8
    r1 = map(sin(fc / 30.0),-1,1,0,290)
    r1 = 0
    r2 = 300
    aStart = i * 1.0 / l * TAU / 2.0 + TAU / 4
    aEnd = (i * 1.0 + map(sin(fc / 20.0),-1,1,0,1)) /l * TAU / 2.0 + TAU / 4
    bStart = map(fc  + (i * 1.0) / l * 100,0,100, 0,TAU) + map(sin(fc / 20.0),-1,1,0,TAU)
    bEnd = map((fc  + (i * 1.0) / l * 100),0,100,0,TAU)  
    type = '2'   
    pork.update(r1,r2,500,500,aStart,aEnd,bStart,bEnd)
    pork.display(type)
def style5(i,pork):
    fc = millis() / 35
    l = 8
    r1 = map(sin(fc / 30.0),-1,1,0,290)
    #r1 = 0
    r2 = 300
    aStart = i * 1.0 / l * TAU / 2.0 + TAU / 4
    aEnd = (i * 1.0 + map(sin(fc / 20.0),-1,1,0,1)) /l * TAU / 2.0 + TAU / 4
    bStart = map(fc  + (i * 1.0) / l * 100,0,100, 0,TAU) + map(sin(fc / 20.0),-1,1,0,TAU)
    bEnd = map((fc  + (i * 1.0) / l * 100),0,100,0,TAU)  
    type = '3'   
    pork.update(r1,r2,500,500,aStart,aEnd,bStart,bEnd)
    pork.display(type)
