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


# Classe Richard
class richard:
    def __init__(self, spriteCorrendo, spritePulando, spriteAbaixando, qtTiros):
        self.spriteCorrendo = spriteCorrendo
        self.spritePulando = spritePulando
        self.spriteAbaixando = spriteAbaixando
        self.qtTiros = qtTiros


# Classe pokemon
class pokemon:
    def __init__(self, sprite, voador):
        self.sprite = sprite
        self.voador = voador
        sprite.set_total_duration(1250)
        self.cordX = xJanela
        if voador:
            self.cordY = yJanela * 0.55
        else:
            self.cordY = yJanela * 0.8


# Criar Pokemons
def escolherPoke(vetor):
    escolha = randint(0, len(vetor) - 1)
    return vetor[escolha]


# Cria Pokemons

# aereos

mantine = pokemon(
    Sprite("D:/Daniel/PycharmProjects/test/labJogos/Richard/Sprites jogo/sprites/Ar/arraia_fps21.png", 21), True)
qwilfish = pokemon(
    Sprite("D:/Daniel/PycharmProjects/test/labJogos/Richard/Sprites jogo/sprites/Ar/baiacu_fps33.png", 33), True)
beedrill = pokemon(
    Sprite("D:/Daniel/PycharmProjects/test/labJogos/Richard/Sprites jogo/sprites/Ar/beedrill_fps20.png", 20), True)
kyogre = pokemon(Sprite("D:/Daniel/PycharmProjects/test/labJogos/Richard/Sprites jogo/sprites/Ar/kyogre_fps24.png", 24),
                 True)
lanturn = pokemon(
    Sprite("D:/Daniel/PycharmProjects/test/labJogos/Richard/Sprites jogo/sprites/Ar/lanturne_fps16.png", 16), True)
pidgey = pokemon(Sprite("D:/Daniel/PycharmProjects/test/labJogos/Richard/Sprites jogo/sprites/Ar/pigey_fps18.png", 18),
                 True)
carvana = pokemon(
    Sprite("D:/Daniel/PycharmProjects/test/labJogos/Richard/Sprites jogo/sprites/Ar/piranha_fps19.png", 19), True)
pori2 = pokemon(Sprite("D:/Daniel/PycharmProjects/test/labJogos/Richard/Sprites jogo/sprites/Ar/pori2_fps12.png", 12),
                True)
sharpedo = pokemon(
    Sprite("D:/Daniel/PycharmProjects/test/labJogos/Richard/Sprites jogo/sprites/Ar/shapedo_fps19.png", 19), True)
wailord = pokemon(
    Sprite("D:/Daniel/PycharmProjects/test/labJogos/Richard/Sprites jogo/sprites/Ar/wailord_fps28.png", 28), True)
woobat = pokemon(Sprite("D:/Daniel/PycharmProjects/test/labJogos/Richard/Sprites jogo/sprites/Ar/woobat_fps16.png", 16),
                 True)
yanma = pokemon(Sprite("D:/Daniel/PycharmProjects/test/labJogos/Richard/Sprites jogo/sprites/Ar/yama_fps21.png", 21),
                True)
zoobat = pokemon(Sprite("D:/Daniel/PycharmProjects/test/labJogos/Richard/Sprites jogo/sprites/Ar/zoobat_fps20.png", 20),
                 True)

# terrestres
bloqueador = pokemon(
    Sprite("D:/Daniel/PycharmProjects/test/labJogos/Richard/Sprites jogo/sprites/Terra/bloqueador_fps17.png", 17),
    False)
gamba = pokemon(
    Sprite("D:/Daniel/PycharmProjects/test/labJogos/Richard/Sprites jogo/sprites/Terra/gamba_fps16.png", 16), False)
golem = pokemon(
    Sprite("D:/Daniel/PycharmProjects/test/labJogos/Richard/Sprites jogo/sprites/Terra/golem_fps16.png", 16), False)
hipo = pokemon(
    Sprite("D:/Daniel/PycharmProjects/test/labJogos/Richard/Sprites jogo/sprites/Terra/hipopotamo_fps16.png", 16),
    False)
lesma = pokemon(Sprite("D:/Daniel/PycharmProjects/test/labJogos/Richard/Sprites jogo/sprites/Terra/lesma_fps9.png", 9),
                False)
muk = pokemon(Sprite("D:/Daniel/PycharmProjects/test/labJogos/Richard/Sprites jogo/sprites/Terra/muk_fps17.png", 17),
              False)
quilava = pokemon(
    Sprite("D:/Daniel/PycharmProjects/test/labJogos/Richard/Sprites jogo/sprites/Terra/quilava_fps18.png", 18), False)
raticate = pokemon(
    Sprite("D:/Daniel/PycharmProjects/test/labJogos/Richard/Sprites jogo/sprites/Terra/raticate_fps11.png", 11), False)
sarcofago = pokemon(
    Sprite("D:/Daniel/PycharmProjects/test/labJogos/Richard/Sprites jogo/sprites/Terra/sacofago_fps17.png", 17), False)
torterra = pokemon(
    Sprite("D:/Daniel/PycharmProjects/test/labJogos/Richard/Sprites jogo/sprites/Terra/torterra_fps11.png", 11), False)
vic = pokemon(Sprite("D:/Daniel/PycharmProjects/test/labJogos/Richard/Sprites jogo/sprites/Terra/vic_fps19.png", 19),
              False)
wailmer = pokemon(
    Sprite("D:/Daniel/PycharmProjects/test/labJogos/Richard/Sprites jogo/sprites/Terra/wailmer_fps21.png", 21), False)

pokes = [sarcofago, mantine, qwilfish, beedrill, kyogre, lanturn, pidgey, carvana, pori2, sharpedo, wailord, woobat,
         yanma, zoobat, bloqueador, gamba, golem, hipo, lesma, muk, quilava, raticate, torterra, vic, wailmer]

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


def updateBackgroundPosition(background, bgPosX, bgPosY):  ## certo
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

pokemonsNaHora = []

# Game Loop
while True:
    xFundo, yFundo = updateBackgroundPosition(background, xFundo, yFundo)
    drawBackground(background, xFundo, yFundo)
    if janela.total_time % 300 == 0 or len(pokemonsNaHora) == 0:
        pokemonsNaHora.append(escolherPoke(pokes))
    for x in set(pokemonsNaHora):
        x.cordX, x.cordY = updateBackgroundPosition(x.sprite, x.cordX, x.cordY)
        if x.cordX < 50:
            x.cordX = xJanela
            if x.voador:
                x.cordY = yJanela * 0.55
            else:
                x.cordY = yJanela * 0.8
            pokemonsNaHora.remove(x)
        desenharSprite(x.sprite, x.cordX, x.cordY)
    desenharSprite(pororoca, -120, 170)
    janela.update()
