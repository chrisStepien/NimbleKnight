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

# Skeleton
def import_enemy_1(path):
    
    enemy_1_animations = []
    
    for assetname in os.listdir(path):
        frame_path = path + '/' + assetname
        frame = pygame.image.load(frame_path).convert_alpha()
        enemy_1_animations.append(frame)    
               
    return enemy_1_animations

# Necromancer (Coming soon!)    
def import_enemy_2(path):
    
    enemy_2_animations = []
    
    for assetname in os.listdir(path):
        frame_path = path + '/' + assetname
        frame = pygame.image.load(frame_path).convert_alpha()
        enemy_2_animations.append(frame)    
               
    return enemy_2_animations 

# Mage
def import_npc(path):
    
    npc_animation = []
    
    for assetname in os.listdir(path):
        frame_path = path + '/' + assetname
        frame = pygame.image.load(frame_path).convert_alpha()
        npc_animation.append(frame)    
               
    return npc_animation

# Demon Slime
def import_boss(path):
    
    boss_animations = []
    
    for assetname in os.listdir(path):
        frame_path = path + '/' + assetname
        frame = pygame.image.load(frame_path).convert_alpha()
        boss_animations.append(frame)
    
    return boss_animations

# Additional attacks for Boss
def import_fire_column(path):
    
    column_animations = []
    
    for assetname in os.listdir(path):
        frame_path = path + '/' + assetname
        frame = pygame.image.load(frame_path).convert_alpha()
        column_animations.append(frame)
    
    return column_animations         

# Additional attacks for Boss
def import_fire_ball(path):
    
    ball_animations = []
    
    for assetname in os.listdir(path):
        frame_path = path + '/' + assetname
        frame = pygame.image.load(frame_path).convert_alpha()
        ball_animations.append(frame)
    
    return ball_animations  