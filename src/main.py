import pygame, sys
from level_settings import *
from level import Level
from background import *
from player import * 

# General setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
Background = Background('./assets/background/background.png', (0,0), (screen_width, screen_height))
clock = pygame.time.Clock()
fps = 10

level = Level(level_map, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  
              
    screen.fill('black')
    screen.blit(Background.image, Background.rect)
    level.run()

    pygame.display.update()
    
    clock.tick(fps)        
