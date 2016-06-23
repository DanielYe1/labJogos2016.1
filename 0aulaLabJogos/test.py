# As usual, we import our Window class
from PPlay.window import *
# Then we import Sprite - that inherits methods from GameObject
from PPlay.sprite import *

window = Window(500, 500)
ball1 = Sprite("graycreep.png")
ball2 = Sprite("red_enemy.png")

# Defining a initial position to both Sprites
ball1.set_position(100, 0)
ball2.set_position(100, 400)

# Speed
ball1_speed = 120  # POSITIVE MEANS DOWN!!!
ball2_speed = -120  # NEGATIVE MEANS UP!!!

janela = Window(512, 512)
while (True):
    janela.set_background_color((255, 255, 255))

    # We'll move both balls towards each other.
    # Y AXIS POSTIVE MEANS DOWN!!!
    ball1.move_y(ball1_speed * window.delta_time())
    ball2.move_y(ball2_speed * window.delta_time())

    # Check if ball2 collided with ball1.
    # if(ball2.collided(ball1)):
    if (ball1.collided(ball2)):
        ball1_speed = 0  # stays in its place
        ball2_speed = 0

        print("They collided in:", ball2.y)

    ball1.draw()
    ball2.draw()

    window.update()
    # You just import Collision class
    from PPlay.collision import *

    # And change the line 28 ->
    # if(ball1.collided(ball2)):
    # To this ->
    if (Collision.collided(ball1, ball2)):
        print("WIN")
