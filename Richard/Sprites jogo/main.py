from PPlay.window import *
from PPlay.keyboard import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.collision import *
from random import *
from math import *
from datetime import datetime

# Cria teclado
teclado = Keyboard()

# Cria janela
xJanela = 800
yJanela = 451
janela = Window(xJanela, yJanela)


# Classe Richard
class richard:
    def __init__(self, spriteCorrendo, spritePulando, spriteAbaixando, spriteAtual, posX, posY, speedY):
        self.spriteCorrendo = spriteCorrendo
        self.spritePulando = spritePulando
        self.spriteAbaixando = spriteAbaixando
        self.spriteAtual = spriteAtual
        self.posX = posX
        self.posY = posY
        self.speedY = speedY
        spriteCorrendo.set_total_duration(450)
        spriteCorrendo = spriteCorrendo.set_sequence(0, 4)
        spritePulando.set_total_duration(0)
        spritePulando = spritePulando.set_sequence(4, 5)
        spriteAbaixando.set_total_duration(0)
        spriteAbaixando = spriteAbaixando.set_sequence(5, 6)
        if spriteAtual == spriteCorrendo:
            spriteAtual.set_total_duration(450)
        else:
            spriteAtual.set_total_duration(0)

    def updateHeroPosition(self, dt):
        self.posY += self.speedY * dt
        if self.posY < 350:
            self.speedY += gravidade * dt
        else:
            self.speedY = 0
            self.posY = 350


# Gravidade

gravidade = 1000

richard = richard(Sprite("./sprites/richard60.png", 6), Sprite("./sprites/richard60.png", 6),
                  Sprite("./sprites/richard60.png", 6),
                  Sprite("./sprites/richard60.png", 6), 300, 350, -500)


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
def criarPokemons():
    pokes = []
    mantine = pokemon(
        Sprite("./sprites/Ar/arraia_fps21.png", 21), True)
    qwilfish = pokemon(
        Sprite("./sprites/Ar/baiacu_fps33.png", 33), True)
    beedrill = pokemon(
        Sprite("./sprites/Ar/beedrill_fps20.png", 20), True)
    kyogre = pokemon(
        Sprite("./sprites/Ar/kyogre_fps24.png", 24),
        True)
    lanturn = pokemon(
        Sprite("./sprites/Ar/lanturne_fps16.png", 16), True)
    carvana = pokemon(
        Sprite("./sprites/Ar/piranha_fps19.png", 19), True)
    pori2 = pokemon(
        Sprite("./sprites/Ar/pori2_fps12.png", 12),
        True)
    sharpedo = pokemon(
        Sprite("./sprites/Ar/shapedo_fps19.png", 19), True)
    wailord = pokemon(
        Sprite("./sprites/Ar/wailord_fps28.png", 28), True)
    woobat = pokemon(
        Sprite("./sprites/Ar/woobat_fps16.png", 16),
        True)
    yanma = pokemon(
        Sprite("./sprites/Ar/yama_fps21.png", 21),
        True)
    zoobat = pokemon(
        Sprite("./sprites/Ar/zoobat_fps20.png", 20),
        True)
    # fim

    # terrestres
    bloqueador = pokemon(
        Sprite("./sprites/Terra/bloqueador_fps17.png", 17),
        False)
    gamba = pokemon(
        Sprite("./sprites/Terra/gamba_fps16.png", 16), False)
    golem = pokemon(
        Sprite("./sprites/Terra/golem_fps16.png", 16), False)
    hipo = pokemon(
        Sprite("./sprites/Terra/hipopotamo_fps16.png", 16),
        False)
    lesma = pokemon(
        Sprite("./sprites/Terra/lesma_fps9.png", 9),
        False)
    muk = pokemon(
        Sprite("./sprites/Terra/muk_fps17.png", 17),
        False)
    quilava = pokemon(
        Sprite("./sprites/Terra/quilava_fps18.png", 18),
        False)
    raticate = pokemon(
        Sprite("./sprites/Terra/raticate_fps11.png", 11),
        False)
    sarcofago = pokemon(
        Sprite("./sprites/Terra/sacofago_fps17.png", 17),
        False)
    torterra = pokemon(
        Sprite("./sprites/Terra/torterra_fps11.png", 11),
        False)
    vic = pokemon(
        Sprite("./sprites/Terra/vic_fps19.png", 19),
        False)
    wailmer = pokemon(
        Sprite("./sprites/Terra/wailmer_fps21.png", 21),
        False)
    pokes = [sarcofago, mantine, qwilfish, beedrill, kyogre, lanturn, carvana, pori2, sharpedo, wailord, woobat,
             yanma, zoobat, bloqueador, gamba, golem, hipo, lesma, muk, quilava, raticate, torterra, vic, wailmer]
    return pokes


pokes = criarPokemons()

# Cria Pororoca
pororoca = Sprite("./sprites/pororoca.png", 10)
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

# Desenhar pokemons junto com colisão
def desenharPokes(pokemonsNaHora, count):
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
        # treta, pode dar ruim
        if Collision.perfect_collision(x.sprite, richard.spriteAtual):
            x.cordX = xJanela
            if x.voador:
                x.cordY = yJanela * 0.55
            else:
                x.cordY = yJanela * 0.8
            pokemonsNaHora.remove(x)
            count += 1
    return count


# Criar Background
background, xFundo, yFundo = createBackGround("./images/Background_01jungle.jpg")

pokemonsNaHora = []

pokemonRate = 300
count = 0
telaAtual = 'menu'


def textosImg(imagem, posx=0, posy=0):
    imagem.set_position(posx, posy)
    imagem.draw()
    return 0


def menu(xJanela, yJanela):
    global telaAtual
    # Criar Background
    drawBackground(background, xFundo, yFundo)
    textos = dict(
        logo=GameImage('./images/logoRunRunRichard.png'),
        enter=GameImage('./images/aperteEnter.png'),
        scrore=GameImage('./images/score.png'),
    )
    textosImg(textos['logo'], xJanela / 2 - textos['logo'].width / 2, 20)
    textosImg(textos['enter'], xJanela / 2 - textos['enter'].width / 2, yJanela / 2 + 80)
    if teclado.key_pressed("ENTER"):
        telaAtual = 'start'


# ranking
def gravaRanking(distPercorrida, nomeArq):
    bd = open(nomeArq, 'r')
    bc = open('copia.txt', 'w')
    for linha in bd:
        dado = linha.strip().split()
        if distPercorrida > int(dado[0]):
            bc.write(str(distPercorrida) + " " + str(datetime.now()) + "\n")
            distPercorrida = 0
        bc.write(linha)
    bd.close()
    bc.close()
    bd = open(nomeArq, "w")
    bc = open("copia.txt", "r")
    count = 0
    for linha in bc:
        count += 1
        if count <= 3:
            bd.write(linha)
    bd.close()
    bc.close()


def ranking(xJanela, yJanela):
    bd = open('ranking.txt')
    ranking = []
    for linha in bd:
        ranking.append(linha.strip().split())
    global telaAtual
    drawBackground(background, xFundo, yFundo)
    score = GameImage('./images/score.png')
    score.set_position(xJanela / 2 - score.width / 2, 20)
    score.draw()
    for i in range(0, len(ranking)):
        janela.draw_text(str(i + 1) + 'º: ' + ranking[i][1] + ': ' + ranking[i][0], xJanela / 2 - score.width / 2.5,
                         100 + (i * 40), 30, (255, 235, 143), "Helvetica", True)
    enterEsc = GameImage('./images/enterEsc.png')
    enterEsc.set_position(xJanela / 2 - enterEsc.width / 2, 260)
    enterEsc.draw()
    bd.close()
    if teclado.key_pressed("ENTER"):
        telaAtual = 'start'
    elif teclado.key_pressed("ESCAPE"):
        janela.close()


nomeArq = "ranking.txt"

tempoInutil = 0
# Game Loop
while True:
    if telaAtual == 'menu':
        menu(xJanela, yJanela)
        tempoInutil = janela.total_time
    elif telaAtual == 'start':
        dt = janela.delta_time()
        xFundo, yFundo = updateBackgroundPosition(background, xFundo, yFundo)
        drawBackground(background, xFundo, yFundo)
        if janela.total_time % 300 == 0:
            pokemonsNaHora.append(escolherPoke(pokes))
            pokemonRate -= 1

        # gravidade e mudança de sprites
        if teclado.key_pressed("UP") and richard.posY == 350:
            richard.speedY = -500
        elif teclado.key_pressed("DOWN") and richard.posY == 350:
            richard.spriteAtual = richard.spriteAbaixando
        elif richard.posY < 350:
            richard.spriteAtual = richard.spritePulando
        elif richard.posY == 350:
            richard.spriteAtual = richard.spriteCorrendo
        desenharSprite(richard.spriteAtual, richard.posX, richard.posY)

        count = desenharPokes(pokemonsNaHora, count)

        desenharSprite(pororoca, -120, 170)
        richard.updateHeroPosition(dt)
        distancia = int(((janela.total_time - tempoInutil) / 300))
        janela.draw_text('Distância: ' + str(distancia), 5, 5, 40, (255, 235, 143), "Helvetica", True)
        janela.draw_text('Vidas: ' + str(3 - count), xJanela - 150, 5, 40, (255, 235, 143), "Helvetica", True)

        if count >= 3:
            gravaRanking(distancia, nomeArq)
            count = 0
            distancia = 0
            telaAtual = 'score'
    elif telaAtual == 'score':
        ranking(xJanela, yJanela)
        tempoInutil = janela.total_time

    janela.update()
