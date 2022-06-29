import pygame
from pygame import Vector2
from pygame.locals import *
import sys
import BGScrolling

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


'''
Create a BACKGROUND object with your display surface and image.
'''
bg = BGScrolling.BACKGROUND(screen, pygame.image.load("example-background-2.jpg"))


'''
There are three modes you can choose from.
    - Mode 1 will place buffers on the sides, 
    - Mode 2 will place buffers on the top and botton,
    - Mode 3 will place buffers on all 8 surrounding faces.

Set to Mode 1 by default, feel free to play around!
'''

bg.set_mode(3)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
            sys.exit()

    '''
    Move the background with the move() function
    The move funtion takes a Vector2 object as a parameter

    Alternativly, you can use the move_y() and move_x() functions as demonstrated below
    '''
    keys = pygame.key.get_pressed()
    if keys[K_w]:
        bg.move_y(30)
    if keys[K_s]:
        bg.move_y(-30)

    
    bg.update() # This repositions the background

    screen.fill((0,0,0))

    bg.draw() # Draws all the images
    

    pygame.display.update()
    clock.tick(30)