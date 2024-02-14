import pygame
#O * esta importando todas as funçoes e todas as contantes
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480
#x = 0
#y = 0

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Tela')

while True:
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    #Desenhando um retangulo, primeiro paramentro a tela,depois a cor, em seguida o posiçao depois a largura
    #e a altura do quadrado
    pygame.draw.rect(tela, (255,0,0), (255,100,100,50))
    #if y >= altura:
        #y = 0

    #y = y + 1
    #Para o circulo eu preciso informar o radius, que foi 4,é  a espessura do circulo
    #pygame.draw.circle(tela, (125,125,0),(100,400),50)
    #Para a linha e precisa passar o ponto que ela se inicia no caso e (400,0) e onde ela termina que e
    #(300,0) e por ultimo tem a espessura da linha
    #pygame.draw.line(tela, (150,130,45),(255,   0),(150,0), 5)
    #pygame.display.update()


