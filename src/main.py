import pygame, sys
from level_settings import *
from level import Level
from background import *
from player import * 

# General setup
pygame.init()

#Init Required Pygame Variables
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
fps = 20
game_state = None
pygame.display.set_caption("Nimble Knight")
Background = Background((0,0), (screen_width, screen_height))

#Init Main Menu Components
background = pygame.image.load('./assets/background/background.png')
main_font = pygame.font.Font('./fonts/RINGM___.TTF', 70)
second_font = pygame.font.Font('./fonts/RINGM___.TTF', 40)
main_text = "Nimble Knight"
normal_text = "(1) Normal"
hard_text = "(2) Hard"
impossible_text = "(3) Impossible"

#Welcome Screen
menuRunning = True
screen.fill((0, 0, 0))
screen.blit(Background.image, Background.rect)

# Sound
#Menu Music
pygame.mixer.music.load("./media/menu_music.mp3")
pygame.mixer.music.play(-1)

#Select
select = pygame.mixer.Sound("./media/select.wav")


#Nimble Knight Title
main_text_display = main_font.render(main_text, True, (0, 0, 0))
text_rect = main_text_display.get_rect(center=(screen.get_width()/2, screen.get_height()/2 - 160))
screen.blit(main_text_display, text_rect)

#Normal Difficulty Text
normal_text_display = second_font.render(normal_text, True, (255, 255, 255))
text_rect2 = normal_text_display.get_rect(center=(screen.get_width()/2 - 250, screen.get_height()/2 - 50))
screen.blit(normal_text_display, text_rect2)

#Hard Difficulty Text
hard_text_display = second_font.render(hard_text, True, (229, 149, 0))
text_rect3 = hard_text_display.get_rect(center=(screen.get_width()/2 - 10, screen.get_height()/2 - 50))
screen.blit(hard_text_display, text_rect3)

#Impossible Difficulty Text
impossible_text_display = second_font.render(impossible_text, True, (136, 8, 8))
text_rect4 = impossible_text_display.get_rect(center=(screen.get_width()/2 + 250, screen.get_height()/2 - 50))
screen.blit(impossible_text_display, text_rect4)

pygame.display.update()

#Start Screen Loop
while menuRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                select.play()
                menuRunning = False
                game_state = 1    
            if event.key == pygame.K_2:
                select.play()
                menuRunning = False
                game_state = 2    
            if event.key == pygame.K_3:
                select.play()
                menuRunning = False
                game_state = 3                           

#Restart Game Loop            
while True:
    
    #Loading Screen
    screen.fill((0, 0, 0))
    main_text = "Loading..."
    second_text = "Get Ready!"
    main_text_display = main_font.render(main_text, True, (255, 255, 255))
    text_rect = main_text_display.get_rect(center=(screen.get_width()/2, screen.get_height()/2 - 50))
    screen.blit(main_text_display, text_rect)
    second_main_text_display = second_font.render(second_text, True, (136, 8, 8))
    text_rect2 = second_main_text_display.get_rect(center=(screen.get_width()/2, screen.get_height()/2 + 30))
    screen.blit(second_main_text_display, text_rect2)
    pygame.display.update()
    
    #Start Level   
    level = Level(level_map, screen, game_state)
    attacking = False
    playing = True
    quit_game = False
    
    #Game Music
    pygame.mixer.music.load("./media/background_music.mp3")
    pygame.mixer.music.play(-1)
    
    #Main Game Loop    
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
                # Restart Game      
                if event.key == pygame.K_SPACE and game_over_flag:
                    select.play()
                    playing = False
                # Exit Game    
                if event.key == pygame.K_ESCAPE and game_over_flag:
                    pygame.quit()
                    sys.exit()  
        
        #Background        
        screen.fill('black')
        screen.blit(Background.image, Background.rect)
        
        #Check status of game
        data = level.run(attacking)
        game_over_flag = data[3]
        
        #Reset attack
        attacking = False

        pygame.display.update()
        clock.tick(fps)        
