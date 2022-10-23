import pygame, sys
from level_settings import *
from level import Level 

# General setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()


level = Level(level_map, screen)
key_pressed = False
key_up = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            #add all attacks to this
            #Fix roll that makes it go far
            if event.key == pygame.K_e:
                key_pressed = True
            
            elif event.key == pygame.K_w:
                
                key_pressed = True
            else:
                key_pressed = False
            
            key_up = False
                    
        if event.type == pygame.KEYUP:
            
            key_up = True
            
              
    screen.fill('white')
    level.run(key_pressed)
    pygame.display.update()
    clock.tick(15)        
