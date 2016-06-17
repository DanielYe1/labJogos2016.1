from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *

janela = Window(535, 535)

janela.set_title("My Game")


janela.set_background_color((0, 0, 0))
janela.update()


ball = Sprite("red_enemy.png")

while(True):
    bgimage = GameImage("background.png")


    bgimage.draw()
    janela.update()

    ball.move_key_x(3)
    ball.move_key_y(3)
    ball.draw()
    janela.update()