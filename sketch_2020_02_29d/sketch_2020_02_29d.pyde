from __future__ import division

gestos = []  # lista de gestos
gesto = []  # lista de pontos, tuplas (x, y)
select_gesto = -1  # -1 significa nenhum gesto selecionado

def setup():
    size(500, 500)
    pixelDensity(2)
    fill(0)
    smooth(8)
    # noSmooth()


def draw():
    largura = 30
    dx, dy = 0.87 * largura, -0.5 * largura

    if not mousePressed:
        background(200)
    else:
        xi, yi = pmouseX, pmouseY
        xf, yf = mouseX, mouseY
        quad(xi + dx, yi + dy, xi - dx, yi - dy,
             xf - dx, yf - dy, xf + dx, yf + dy)

    for i, gesto in enumerate(gestos):
        for (xi, yi), (xf, yf) in zip(gesto[:-1], gesto[1:]):
            quad(xi + dx, yi + dy, xi - dx, yi - dy,
                 xf - dx, yf - dy, xf + dx, yf + dy)

def mousePressed():
    global select_gesto
    if keyPressed and keyCode == SHIFT:
        for i, gesto in enumerate(gestos):
            for x, y in gesto:
                if dist(x, y, mouseX, mouseY) < 10:
                    select_gesto = i
                    return
        select_gesto = -1  # deixa nenhum gesto selecionado

def mouseDragged():
    if not keyPressed:
        # if frameCount % 2 == 0:
            gesto.append((mouseX, mouseY))
    if key == 'm':
        if select_gesto >= 0:
            dx = mouseX - pmouseX
            dy = mouseY - pmouseY
            sel_gesto = gestos[select_gesto]
            for i, (x, y) in enumerate(sel_gesto):
                sel_gesto[i] = (x + dx, y + dy)


def mouseReleased():
    for _ in range(4):
        for i, (x, y) in enumerate(gesto[:-2]):
            xs, ys = gesto[i + 1]
            xm, ym = (x + xs) / 2., (y + ys) / 2.
            gesto[i + 1] = (xm, ym)
    novo_gesto = gesto[:]  # cria uma cópia
    gestos.append(novo_gesto)
    gesto[:] = []  # esvazia a lista gesto original

def keyPressed():
    global select_gesto
    if key == 's':
        saveFrame("####.png")
    if key == ' ':
        gestos[:] = []  # esvazia a lista gestos

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
        gestos.pop()  # apaga o último gesto

    if key == 'l':
        for gesto in gestos:
            for i, (x, y) in enumerate(gesto[:-2]):
                xs, ys = gesto[i + 1]
                xm, ym = (x + xs) / 2., (y + ys) / 2.
                gesto[i + 1] = (xm, ym)
