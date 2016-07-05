__author__ = "Daniel Ye"

from PPlay.window import *
from PPlay.keyboard import *
from PPlay.gameimage import *
from PPlay.sprite import *
from random import *

SCROLLINGSPEED = 100
window = Window(548, 547)


# teste com orientação a objetos
class tiro:
    def __init__(self, sprite, posX, posY, speed, last_shot, lista_tiros):
        self.sprite = Sprite(sprite)
        self.posX = posX
        self.posY = posY
        self.speed = speed
        self.last_shot = last_shot
        self.lista_tiros = lista_tiros

class inimigo:
    def __init__(self, sprite, posX, posY, speed):
        self.sprite = Sprite(sprite)
        self.posX = posX
        self.posY = posY
        self.speed = speed

shot_delay = 300
shot = tiro("shot1.png", 0, 0, 200, 0, [])


def updateBackgroundPosition(bgPosX, bgPosY):  ## certo
    bgPosY += SCROLLINGSPEED * window.delta_time()
    if bgPosY >= window.height:
        bgPosY = 0
    return bgPosX, bgPosY


def createBackGround(filename):
    background = GameImage(filename)
    bgPosX = 0
    bgPosY = 0
    return background, bgPosX, bgPosY


def drawBackground(background, bgPosX, bgPosY):
    background.set_position(bgPosX, bgPosY - background.height)
    background.draw()
    background.set_position(bgPosX, bgPosY)
    background.draw()


keyboard = Keyboard()

ship = Sprite("spacefighter.png", 8)
ship.set_total_duration(500)


def desenharSprite(sprite):
    sprite.set_position(startX - totX, startY - totY)
    sprite.draw()
    sprite.update()


## limit position
def limitPosition(posX, posY):
    return None


## começar bonito
startX = (window.width - ship.width) / 2
startY = ((window.height - ship.height) / 2) + window.height / 3
totX = 0
totY = 0

background, bgPosX, bgPosY = createBackGround("spacebackgroundseamless.jpg")

while (True):
    bgPosX, bgPosY = updateBackgroundPosition(bgPosX, bgPosY)
    drawBackground(background, bgPosX, bgPosY)
    if keyboard.key_pressed("UP"):
        totY += 1
    elif keyboard.key_pressed("DOWN"):
        totY -= 1
    elif keyboard.key_pressed("RIGHT"):
        totX -= 1
    elif keyboard.key_pressed("LEFT"):
        totX += 1
    desenharSprite(ship)

    if keyboard.key_pressed("SPACE") and window.last_time - shot.last_shot > shot_delay:
        shot.lista_tiros.append([startX - totX + ship.width / 2 - shot.sprite.width / 2, startY - totY])
        shot.last_shot = window.last_time

    for i in shot.lista_tiros:
        i[1] -= shot.speed * window.delta_time()
        shot.sprite.set_position(i[0], i[1])
        shot.sprite.draw()
        if i[1]<=-shot.sprite.height:
            shot.lista_tiros.remove(i)
    window.update()
