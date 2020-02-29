gestos = [] # lista de gestos
gesto = []  # lista de pontos, tuplas (x, y)
select_gesto = -1 # -1 significa nenhum gesto selecionado

def setup():
    size(500, 500)
    # noStroke()
    fill(100, 200)
    frameRate(10)
    smooth(8)
    
def draw():
    # scale(1.5, 1.5)
    background(200)
    for i, gesto in enumerate(gestos):    
        largura = 30
        dx, dy = 0.87 * largura, -0.5 * largura
        beginShape()
        for i, pi in enumerate(gesto):
            vertex(pi.x + dx, pi.y + dy)
            # text(str(i), pi.x + dx, pi.y + dy)
        for pv in reversed(gesto):
            vertex(pv.x - dx, pv.y - dy)
        endShape(CLOSE)
        
def mousePressed():
    global select_gesto
    if keyPressed and keyCode == SHIFT:
        for i, gesto in enumerate(gestos):
            for p in gesto:
                if dist(p.x, p.y, mouseX, mouseY) < 10:
                    select_gesto = i
                    return
        select_gesto = -1 # deixa nenhum gesto selecionado
    
def mouseDragged():
    if not keyPressed:
        # if frameCount % 2 == 0:
            gesto.append(PVector(mouseX, mouseY))
    if key == 'm':
        if select_gesto >= 0:
            dx = mouseX - pmouseX
            dy = mouseY - pmouseY
            sel_gesto = gestos[select_gesto]
            for p in enumerate(sel_gesto):
                sel_gesto[i] = PVector(p.x + dx, p.y + dy)
                
    
def mouseReleased():
    novo_gesto = gesto[:] # cria uma cópia
    gestos.append(novo_gesto)
    gesto[:] = [] # esvazia a lista gesto original
    
def keyPressed():
    global select_gesto
    if key == 's':
        saveFrame("####.png")
    if key == ' ':
        gestos[:] = [] # esvazia a lista gestos 
          
    if key == 'r' and select_gesto >= 0:
        gestos.pop(select_gesto)
        select_gesto = -1
        
    if key == 'd' and select_gesto >= 0:
        new_gesto = gestos[select_gesto][:]
        for i, (x, y) in enumerate(new_gesto):
            new_gesto[i] = (x + 20, y + 20)
        gestos.append(new_gesto)
        select_gesto = len(gestos) - 1
        
    if key == 'z' and len(gestos) > 0:
        gestos.pop() # apaga o último gesto
    
    if key == 'l':
        for gesto in gestos:
            for i, p in enumerate(gesto[1:-1]):
                pa = gesto[1 + i - 1]
                gesto[1 + i] = PVector((p.x + pa.x) / 2,(p.y + pa.y) / 2)
    
