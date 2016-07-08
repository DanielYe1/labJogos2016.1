from PPlay.window import *
from PPlay.keyboard import *
from PPlay.gameimage import *
from PPlay.sprite import *
from random import *
from math import *

janela = Window(250,250)

moeda = Sprite("sarcofago.png",144)
moeda.set_total_duration(1000)

while True:
    moeda.draw()
    moeda.update()
    janela.update()