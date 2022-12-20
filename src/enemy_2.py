import pygame
from import_assets import import_enemy_2

#WORK IN PROGRESS
class Enemy_2(pygame.sprite.Sprite):
    def __init__(self, pos):
        
        super().__init__()
        self.import_enemy_2_assets()
        
        self.consume_frame_index = 0
        self.death_frame_index = 0
        self.hurt_frame_index = 0
        self.idle_frame_index = 0
        self.move_frame_index = 0
        self.summon_frame_index = 0
        
        self.frame_speed = 0.2
        
        self.image = self.animations['idle'][self.idle_frame_index]
        self.rect = self.image.get_rect(topleft=pos)        
    
    def import_enemy_2_assets(self):
        
        self.animations = {'consume': [], 'death': [], 'hurt': [], 'idle': [], 'move': [], 'summon': []}    
        
        for animation in self.animations.keys():
            
            self.default_path = './assets/enemies/necromancer/'
            self.default_path += animation
            self.animations[animation] = import_enemy_2(self.default_path)
            
    def animate(self):
        return  