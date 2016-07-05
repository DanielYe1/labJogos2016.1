from PPlay.window import *
from PPlay.keyboard import *
from PPlay.gameimage import *
from PPlay.sprite import *
from random import *
from math import *

# Cria janela
xJanela = 800
yJanela = 451
janela = Window(xJanela, yJanela)

# Cria Pororoca
pororoca = Sprite("pororoca.png", 10)
pororoca.set_total_duration(1250)


# Desenhar Sprite
def desenharSprite(sprite, cordX, cordY):
    sprite.set_position(cordX, cordY)
    sprite.draw()
    sprite.update()


# Mover Fundo
SCROLLINGSPEED = 300


def updateBackgroundPosition(background,bgPosX, bgPosY):  ## certo
    bgPosX -= SCROLLINGSPEED * janela.delta_time()
    if bgPosX <= -background.width:
        bgPosX = 0
    return bgPosX, bgPosY


def createBackGround(filename):
    background = GameImage(filename)
    bgPosX = 0
    bgPosY = 0
    return background, bgPosX, bgPosY


def drawBackground(background, bgPosX, bgPosY):
    background.set_position(bgPosX + background.width, bgPosY)
    background.draw()
    background.set_position(bgPosX, bgPosY)
    background.draw()
# Terminar de mover fundo

# Criar Background
background, xFundo, yFundo = createBackGround("Background_01jungle.jpg")

# Game Loop
while True:
    xFundo, yFundo = updateBackgroundPosition(background,xFundo, yFundo)
    drawBackground(background, xFundo, yFundo)
    desenharSprite(pororoca, -120, 170)
    janela.update()
