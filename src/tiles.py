import pygame
from import_assets import import_tiles

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,size,tile):
        super().__init__()
        self.import_tile_assets()
        self.frame_index = 0
        self.image = self.tiles['_']
        self.rect = self.image.get_rect(topleft = pos)
        self.generate_tile(tile, pos)
    
        
        
    def update(self,offset):
        self.rect.x += offset.x
        self.rect.y += offset.y    
        
    def import_tile_assets(self):
        self.tiles = {'_': [], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': []}
        
        for tile in self.tiles.keys():

            self.default_path = './images/tiles/'
            self.default_path += tile
            self.default_path += ".png"
            self.tiles[tile] = import_tiles(self.default_path)
    #create tiles that dont have collision prob done in level.py
    def generate_tile(self, tile, pos):
        
        if(tile == 'X'):
            
            
            self.image = self.tiles['B']
            
            self.rect = self.image.get_rect(topleft = pos)
            
            
            
        if(tile == 'D'):
            
            self.image = self.tiles['B']
            self.rect = self.image.get_rect(topleft = pos)
        if(tile == 'F'):
        
            self.image = self.tiles['_']
            self.rect = self.image.get_rect(topleft = pos)

           # self.rect.height = self.rect.height - 5
        if(tile == 'S'):   
            
            self.image = self.tiles['stairs1']
            self.rect = self.image.get_rect(topleft = pos)
        if(tile == 'B'):
            
            self.image = self.tiles['brick1']
            self.rect = self.image.get_rect(topleft = pos)
        if(tile == '1'):
            
            self.image = self.tiles['1']
            self.rect = self.image.get_rect(topleft = pos)
        if(tile == '2'):
            
            self.image = self.tiles['2']
            self.rect = self.image.get_rect(topleft = pos)
        if(tile == '3'):
            
            self.image = self.tiles['3']
            self.rect = self.image.get_rect(topleft = pos)
        if(tile == '4'):
            
            self.image = self.tiles['4']
            self.rect = self.image.get_rect(topleft = pos)
        if(tile == '5'):                    
                    
            self.image = self.tiles['5']
            # image = self.tiles['5'][self.frame_index]
            # flipped_image = pygame.transform.flip(image, False, False)
            # self.image = flipped_image
            self.rect = self.image.get_rect(topleft = pos)
            #self.rect.width = 32     
        if(tile == '6'):
        
            self.image = self.tiles['6']
            self.rect = self.image.get_rect(topleft = pos)
        if(tile == '7'):
        
            self.image = self.tiles['7']
            # image = self.tiles['7'][self.frame_index]
            # flipped_image = pygame.transform.flip(image, False, False)
            # self.image = flipped_image
            self.rect = self.image.get_rect(topleft = pos)

            
        
        
        #self.image = self.tiles['attack_1'][self.frame_index]
        #self.rect = self.image.get_rect(topleft = )            