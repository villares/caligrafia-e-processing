from __future__ import division

gestos = []  # lista de gestos
gesto = []  # lista de pontos, tuplas (x, y)
gesto_selecionado = -1  # -1 significa nenhum gesto selecionado
ecavalou = False

def setup():
    size(500, 500)
    pixelDensity(2)
    fill(0)
    smooth(8)
    # noSmooth()


def draw():
    largura = 30
    dx, dy = 0.87 * largura, -0.5 * largura

    if not mousePressed or keyPressed:
        background(200)
    else:
        xi, yi = pmouseX, pmouseY
        xf, yf = mouseX, mouseY
        quad(xi + dx, yi + dy, xi - dx, yi - dy,
             xf - dx, yf - dy, xf + dx, yf + dy)
    for i, gesto in enumerate(gestos):
        if i == gesto_selecionado:
            stroke(200, 0, 0)
        else:
            stroke(0)
        for (xi, yi), (xf, yf) in zip(gesto[:-1], gesto[1:]):
            quad(xi + dx, yi + dy, xi - dx, yi - dy,
                 xf - dx, yf - dy, xf + dx, yf + dy)

def mousePressed():
    global gesto_selecionado
    if keyPressed and keyCode == SHIFT:
        for i, gesto in enumerate(gestos):
            for x, y in gesto:
                if dist(x, y, mouseX, mouseY) < 10:
                    gesto_selecionado = i
                    return
        gesto_selecionado = -1  # deixa nenhum gesto selecionado

def mouseDragged():
    if not keyPressed:
        if dist(mouseX, mouseY, pmouseX, pmouseY) > 2:
            gesto.append((mouseX, mouseY))
            encavalou = False
        else:
            encavalou = True
    elif key == 'm':
        if gesto_selecionado >= 0:
            dx = mouseX - pmouseX
            dy = mouseY - pmouseY
            sel_gesto = gestos[gesto_selecionado]
            for i, (x, y) in enumerate(sel_gesto):
                sel_gesto[i] = (x + dx, y + dy)


def mouseReleased():
    global encavalou
    if encavalou:
        gesto.append((mouseX, mouseY))
        ecavalou = False
    nivel_ajuste = 4
    for _ in range(nivel_ajuste):
        for i, (x, y) in enumerate(gesto[:-2]):
            xs, ys = gesto[i + 1]
            xm, ym = (x + xs) / 2., (y + ys) / 2.
            gesto[i + 1] = (xm, ym)
    novo_gesto = gesto[:]  # cria uma cópia
    gestos.append(novo_gesto)
    gesto[:] = []  # esvazia a lista gesto original

def keyPressed():
    global gesto_selecionado
    if key == 's':
        saveFrame("####.png")
    if key == ' ':
        gestos[:] = []  # esvazia a lista gestos

    if key == 'r' and gesto_selecionado >= 0:
        gestos.pop(gesto_selecionado)
        gesto_selecionado = -1

    if key == 'd' and gesto_selecionado >= 0:
        new_gesto = gestos[gesto_selecionado][:]
        for i, (x, y) in enumerate(new_gesto):
            new_gesto[i] = (x + 20, y + 20)
        gestos.append(new_gesto)
        gesto_selecionado = len(gestos) - 1

    if key == 'z' and len(gestos) > 0:
        gestos.pop()  # apaga o último gesto

    if key == 'l':
        for gesto in gestos:
            for i, (x, y) in enumerate(gesto[:-2]):
                xs, ys = gesto[i + 1]
                xm, ym = (x + xs) / 2., (y + ys) / 2.
                gesto[i + 1] = (xm, ym)
