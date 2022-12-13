import os
import pygame

def import_tiles(path):
        
    frame = pygame.image.load(path).convert_alpha()   
               
    return frame
  
def import_player_animations(path):
    
    player_animations = []

    for assetname in os.listdir(path):
        frame_path = path + '/' + assetname
        frame = pygame.image.load(frame_path).convert_alpha()
        player_animations.append(frame)    
               
    return player_animations      

def import_enemy_1(path):
    
    enemy_1_animations = []
    
    for assetname in os.listdir(path):
        frame_path = path + '/' + assetname
        frame = pygame.image.load(frame_path).convert_alpha()
        enemy_1_animations.append(frame)    
               
    return enemy_1_animations
    
def import_enemy_2(path):
    
    enemy_2_animations = []
    
    for assetname in os.listdir(path):
        frame_path = path + '/' + assetname
        frame = pygame.image.load(frame_path).convert_alpha()
        enemy_2_animations.append(frame)    
               
    return enemy_2_animations 

def import_npc(path):
    
    npc_animation = []
    
    for assetname in os.listdir(path):
        frame_path = path + '/' + assetname
        frame = pygame.image.load(frame_path).convert_alpha()
        npc_animation.append(frame)    
               
    return npc_animation
            
#import enemies and randomize

#import boss 