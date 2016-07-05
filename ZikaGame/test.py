from PPlay.window import *
from PPlay.keyboard import *
from PPlay.gameimage import *
from PPlay.sprite import *
from random import *
from math import *

janela = Window(250,250)

moeda = Sprite("Dragon-coin.gif",10)
moeda.set_total_duration(1250)

while True:
    moeda.draw()
    moeda.update()
    janela.update()