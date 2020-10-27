import pygame
import numpy as np
import random as rand
from paddle import Paddle
from ball import Ball

def main(): 
    pygame.init() 
    pygame.display.set_caption("my pong")

    WIDTH = 800
    HEIGHT = 400
    BORDER = 20
    VELOCITY = 5
    FPS = 30
    #surface 
    #NOT A MATRIX, WIDTH FIRST, HEIGHT SECOND
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    screen.fill((0, 0, 0))

    #double buffering: stage updates togeher; update them at once
    #avoids flickering
    pygame.display.update()

    #walls
    #Rect(surface, color, rect)
    #Rect((left, top), (width, height)) 
    fgcolor = pygame.Color("white")
    bgcolor = pygame.Color("black")

    #top wall 
    pygame.draw.rect(screen, fgcolor, pygame.Rect((0, 0), (WIDTH, BORDER)))

    #left wall
    pygame.draw.rect(screen, fgcolor, pygame.Rect((0, 0), (BORDER, HEIGHT)))

    #bottom wall
    pygame.draw.rect(screen, fgcolor, pygame.Rect((0, HEIGHT-BORDER), (WIDTH, BORDER)))

    #Ball init
    x0 = WIDTH - Ball.RADIUS
    y0 = HEIGHT//2 

    #+/- 45degree random
    randInit = rand.random()
    if (randInit < (1/3)): 
        vx0 = -VELOCITY
        vy0 = VELOCITY
    elif ((randInit >= (1/3)) & (randInit < (2/3))): 
        vx0 = -VELOCITY
        vy0 = 0
    else: 
        vx0 = -VELOCITY
        vy0 = -VELOCITY

    b0 = Ball(x0, y0, vx0, vy0, screen, fgcolor, bgcolor, BORDER, HEIGHT, WIDTH)
    b0.show(fgcolor)

    pygame.display.update()

    # define a variable to control the main loop
    running = True
    clock = pygame.time.Clock()

    #delay so i can actually record it. 3 sec delay
    #pygame.time.wait(3000)

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        pygame.display.update()
        clock.tick(FPS)
        #ball
        b0.update()
    
if __name__ == "__main__": 
    main()

#push lab3.py to git + capture a gif and include in README.md