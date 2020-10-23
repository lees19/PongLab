import pygame

class Ball: 
    # pass
    #class variables
    RADIUS = 10

    def __init__(self, x, y,vx, vy, screen, fgcolor, bgcolor, BORDER, HEIGHT, WIDTH): 
        #instance variables
        self.x = x
        self.y = y 
        self.vx = vx
        self.vy = vy
        self.screen = screen
        self.fgcolor = fgcolor
        self.bgcolor = bgcolor
        self.BORDER = BORDER
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH

    def show(self, color): 
        pygame.draw.circle(self.screen, color, (self.x, self.y), self.RADIUS)

    def update(self): 
        #np = np+dp
        #delete old ball
        self.show(self.bgcolor)
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(self.fgcolor)

        #check if i'm colliding with wall
            #flip the velocity
        if self.x == (self.BORDER + Ball.RADIUS): 
            self.vx = -self.vx
        if self.y == (self.BORDER + self.RADIUS): 
            self.vy = -self.vy
        if self.y == (self.HEIGHT - self.BORDER - self.RADIUS): 
            self.vy = -self.vy
        # pass