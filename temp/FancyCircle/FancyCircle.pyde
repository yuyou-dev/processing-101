colors = [color(13,127,190),color(245,10,10),color(251,228,20),color(255,255,255)]
def setup():
    size(500,500)
    background(255)

    noFill()
    stroke(0)
    strokeWeight(10)

    smooth(4)
def draw():
    global colors
    background(255)
    translate(width / 2.0,height / 2.0)
    
    for i in range(0,5):
        r = i * 50
        dir = map(i % 2,0,1,-1,1)
        start1 = map(millis() * dir + r * 7,0,2000,0,TAU)
        end1 = start1 + map(sin(millis()  / 500.0),-1,1,0.1,TAU / 2.6)
        
        
        start2 = start1 + TAU / 2
        end2 = end1 + TAU / 2
        
        
        stroke(0)
        strokeWeight(14)

        arc(0,0,r,r,start1,end1)
        arc(0,0,r,r,start2,end2)
        stroke(colors[i % 4])
        strokeWeight(10)
        arc(0,0,r,r,start1,end1)
        
        stroke(colors[(i + 3) % 4])
        arc(0,0,r,r,start2,end2)
