import pygame,sys
import numpy as np
from pygame.locals import *

pygame.init()
pygame.display.init()

#screen
screen = pygame.display.set_mode((800,600)) 
pygame.display.set_caption('Snake Game')

#snake
x = 400
y = 400
w,h = (30,30)
vel = 10
green = (0,255,0)

#food
red = (255,0,0)
xloc = random.randrange(0, 800,20)
random_y = np.random.randint(0,600,1)
print(xloc)
while True:
    pygame.time.delay(25)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() 
            sys.exit()
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    
    if keys[pygame.K_RIGHT] and x < 800-w:
        x += vel

    if keys[pygame.K_UP] and y > 0:
        y -= vel
    
    if keys[pygame.K_DOWN] and y < 600-h:
        y += vel
    screen.fill((0,0,0))
    snake = pygame.draw.rect(screen,green,(x,y,w,h))
    food = pygame.draw.rect(screen,red,(xloc,100, w, h))
    pygame.display.update()
   