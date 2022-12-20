import pygame, sys
from level_settings import *
from level import Level
from background import *
from player import * 

# General setup
pygame.init()


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Nimble Knight")

Background = Background('./assets/background/background.png', (0,0), (screen_width, screen_height))
clock = pygame.time.Clock()
fps = 20
game_state = None
#Init Main Menu Components
background = pygame.image.load('./assets/background/background.png')
main_font = pygame.font.Font('./fonts/Square.ttf', 75)
second_font = pygame.font.Font('./fonts/Square.ttf', 50)
main_text = "NIMBLE KNIGHT"
second_text = "(1) Normal (2) Hard (3) Impossible"

#Welcome Screen
menuRunning = True
screen.fill((0, 0, 0))
screen.blit(Background.image, Background.rect)

#Nimble Knight Title
main_text_display = main_font.render(main_text, True, (255, 255, 255))
text_rect = main_text_display.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
screen.blit(main_text_display, text_rect)

#Instruction Text
second_main_text_display = second_font.render(second_text, True, (255, 255, 255))
text_rect2 = second_main_text_display.get_rect(center=(screen.get_width()/2, screen.get_height()/2 + 55))
screen.blit(second_main_text_display, text_rect2)


pygame.display.update()
while menuRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                menuRunning = False
                game_state = 1    
            if event.key == pygame.K_2:
                menuRunning = False
                game_state = 2    
            if event.key == pygame.K_3:
                menuRunning = False
                game_state = 3                           
            


while True:
    screen.fill((0, 0, 0))

    main_text = "Loading..."
    second_text = "Get Ready!"

    main_text_display = main_font.render(main_text, True, (255, 255, 255))
    text_rect = main_text_display.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
    screen.blit(main_text_display, text_rect)

    second_main_text_display = second_font.render(second_text, True, (255, 255, 255))
    text_rect2 = second_main_text_display.get_rect(center=(screen.get_width()/2, screen.get_height()/2 + 55))
    screen.blit(second_main_text_display, text_rect2)
    
    pygame.display.update()
       
    level = Level(level_map, screen, game_state)
    attacking = False
    playing = True
    quit_game = False
    
    time_difference = pygame.time.get_ticks()
    
    while playing:
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or quit_game == True:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT:
                    attacking = True
                else:
                    attacking = False  
                if event.key == pygame.K_SPACE and game_over_flag:
                    playing = False
                if event.key == pygame.K_ESCAPE and game_over_flag:
                    pygame.quit()
                    sys.exit()  
                
        screen.fill('black')
        screen.blit(Background.image, Background.rect)
    
        time = pygame.time.get_ticks() - time_difference
        data = level.run(attacking, time)
        game_over_flag = data[3]
        attacking = False

        pygame.display.update()
        
        clock.tick(fps)        
