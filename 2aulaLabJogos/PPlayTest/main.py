__author__ = 'Anselmo'

# importei os módulos necessários do PPlay
from PPlay.window import *
from PPlay.keyboard import *
from PPlay.gameimage import *
from PPlay.sprite import *
from random import *

# criar um janela de 512x512 pixels
janela = Window(512, 512)

# criar um teclado para interagir com o jogo
teclado = Keyboard()

# criar o fundo do cenário
fundo = GameImage("gtabg.png")

# posicionar o centro do mapa no centro da janela
# fundoPosX = -(fundo.width/2 - janela.width/2)
# fundoPosY = -(fundo.height/2 - janela.height/2)

fundoPosX = 0
fundoPosY = 0

# posicionar o centro do janela no centro do mapa
janelaPosX = 0  # fundo.width/2 - janela.width/2
janelaPosY = 0  # fundo.height/2 - janela.height/2


# Converte coordenadas do mundo para tela
def MapaParaTela(xm, ym, janelaPosX, janelaPox):
    xt = xm - janelaPosX
    yt = ym - janelaPosY
    # para de coordenadas da janela retornados
    return xt, yt


# criar sprite
ufo = Sprite("heli.png",3)
ufo.set_total_duration(300)

# mover o sprite para a posição (ufoPosX,ufoPosY)
# ufo.move_x(ufoPosX)
# ufo.move_y(ufoPosY)

# criar nuvem de dengue

nuvemDengue = Sprite("nuvemdengue.png", 1)
nuvemDengue.xm = randint(0, 2048)
nuvemDengue.ym = randint(0, 2048)


def virarLegal(desejada, antiga):
    if desejada > antiga:
        antiga += 1
        ufo.rotate(antiga)
    if desejada < antiga:
        antiga -= 1
        ufo.rotate(antiga)
    return antiga


desejada = 0
# Game Loop
while True:
    ufo.update()
    ufo.draw()
    # Limpar a tela com cor negra
    janela.set_background_color((0, 0, 0))

    # Tratar a entrada do tecla
    if (teclado.key_pressed("UP")):
        # fundoPosY +=1
        janelaPosY -= 1
        desejada = virarLegal(0, desejada)
    elif (teclado.key_pressed("DOWN")):
        # fundoPosY -=1
        janelaPosY += 1
        desejada = virarLegal(180, desejada)
    if (teclado.key_pressed("LEFT")):
        janelaPosX -= 1
        # fundoPosX +=1
        desejada = virarLegal(90, desejada)
    elif (teclado.key_pressed("RIGHT")):
        janelaPosX += 1
        # fundoPosX -=1
        desejada = virarLegal(270, desejada)

    # checar os limites
    if janelaPosX <= -janela.width / 2:
        janelaPosX = -janela.width / 2
    elif janelaPosX >= fundo.width - janela.width / 2:
        janelaPosX = fundo.width - janela.width / 2

    if janelaPosY <= -janela.height / 2:
        janelaPosY = -janela.height / 2
    elif janelaPosY >= fundo.height - janela.height / 2:
        janelaPosY = fundo.height - janela.height / 2

    # print(fundoPosX,fundoPosY)

    # atualização do fundo
    xt, yt = MapaParaTela(fundoPosX, fundoPosY, janelaPosX, janelaPosY)
    fundo.set_position(xt, yt)
    fundo.draw()

    # desenhar o ufo

    xt, yt = MapaParaTela(nuvemDengue.xm, nuvemDengue.ym, janelaPosX, janelaPosY)
    nuvemDengue.set_position(xt, yt)
    nuvemDengue.draw()

    # incializar a posição do sprite no centro da tela
    ufoPosX = janelaPosX + janela.width / 2 - ufo.width / 2
    ufoPosY = janelaPosY + janela.height / 2 - ufo.height / 2
    xt, yt = MapaParaTela(ufoPosX, ufoPosY, janelaPosX, janelaPosY)
    ufo.set_position(xt, yt)
    ufo.draw()

    janela.update()

# continuar = True
# i = 1
# while continuar:
#     print("Esta é soma de ordem:",i)
#     x = int(input("Digite o primeiro numero:"))
#     y = int(input("Digite o segundo numero:"))
#     print("A soma e ",x+y)
#     resposta = input("Deseja continuar com a soma (s/n)")
#     if (resposta == "s"):
#         i = i + 1
#     else:
#         continuar = False
