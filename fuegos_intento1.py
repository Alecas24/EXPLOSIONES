import math
import random
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 800))
particles = [(random.gauss(0,.5), random.uniform(0,6.28318)) for i in range(2000)]


# INCISO A - FUNCIONA CORRECTAMENTE
def explotar(posx,posy,radio):
    for i in range(radio):
        screen.fill((255,255,255))
        for speed, angle in particles:
            distance = i * speed
            x = posx + distance * math.cos(angle)
            y = posy + distance * math.sin(angle)
            screen.set_at((int(x), int(y)), (0,0,0))
        pygame.display.flip()

contador=1
while (contador<=3):
    print("EXPLOSION " ,contador)
    radio2 = (random.choice((199,299,399)))
    posx2 = (random.choice((200,300,400)))
    posy2 = (random.choice((250,350,550)))
    explotar(posx2,posy2,radio2)
    print("Posicion X: ", posx2)
    print("Posicion Y: ", posy2)
    print("Radio: ", radio2)
    contador=contador+1

# INCISO B - FUNCIONA CORRECTAMENTE
def secuencia_explosiones():
    screen = pygame.display.set_mode((800, 800))
    particles = [(random.gauss(0,.5), random.uniform(10,10)) for i in range(2000)]
    for i in range(399):
        screen.fill((255,255,255))
        for speed, angle in particles:
            distance = i * speed
            x = 400 + distance * math.cos(angle)
            y = 400 + distance * math.sin(angle)
            screen.set_at((int(x), int(y)), (0,0,0))
        pygame.display.flip()

secuencia_explosiones()

#INCISO C -.
if len(sys.argv) > 1:
    explosiones = (sys.argv[1])
else:
    explosiones = 5
explosiones = int(explosiones)
contador2=1
while (contador2<=explosiones):
    radio = (random.choice((199,299,399)))
    posx = (random.choice((200,300,400)))
    posy = (random.choice((250,350,550)))
    for i in range(radio):
        screen.fill((255,255,255))
        for speed, angle in particles:
            distance = i * speed
            x = posx + distance * math.cos(angle)
            y = posy + distance * math.sin(angle)
            screen.set_at((int(x), int(y)), (0,0,0))
        pygame.display.flip()
    contador2=contador2+1
