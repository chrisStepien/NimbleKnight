import pygame
from import_assets import import_npc

class NPC(pygame.sprite.Sprite):
    def __init__(self, pos):
        
        super().__init__()
        self.import_npc_assets()

        self.frame_index = 0
        self.frame_speed = 0.2
        
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

    def import_npc_assets(self):
        self.animations = {'idle': []}
        
        for animation in self.animations.keys():
            
            self.default_path = './assets/npc/'
            self.default_path += animation
            self.animations[animation] = import_npc(self.default_path)    
    
    
    def animate(self):
        
        self.frame_index += self.frame_speed 
        
        if self.frame_index > len(self.animations['idle']) - 1:
            
            self.frame_index = 0
        
        self.image = self.animations['idle'][int(self.frame_index)]
        self.rect = self.image.get_rect(topleft=self.rect.topleft)
    
    #PRINT WORDING ABOVE HEAD OR SOMETHING
    #PLEASE SAVE THIS CASTLE FROM THE DEMON LORD
    
    
    def update(self, offset):
        self.rect.x += offset.x
        self.animate()             