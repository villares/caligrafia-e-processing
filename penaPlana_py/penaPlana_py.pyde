# Mariana Leal originalmente em Java,
# Alexandre Villares portou para Python

larguraPena = 40
x, y = 0, 0

def setup():
    size(600, 500)
    smooth()
    background(255)
    # stroke(0)
    # fill(0)
    rectMode(CENTER)
    for i in range(0, height, 5 * larguraPena):
        stroke(200)
        line(0, i, width, i)

def draw():
    global x, y
    # aqui que acontece o easing
    noStroke()
    miraX = mouseX
    miraY = mouseY
    x = lerp(x, miraX, 0.1)
    y = lerp(y, miraY, 0.1)
    if mousePressed:
        fill(x, x / y, y, 50)
        translate(x, y)
        rotate(5 * PI / 6)
        rect(0, 0, larguraPena, 3, 4, 4, 4, 4)
