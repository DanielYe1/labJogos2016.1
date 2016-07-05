# importei os módulos necessários do PPlay
from PPlay.window import *
from PPlay.keyboard import *
from PPlay.gameimage import *
from PPlay.sprite import *
from random import *
from math import *

# Criar constantes

# Tamanho da janela
TAMJANELA_X = 512
TAMJANELA_Y = 512

# Numero de quadrantes do mapa
NQUADRANTES_X = 32
NQUADRANTES_Y = 32

# Numero de focos de insetos
NFOCOS = 20

# Velocidade da aeronave
SPEED = 260

# criar um janela de 512x512 pixels
janela = Window(TAMJANELA_X, TAMJANELA_Y)

# criar um teclado para interagir com o jogo
teclado = Keyboard()

# criar o fundo do cenário
fundo = GameImage("pokemonmap.png")

# posicao do fundo do cenario
fundoPosX = 0
fundoPosY = 0

# posicionar a janela no centro do mapa
janelaPosX = fundo.width / 2 - janela.width / 2
janelaPosY = fundo.height / 2 - janela.height / 2


# Converte coordenadas do mundo para tela
def mapaParaTela(xm, ym, janelaPosX, janelaPosY):
    xt = xm - janelaPosX
    yt = ym - janelaPosY
    # para de coordenadas da janela retornados
    return xt, yt


# Calcula os indices da matriz de objetos correspondente
# a uma posicao (xm,ym) em coordenadas do mapa
def mapaParaCoordDescricao(xm, ym, nLin, nCol, tamMapaX, tamMapaY):
    tamQuadranteX = tamMapaX / nCol
    tamQuadranteY = tamMapaY / nLin

    i = int(ym / tamQuadranteY)
    j = int(xm / tamQuadranteX)
    # retorna os indices da matriz
    return i, j


def desenharFundo(fundo):
    # atualização do fundo
    xt, yt = mapaParaTela(fundoPosX, fundoPosY, janelaPosX, janelaPosY)
    fundo.set_position(xt, yt)
    fundo.draw()


def desenharHelicoptero(heli):
    # incializar a posição do sprite no centro da tela
    heliPosX = janelaPosX + janela.width / 2 - heli.width / 2
    heliPosY = janelaPosY + janela.height / 2 - heli.height / 2
    xt, yt = mapaParaTela(heliPosX, heliPosY, janelaPosX, janelaPosY)
    heli.set_position(xt, yt)
    heli.update()
    heli.draw()


# Cria uma matriz que armazena objetos do jogo dispostos no mapa
def criarDescricaoMapa(nLin, nCol):
    # inicializar uma matriz vazia
    elemMapa = []
    # para cada linha
    for lin in range(0, nLin):
        # cria uma linha vazia
        linha = []
        # preencha a linha com nCol zeros
        # zero indica que nao ha objetos
        for col in range(0, nCol):
            linha.append(0)
        # adiciona a nova linha a matriz
        elemMapa.append(linha)
    # retorna a matriz criada
    return elemMapa


# Cria Rockets
def criarRockets(elemMapa, numFocos, larguraMapa, alturaMapa):
    # repetir numFocos vezes a operacao de criacao
    for n in range(0, numFocos):
        # criar um sprite para um foco
        foco = Sprite("rocketTeam.gif")
        # sortear a posicao no mapa e armzenar os valores
        foco.xm = randint(0, larguraMapa)
        foco.ym = randint(0, alturaMapa)

        # posicionar o foco nas coordenadas sorteadas
        foco.set_position(foco.xm, foco.ym)

        # calcular a posicao na matriz
        nLin = len(elemMapa)
        nCol = len(elemMapa[0])
        i, j = mapaParaCoordDescricao(foco.xm, foco.ym, nLin, nCol,
                                      fundo.width, fundo.height)
        # atribuir o foco ao elemento da matriz
        elemMapa[i][j] = foco


# Cria Pikachu
def criarPikachu(elemMapa, numFocos, larguraMapa, alturaMapa):
    # repetir numFocos vezes a operacao de criacao
    for n in range(0, numFocos):
        # criar um sprite para um foco
        foco = Sprite("pikachu.png")
        # sortear a posicao no mapa e armzenar os valores
        foco.xm = randint(0, larguraMapa)
        foco.ym = randint(0, alturaMapa)

        # posicionar o foco nas coordenadas sorteadas
        foco.set_position(foco.xm, foco.ym)

        # calcular a posicao na matriz
        nLin = len(elemMapa)
        nCol = len(elemMapa[0])
        i, j = mapaParaCoordDescricao(foco.xm, foco.ym, nLin, nCol,
                                      fundo.width, fundo.height)
        # atribuir o foco ao elemento da matriz
        elemMapa[i][j] = foco


# Preencher a matriz com os focos de insetos
def criarFocos(elemMapa, numFocos, larguraMapa, alturaMapa):
    # repetir numFocos vezes a operacao de criacao
    for n in range(0, numFocos):
        # criar um sprite para um foco
        foco = Sprite("bola.png")
        # sortear a posicao no mapa e armzenar os valores
        foco.xm = randint(0, larguraMapa)
        foco.ym = randint(0, alturaMapa)

        # posicionar o foco nas coordenadas sorteadas
        foco.set_position(foco.xm, foco.ym)

        # calcular a posicao na matriz
        nLin = len(elemMapa)
        nCol = len(elemMapa[0])
        i, j = mapaParaCoordDescricao(foco.xm, foco.ym, nLin, nCol,
                                      fundo.width, fundo.height)
        # atribuir o foco ao elemento da matriz
        elemMapa[i][j] = foco


def checarColisao(heli, elemMapa):
    nLin = len(elemMapa)
    nCol = len(elemMapa[0])
    for i in range(0, nLin):
        for j in range(0, nCol):
            if (elemMapa[i][j] != 0):
                foco = elemMapa[i][j]
                if heli.collided_perfect(foco):
                    elemMapa[i][j] = 0
                    return True


# Desenha a infestacao de insetos
def desenharFocos(elemMapa):
    nLin = len(elemMapa)
    nCol = len(elemMapa[0])
    # Para cada elemento da matriz
    for i in range(0, nLin):
        for j in range(0, nCol):
            # se o elemento existir
            if (elemMapa[i][j] != 0):
                # pegar o foco
                foco = elemMapa[i][j]
                # converter suas coordenadas de mapa para tela
                xt, yt = mapaParaTela(foco.xm, foco.ym, janelaPosX, janelaPosY)
                # posicionar o foco na janela
                foco.set_position(xt, yt)
                # desenhar
                foco.draw()


def criarHelicoptero():
    # criar sprite
    heli = Sprite("heli.png", 3)
    # define a direcao do helicoptero (90 graus e a direcao norte)
    heli.dir = 90
    # define o tamanho do sprite (sua escala)
    heli.scale = 1
    # define o tempo de duracao de cada frame da animacao do sprite
    heli.set_total_duration(250)
    # posiciona o sprite no centro da janela
    heli.set_position(janela.width / 2, janela.height / 2)

    return heli


# faz o tratamento da entrada de dados do jogador
def input(janelaPosX, janelaPosY, heli):
    if (teclado.key_pressed("UP")):  # atualiza a posicao delocando a janela para cima
        janelaPosX += SPEED * janela.delta_time() * cos(heli.dir * pi / 180)
        janelaPosY -= SPEED * janela.delta_time() * sin(heli.dir * pi / 180)
    elif (teclado.key_pressed("DOWN")):  # desloca para baixo
        janelaPosX -= SPEED * janela.delta_time() * cos(heli.dir * pi / 180)
        janelaPosY += SPEED * janela.delta_time() * sin(heli.dir * pi / 180)
    if (teclado.key_pressed("LEFT")):  # altera a orientacao do helicoptero
        heli.dir += 1
        # rotaciona e aplica escala ao helicoptero
        heli.rotatescale(heli.dir - 90, heli.scale)
    elif (teclado.key_pressed("RIGHT")):
        heli.dir -= 1
        heli.rotatescale(heli.dir - 90, heli.scale)
    elif (teclado.key_pressed("a")):  # altera o tamanho do helicoptero
        heli.scale *= 1.01
        # limita a mudanca de escala no minimo metade e no maximo o dobro do tamanho
        if heli.scale < 0.5:
            heli.scale = 0.5
        elif heli.scale > 2.0:
            heli.scale = 2.0
        heli.rotatescale(heli.dir - 90, heli.scale)
    elif (teclado.key_pressed("s")):
        heli.scale *= 0.99
        if heli.scale < 0.5:
            heli.scale = 0.5
        elif heli.scale > 2.0:
            heli.scale = 2.0
        heli.rotatescale(heli.dir - 90, heli.scale)

    return janelaPosX, janelaPosY


# Impede que a camera saia do mapa
def limitarMovimentoJanela(janelaPosX, janelaPosY):
    # checar os limites
    if janelaPosX <= -janela.width / 2:
        janelaPosX = -janela.width / 2
    elif janelaPosX >= fundo.width - janela.width / 2:
        janelaPosX = fundo.width - janela.width / 2

    if janelaPosY <= -janela.height / 2:
        janelaPosY = -janela.height / 2
    elif janelaPosY >= fundo.height - janela.height / 2:
        janelaPosY = fundo.height - janela.height / 2

    return janelaPosX, janelaPosY


heli = criarHelicoptero()

# criar a matriz de elementos
elemMapa = criarDescricaoMapa(NQUADRANTES_X, NQUADRANTES_Y)
elemMapaPikachu = criarDescricaoMapa(NQUADRANTES_X, NQUADRANTES_Y)
elemMapaRocket = criarDescricaoMapa(NQUADRANTES_X, NQUADRANTES_Y)
# instanciar os focos no mapa
criarFocos(elemMapa, NFOCOS, fundo.width, fundo.height)
criarPikachu(elemMapaPikachu, 2, fundo.width, fundo.height)
criarRockets(elemMapaRocket, 2, fundo.width, fundo.height)

score = 0  #### eu fiz


def mensagensPlacar(score):
    if score == 50:
        janela.draw_text("Você começou sua jornada pokemon!!", 50, (TAMJANELA_Y / 2) - 200, 20, (255, 255, 255),
                         "Calibri", True)
    if score == 100:
        janela.draw_text("Você já manja dos paranâue!!", 50, (TAMJANELA_Y / 2) - 200, 20, (255, 255, 255), "Calibri",
                         True)
    if score == 500:
        janela.draw_text("Você já é um mestre pokemon!!", 50, (TAMJANELA_Y / 2) - 200, 20, (255, 255, 255), "Calibri",
                         True)
    if score == 1000:
        janela.draw_text("Boa Anselmo!!", 50, (TAMJANELA_Y / 2) - 200, 70, (255, 255, 255), "Calibri", True)


fim = False
# Game Loop
while True:
    # Limpar a tela com cor negra
    janela.set_background_color((0, 0, 0))

    janelaPosX, janelaPosY = input(janelaPosX, janelaPosY, heli)
    janelaPosX, janelaPosY = limitarMovimentoJanela(janelaPosX, janelaPosY)
    if checarColisao(heli, elemMapa):
        score += 1
    if checarColisao(heli, elemMapaPikachu):
        score += 5

    if janela.total_time % 3000 == 0:
        criarFocos(elemMapa, NFOCOS, fundo.width, fundo.height)
        criarPikachu(elemMapaPikachu, 1, fundo.width, fundo.height)
        criarRockets(elemMapaRocket, 1, fundo.width, fundo.height)
    desenharFundo(fundo)

    mensagensPlacar(score)
    desenharFocos(elemMapa)
    desenharFocos(elemMapaPikachu)
    desenharFocos(elemMapaRocket)
    janela.draw_text(str(score), 5, TAMJANELA_Y - 50, 40, (255, 255, 255), "Calibri", True)
    desenharHelicoptero(heli)
    if checarColisao(heli,elemMapaRocket):
        fim = True
    if fim:
        janela.set_background_color((0, 0, 0))
        janela.draw_text("A EQUIPE ROCKET TE PEGOU!", 5, 5, 40, (255, 255, 255), "Calibri", True)
        if teclado.key_pressed("ENTER"):
            fim = False

    janela.update()
