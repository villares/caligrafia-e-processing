# Mariana Leal originalmente em Java,
# Alexandre Villares portou para Python

add_library('Tablet')

x = y = px = py = 0
strokeColor = 10

def setup():
    global tablet
    size(800, 800)
    background(255)
    # noFill()
    noStroke()
    colorMode(HSB, 359)
    strokeCap(ROUND)
    tablet = Tablet(this)

def draw ():
    global x, y, px, py, strokeColor
    miraX = mouseX
    miraY = mouseY
    # x = pmouseX
    # y = pmouseY
    x = lerp(x, miraX, 0.1)
    y = lerp(y, miraY, 0.1)
    if mousePressed:
        stroke(strokeColor, 356, 300)
        strokeWeight(tablet.getPressure() * 40)
        line(x, y, px, py)
        px = x
        py = y
    
    strokeColor += 1
    if strokeColor >= 359: strokeColor = 10

def keyPressed() :
    background(0, 0, 359)
