from PPlay.window import *
from PPlay.keyboard import *
from PPlay.gameimage import *
from PPlay.sprite import *
from random import *
from math import *

janela = Window(250,250)

moeda = Sprite("sarcofago_teste_f10.png",10)
moeda.set_total_duration(500)

while True:
    janela.set_background_color((255,255,255))
    moeda.draw()
    moeda.update()
    janela.update()