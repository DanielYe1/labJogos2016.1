__author__ = 'Daniel Ye'

from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.keyboard import *

window = Window(640, 640)

teclado = Keyboard()

background = GameImage("seamlessbackground.jpg")


class hero:
    def __init__(self, animation, activeAnimation, posX, posY, speedX, speedY, lifes):
        self.animation = animation
        self.activeAnimation = activeAnimation
        self.posX = posX
        self.posY = posY
        self.speedX = speedX
        self.speedY = speedY
        self.lifes = lifes


pessoa = hero([], 0, 250, 400, 0, 0, 3)
gravidade = 1000


def updateHeroPosition(hero, dt):
    hero.posY += hero.speedY * dt
    if hero.posY < 400:
        hero.speedY += gravidade * dt
    else:
        hero.speedY = 0
        hero.posY = 400
    return hero.posX, hero.posY


# Cria sprites
pessoa.animation.append(Sprite("sl.png", 1))
pessoa.animation.append(Sprite("sr.png", 1))
pessoa.animation.append(Sprite("wl.png", 6))
pessoa.animation.append(Sprite("wr.png", 6))

for i in range(len(pessoa.animation)):
    pessoa.animation[i].set_total_duration(1250)
    pessoa.animation[i].set_position(pessoa.posX, pessoa.posY)

bgX = 0
bgY = 0
walkingSpeed = 100
pessoa.activeAnimation = Sprite("sr.png", 1)
pessoa.activeAnimation.set_position(pessoa.posX, pessoa.posY)
while True:
    background.set_position(bgX, bgY)
    dt = window.delta_time()

    background.draw()
    if teclado.key_pressed("RIGHT"):
        pessoa.activeAnimation = pessoa.animation[3]
        pessoa.activeAnimation.update()
        bgX -= walkingSpeed * window.delta_time()
    elif teclado.key_pressed("LEFT"):
        pessoa.activeAnimation = pessoa.animation[2]
        pessoa.activeAnimation.update()
        bgX += walkingSpeed * window.delta_time()
    else:
        if pessoa.activeAnimation == pessoa.animation[3]:
            pessoa.activeAnimation = pessoa.animation[1]
        elif pessoa.activeAnimation == pessoa.animation[2]:
            pessoa.activeAnimation = pessoa.animation[0]
    if teclado.key_pressed("UP") and pessoa.posY == 400:
        pessoa.speedY = -500

    pessoa.posX, pessoa.posY = updateHeroPosition(pessoa, dt)
    pessoa.activeAnimation.set_position(pessoa.posX, pessoa.posY)

    pessoa.activeAnimation.draw()
    print(pessoa.posY)

    window.update()
