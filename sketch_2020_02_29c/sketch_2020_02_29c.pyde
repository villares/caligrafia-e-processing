gestos = [] # lista de gestos
gesto = []  # lista de pontos, tuplas (x, y)

def setup():
    size(500, 500)
    # noStroke()
    fill(100, 200)
    frameRate(10)
    
def draw():
    scale(1.5, 1.5)
    background(200)
    for gesto in gestos:
        largura = 30
        dx, dy = 0.87 * largura, -0.5 * largura
        beginShape()
        for x, y in gesto:
            vertex(x + dx, y + dy)
        for x, y in reversed(gesto):  # testar [::2]
            vertex(x - dx, y - dy)
        endShape(CLOSE)
           
def mouseDragged():
    gesto.append((mouseX, mouseY))            
    
def mouseReleased():
    # for _ in range(20):
    #     for i, (x, y) in enumerate(gesto[2:-2]):
    #         xa, ya = gesto[1 + i - 1]
    #         gesto[1 + i] = ((x + xa) / 2, (y + ya) / 2)
    novo_gesto = gesto[:] # cria uma cópia
    gestos.append(novo_gesto)
    gesto[:] = [] # esvazia a lista gesto original
    
def keyPressed():
    if key == 's':
        saveFrame("####.png")
    if key == ' ':
        gestos[:] = [] # esvazia a lista gestos 
    if key == 'z' and len(gestos) > 0:
        gestos.pop() # apaga o último gesto
    
    if key == 'l':
        for _ in range(1):
          for gesto in gestos:
            for i, (x, y) in enumerate(gesto[1:-2]):
                xa, ya = gesto[1 + i - 1]
                gesto[1 + i] = ((x + xa) / 2, (y + ya) / 2)
        
