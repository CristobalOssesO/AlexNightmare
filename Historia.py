import sys, pygame
from pygame.locals import *
from image import *


def Introduccion(e,screen):
    imgList = []
    a = pygame.image.load('images/intro1.png')
    b = pygame.image.load('images/intro2.png')
    c = pygame.image.load('images/intro3.png')
    d = pygame.image.load('images/intro4.png')
    e = pygame.image.load('images/intro5.png')
    f = pygame.image.load('images/intro6.png')
    h = pygame.image.load('images/intro6_1.png')
    i = pygame.image.load('images/intro6_2.png')
    j = pygame.image.load('images/intro7.png')
    k = pygame.image.load('images/intro7_1.png')
    l = pygame.image.load('images/intro7_1_2.png')
    m = pygame.image.load('images/intro7_2.png')
    n = pygame.image.load('images/intro8.png')
    imgList = [a,a, b,b, c,c,d, d, e, e, f, f, h,h, i,i,j,j,k,k,l,l,m,m,n,n]
    cont = 0
    screen.blit(imgList[cont], (0, 0))
    pygame.display.flip()
    
    pygame.mixer.music.load("Musica/Historia.mp3")
    pygame.mixer.music.play(-1)
    while 1:
        for e in pygame.event.get():
            if e.key == pygame.K_z:
                screen.blit(imgList[cont], (0, 0))
                pygame.display.flip()
                cont = cont + 1
                print cont
                if cont == 26:
                    return
                break
            break
    #mientras no aprete "siguiente" seguir mostrando la imagen

def Tutorial(screen):
    t = pygame.image.load('images/Tutorial.png')
    screen.blit(t, (0,0))
    pygame.display.flip()