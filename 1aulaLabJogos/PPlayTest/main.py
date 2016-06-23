__author__ = 'Anselmo'

# importei os módulos necessários do PPlay
from PPlay.window import *
from PPlay.keyboard import *
from PPlay.gameimage import *
from PPlay.sprite import *
from random import *
from PPlay.collision import *

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
ufo = Sprite("ufo.png", 1)

# mover o sprite para a posição (ufoPosX,ufoPosY)
# ufo.move_x(ufoPosX)
# ufo.move_y(ufoPosY)

# criar nuvem de dengue

nuvemDengue = Sprite("nuvemdengue.png", 1)
nuvemDengue.xm = randint(0, 2048)
nuvemDengue.ym = randint(0, 2048)

# eu criei
matrix = [[randint(0, 2048), randint(0, 2048)] for x in range(32)]

for i in range(len(matrix) - 1):
    nuvemDengue.set_position(matrix[i][0], matrix[i][1])
    nuvemDengue.draw()
# parei de criar


# Game Loop
while True:
    # Limpar a tela com cor negra
    janela.set_background_color((0, 0, 0))

    # Tratar a entrada do tecla
    if (teclado.key_pressed("UP")):
        # fundoPosY +=1
        janelaPosY -= 2
    elif (teclado.key_pressed("DOWN")):
        # fundoPosY -=1
        janelaPosY += 2
    if (teclado.key_pressed("LEFT")):
        janelaPosX -= 2
        # fundoPosX +=1
    elif (teclado.key_pressed("RIGHT")):
        janelaPosX += 2
        # fundoPosX -=1

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

    for i in range(len(matrix) - 1):
        x, y = MapaParaTela(matrix[i][0], matrix[i][1], janelaPosX, janelaPosY)
        nuvemDengue.set_position(x, y)
        nuvemDengue.draw()

    # incializar a posição do sprite no centro da tela
    ufoPosX = janelaPosX + janela.width / 2 - ufo.width / 2
    ufoPosY = janelaPosY + janela.height / 2 - ufo.height / 2
    xt, yt = MapaParaTela(ufoPosX, ufoPosY, janelaPosX, janelaPosY)
    ufo.set_position(xt, yt)
    ufo.draw()

    janela.update()

    if (Collision.collided(ufo, nuvemDengue)):
        print("win")


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
