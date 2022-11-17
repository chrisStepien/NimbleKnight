import os
import pygame

def import_player_animations(path):
    
    player_animation_list = []

    for assetname in os.listdir(path):
        frame_path = path + '/' + assetname
        frame = pygame.image.load(frame_path).convert_alpha()
        player_animation_list.append(frame)    
               
    return player_animation_list       

def import_tiles(path):
        
    frame = pygame.image.load(path).convert_alpha()   
               
    return frame  