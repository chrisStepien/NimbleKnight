import pygame
from import_assets import import_enemy_1

class Enemy_1(pygame.sprite.Sprite):
    def __init__(self, pos):
        
        super().__init__()
        self.import_enemy_1_assets()
        
        self.attack_frame_index = 0
        self.death_frame_index = 0
        self.hurt_frame_index = 0
        self.idle_frame_index = 0
        self.react_frame_index = 0
        self.walk_frame_index = 0
        
        self.frame_speed = 0.2
        
        self.isAggro = False
        self.isAnimating = False
        
        
        self.image = self.animations['idle'][self.idle_frame_index]
        self.rect = self.image.get_rect(topleft=pos)        
    
    def import_enemy_1_assets(self):
        
        self.animations = {'attack': [], 'death': [], 'hurt': [], 'idle': [], 'react': [], 'walk': []}    
        
        for animation in self.animations.keys():
            
            self.default_path = './assets/enemies/skeleton/'
            self.default_path += animation
            self.animations[animation] = import_enemy_1(self.default_path)
    
    def calculate_distance(self, player): 
    
        skeleton_loc = self.rect.x
        player_loc = player.rect.x
    
        self.diff = skeleton_loc - player_loc
        print("Skel:" + str(skeleton_loc))
        print("player:" + str(player_loc))
        print("diff:" + str(self.diff))
        if self.diff < 50 or self.diff > -50:
            self.isAnimating = True
        
        if self.diff > 50 or self.diff < -50:
            self.isAnimating = False    
    def animate(self):
        
        if not self.isAnimating:
            return
        if self.isAnimating:
            
            self.idle_frame_index += self.frame_speed

            if int(self.idle_frame_index) > len(self.animations['idle']) - 1:

                self.idle_frame_index = 0

            self.image = self.animations['idle'][int(self.idle_frame_index)]
            self.rect = self.image.get_rect(topleft=self.rect.topleft)   
        
    def update(self, player):
        
        self.calculate_distance(player)
        self.animate()    