import pygame
from import_assets import import_fire_column

class Fire_Column(pygame.sprite.Sprite):
    def __init__(self, pos):
        
        super().__init__()
        self.import_fire_column_assets()
        
        self.frame_index = 0
        self.frame_speed = 0.6
        
        self.image = self.animations['fire_column'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
    
    def import_fire_column_assets(self):
        
        self.animations = {'fire_column': []}
        
        for animation in self.animations.keys():
            
            self.default_path = './assets/'
            self.default_path += animation
            self.animations[animation] = import_fire_column(self.default_path)    
            
    
    def animate(self):
        
        self.frame_index += self.frame_speed
        
        if int(self.frame_index) > len(self.animations['fire_column']) - 1:

            self.frame_index = 0
        
        else:
            self.image = self.animations['fire_column'][int(self.frame_index)]
            self.rect = self.image.get_rect(topleft=self.rect.topleft)  
    
    def update(self):
        
        self.animate()        