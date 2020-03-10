from __future__ import division

gestos = []  # lista de gestos
gesto = []  # lista de pontos, tuplas (x, y)
gesto_selecionado = -1  # -1 significa nenhum gesto selecionado

x = 0
y = 0

xi = 0
yi = 0

xf = 0
yf = 0

def setup():
    size(1200, 600)
    pixelDensity(1)
    fill(0)
    smooth(8)
    # noSmooth()
    #strokeCap(ROUND)
    #strokeWeight(1)
    #noStroke()

def draw():
    largura = 20
    dx, dy = 0.87 * largura, -0.5 * largura

    if not mousePressed or keyPressed:
        background(200)
    else:
        #aqui que tentei aplicar o easing
        global xi, yi, xf, yf
        xi, yi = mouseX, mouseY
        xf, yf = pmouseX, pmouseY
        # strokeWeight(4)
        # xi = lerp(xi, mouseX, 0.1)
        # yi = lerp(yi, mouseY, 0.1)
        # line(xi - 15, yi + 15 , xi + 15, yi -15)
        quad(xi + dx, yi + dy, 
                 xi - dx, yi - dy,
                 xf - dx, yf - dy, 
                 xf + dx, yf + dy)
    for i, gesto in enumerate(gestos):
        #recupera o traço do gesto em cada frame
        #noFill()
        for (xi, yi), (xf, yf) in zip(gesto[:-1], gesto[1:]):
            noStroke()
            quad(xi + dx, yi + dy, 
                 xi - dx, yi - dy,
                 xf - dx, yf - dy, 
                 xf + dx, yf + dy)

def mousePressed():
    global gesto_selecionado
    if keyPressed and keyCode == SHIFT:
        for i, gesto in enumerate(gestos):
            for x, y in gesto:
                #não entendo como a relação entre a distância entre o mouse e o ponto determinando qual será o índice escolhido.
                if dist(x, y, mouseX, mouseY) < 10:
                    gesto_selecionado = i
                    return
        gesto_selecionado = -1  # deixa nenhum gesto selecionado

def mouseDragged():
    #easing aqui
    if not keyPressed:
        #if frameCount % 2 == 0:
            global x, y
            x = lerp(x, mouseX, 0.1)
            y = lerp(y, mouseY, 0.1)
            gesto.append((x, y))
    #para mover o gesto selecionado 
    elif key == 'm':
        if gesto_selecionado >= 0:
            dx = mouseX - pmouseX
            dy = mouseY - pmouseY
            sel_gesto = gestos[gesto_selecionado]
            for i, (x, y) in enumerate(sel_gesto): #mas aqui devolve uma tupla tbm? pq a coordenada entre parênteses
                #o dx e dy é o que faz o selecionado se mover
                sel_gesto[i] = (x + dx, y + dy)


def mouseReleased():
    #dá uma garibada nas coordenadas do gesto recém-terminado
    #guarda as coordenadas do gesto na lista gestos
    nivel_ajuste = 15
    for _ in range(nivel_ajuste):
        for i, (x, y) in enumerate(gesto[:-2]):
            xs, ys = gesto[i + 1]
            xm, ym = (x + xs) / 2., (y + ys) / 2.
            gesto[i + 1] = (xm, ym)
    #esquema para guardar o gesto na lista de gestos e apagá-lo em seguida
    novo_gesto = gesto[:]  # cria uma cópia
    gestos.append(novo_gesto)
    gesto[:] = []  # esvazia a lista de gesto original

def keyPressed():
    global gesto_selecionado
    if key == 's':
        saveFrame("####.png")
    if key == ' ':
        gestos[:] = []  # esvazia a lista de gestos
        
    #para apagar o gesto selecionado
    if key == 'r' and gesto_selecionado >= 0:
        gestos.pop(gesto_selecionado)
        gesto_selecionado = -1
        
    #copia o gesto e o coloca no último posto da lista de gestos
    if key == 'd' and gesto_selecionado >= 0:
        new_gesto = gestos[gesto_selecionado][:]
        for i, (x, y) in enumerate(new_gesto):
            new_gesto[i] = (x + 20, y + 20)
        gestos.append(new_gesto)
        gesto_selecionado = len(gestos) - 1

    if key == 'z' and len(gestos) > 0:
        gestos.pop()  # apaga o último gesto
    
    #faz as médias das coordenadas do traço e recoloca essa média na coordenada sequinte
    if key == 'l':
        for gesto in gestos:
            for i, (x, y) in enumerate(gesto[:-2]):
                xs, ys = gesto[i + 1]
                xm, ym = (x + xs) / 2., (y + ys) / 2.
                gesto[i + 1] = (xm, ym)
