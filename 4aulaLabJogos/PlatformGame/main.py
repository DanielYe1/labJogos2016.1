__author__ = 'Anselmo'

from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.keyboard import *

window = Window (640,640)

teclado = Keyboard()

background = GameImage("seamlessbackground.jpg")

class hero:
    def __init__(self,animation,activeAnimation,posX,posY,speedX,speedY,lifes):
        self.animation = animation
        self.activeAnimation = activeAnimation
        self.posX = posX
        self.posY = posY
        self.speedX = speedX
        self.speedY = speedY
        self.lifes = lifes

pessoa = hero([],0,250,400,0,0,3)

pessoa.animation.append(Sprite("sl.png",1))
pessoa.animation.append(Sprite("sr.png",1))
pessoa.animation.append(Sprite("wl.png",6))
pessoa.animation.append(Sprite("wr.png",6))
for i in range(len(pessoa.animation)):
    pessoa.animation[i].set_total_duration(1250)
    pessoa.animation[i].set_position(pessoa.posX,pessoa.posY)

direita = True
esquerda = False

bgX = 0
bgY = 0
walkingSpeed = 100

while True:
    background.set_position(bgX,bgY)
    background.draw()
    if teclado.key_pressed("RIGHT"):
        pessoa.animation[2].update()
        pessoa.animation[2].draw()
        bgX-=walkingSpeed*window.delta_time()
        direita = True
        esquerda = False
    elif direita:
        pessoa.animation[1].draw()
    if teclado.key_pressed("LEFT"):
        pessoa.animation[3].update()
        pessoa.animation[3].draw()
        bgX+=walkingSpeed*window.delta_time()
        direita = False
        esquerda = True
    elif esquerda:
        pessoa.animation[0].draw()

    window.update()