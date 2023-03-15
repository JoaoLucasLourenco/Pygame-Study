import pygame
from pygame.locals import *
from sys import exit
from random import randint
pygame.init()

largura = 1280
altura = 720

x_cobra = largura/2
y_cobra = altura/2

x_maca = 100
y_maca = 100

velocidade = 10
x_controle = velocidade
y_controle = 0

musica_fundo = pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1)

fonte = pygame.font.SysFont('arial',40,True,True)
pontos=0

relogio = pygame.time.Clock()
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Joguin do Jão")

lista_cobra = []
comprimento_inicial = 5

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0,255,0), (XeY[0],XeY[1],40,40))

while True:
    relogio.tick(60)
    tela.fill((255,255,255))
    
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.QUIT
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle
    

    
    
    cobra = pygame.draw.rect(tela,(0,255,0),(x_cobra,y_cobra,40,40))
    maca = pygame.draw.rect(tela,(255,0,0),(x_maca,y_maca,20,20))
    
    if maca.colliderect(cobra):
        y_maca = randint(50,430)
        x_maca = randint(40,600)
        pontos+=1
        comprimento_inicial +=1

    
    if event.type == KEYDOWN:
        if event.key ==K_a:
            x_cobra+=20 
    
    
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    
    
    lista_cobra.append(lista_cabeca)
    
    if len(lista_cobra)>comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)


    if x_cobra==largura:
        x_cobra-=60
    elif x_cobra==0:
        x_cobra+=60
    if y_cobra==altura:
        y_cobra-=60
    elif y_cobra==0:
        y_cobra+=60
    
        
    tela.blit(texto_formatado, (430,40))
    pygame.display.update()
