import os
import pygame

def import_player_animations(path):
    
    player_animation_list = []
    print(path)

    for imagename in os.listdir(path):
        frame_path = path + '/' + imagename
        frame = pygame.image.load(frame_path).convert_alpha()
        player_animation_list.append(frame)    
               
    return player_animation_list       

def import_tiles(path):
    
    tile_list = []
 
    frame = pygame.image.load(path).convert_alpha()
    tile_list.append(frame)    
               
    return tile_list   