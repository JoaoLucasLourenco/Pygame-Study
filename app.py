import pygame
from pygame.locals import *
from sys import exit
from random import randint
pygame.init()

largura = 640
altura = 480

x_cobra = largura/2
y_cobra = altura/2

x_maca = 100
y_maca = 100

musica_fundo = pygame.mixer.music.load('')
pygame.mixer.music.play(-1)

fonte = pygame.font.SysFont('arial',40,True,True)
pontos=0

relogio = pygame.time.Clock()
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Joguin do Jão")
while True:
    relogio.tick(60)
    tela.fill((255,255,255))
    
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.QUIT
            exit()
    if pygame.key.get_pressed()[K_a]:
        x_cobra-=20
    if pygame.key.get_pressed()[K_d]:
        x_cobra+=20
    if pygame.key.get_pressed()[K_w]:
        y_cobra-=20
    if pygame.key.get_pressed()[K_s]:
        y_cobra+=20
    
    
    cobra = pygame.draw.rect(tela,(0,255,0),(x_cobra,y_cobra,40,40))
    maca = pygame.draw.rect(tela,(255,0,0),(x_maca,y_maca,40,40))
    if maca.colliderect(cobra):
        y_azul = randint(50,430)
        x_azul = randint(40,600)
        pontos+=1
    
    if x_cobra==640:
        x_cobra-=60
    elif x_cobra==0:
        x_cobra+=60
    if y_cobra==480:
        y_cobra-=60
    elif y_cobra==0:
        y_cobra+=60
    
        
    tela.blit(texto_formatado, (430,40))
    pygame.display.update()
