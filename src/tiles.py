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
        #Some are named due to file naming conventions
        self.tiles = {'-': [], '[': [], ']': [], '_': [], '{': [], '}': [], 'D': [], 'U': [], 'ceiling_corner_L': [], 'ceiling_corner_R': [], 'ceiling_side': [], 'platform_L': [], 'platform_M': [], 'platform_R': []}
        self.soft_tiles = {'!': [], '#': [], '$': [], '%': [], '&': [], '(': [], ')': [], '@': [], '^': [], '~': [], '0': [], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [], 'A': [], 'B': [], 'C': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'Q': [], 'R': [], 'T': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}
        
        #Hard tiles import
        for tile in self.tiles.keys():

            self.default_path = './assets/tiles/hard_tiles/'
            self.default_path += tile
            self.default_path += ".png"
            self.tiles[tile] = import_tiles(self.default_path)
        
        #Soft tiles import    
        for tile in self.soft_tiles.keys():

            self.default_path = './assets/tiles/soft_tiles/'
            self.default_path += tile
            self.default_path += ".png"
            self.tiles[tile] = import_tiles(self.default_path)
        
    #Generates level tiles
    def generate_tile(self, tile, pos):
        
        #Hard tiles
        if(tile == '-'):
            
            self.image = self.tiles['-']
            self.rect = self.image.get_rect(topleft = pos)
      
        if(tile == '['):
            
            self.image = self.tiles['[']
            self.rect = self.image.get_rect(topleft = pos)
            
        if(tile == ']'):
        
            self.image = self.tiles[']']
            self.rect = self.image.get_rect(topleft = pos)

        if(tile == '_'):   
            
            self.image = self.tiles['_']
            self.rect = self.image.get_rect(topleft = pos)
            
        if(tile == '{'):
            
            self.image = self.tiles['{']
            self.rect = self.image.get_rect(topleft = pos)
            
        if(tile == '}'):
            
            self.image = self.tiles['}']
            self.rect = self.image.get_rect(topleft = pos)
            
        if(tile == '/'):
            
            self.image = self.tiles['ceiling_corner_L']
            self.rect = self.image.get_rect(topleft = pos)
            
        if(tile == '|'):
            
            self.image = self.tiles['ceiling_corner_R']
            self.rect = self.image.get_rect(topleft = pos)
            
        if(tile == ':'):
            
            self.image = self.tiles['ceiling_side']
            self.rect = self.image.get_rect(topleft = pos)
            
        if(tile == '<'):                    
                    
            self.image = self.tiles['platform_L']
            self.rect = self.image.get_rect(topleft = pos)
              
        if(tile == '='):
        
            self.image = self.tiles['platform_M']
            self.rect = self.image.get_rect(topleft = pos)
        
        if(tile == '>'):
        
            self.image = self.tiles['platform_R']
            self.rect = self.image.get_rect(topleft = pos)
            
        if(tile == 'D'):
        
            self.image = self.tiles['D']
            self.rect = self.image.get_rect(topleft = pos)

        if(tile == 'U'):
        
            self.image = self.tiles['U']
            self.rect = self.image.get_rect(topleft = pos)
        
        #Soft tiles
        if(tile == '!'):
            
            self.image = self.tiles['!']
            self.rect = self.image.get_rect(topleft = pos)
      
        if(tile == '#'):
            
            self.image = self.tiles['#']
            self.rect = self.image.get_rect(topleft = pos)
            
        if(tile == '$'):
        
            self.image = self.tiles['$']
            self.rect = self.image.get_rect(topleft = pos)

        if(tile == '%'):   
            
            self.image = self.tiles['%']
            self.rect = self.image.get_rect(topleft = pos)
            
        if(tile == '&'):
            
            self.image = self.tiles['&']
            self.rect = self.image.get_rect(topleft = pos)
            
        if(tile == '('):
            
            self.image = self.tiles['(']
            self.rect = self.image.get_rect(topleft = pos)
            
        if(tile == ')'):
            
            self.image = self.tiles[')']
            self.rect = self.image.get_rect(topleft = pos)
            
        if(tile == '@'):
            
            self.image = self.tiles['@']
            self.rect = self.image.get_rect(topleft = pos)
            
        if(tile == '^'):
            
            self.image = self.tiles['^']
            self.rect = self.image.get_rect(topleft = pos)
            
        if(tile == '~'):                    
                    
            self.image = self.tiles['~']
            self.rect = self.image.get_rect(topleft = pos)
              
        if(tile == '0'):
        
            self.image = self.tiles['0']
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
            self.rect = self.image.get_rect(topleft = pos)
        
        if(tile == '6'):
        
            self.image = self.tiles['6']
            self.rect = self.image.get_rect(topleft = pos)
            
        if(tile == '7'):
        
            self.image = self.tiles['7']
            self.rect = self.image.get_rect(topleft = pos)

        if(tile == '8'):
        
            self.image = self.tiles['8']
            self.rect = self.image.get_rect(topleft = pos)
        
        if(tile == '9'):                    
                    
            self.image = self.tiles['9']
            self.rect = self.image.get_rect(topleft = pos)
              
        if(tile == 'A'):
        
            self.image = self.tiles['A']
            self.rect = self.image.get_rect(topleft = pos)
        
        if(tile == 'B'):
        
            self.image = self.tiles['B']
            self.rect = self.image.get_rect(topleft = pos)
            
        if(tile == 'C'):
        
            self.image = self.tiles['C']
            self.rect = self.image.get_rect(topleft = pos)

        if(tile == 'F'):
        
            self.image = self.tiles['F']
            self.rect = self.image.get_rect(topleft = pos)              
        
        if(tile == 'G'):
        
            self.image = self.tiles['G']
            self.rect = self.image.get_rect(topleft = pos)
        
        if(tile == 'H'):                    
                    
            self.image = self.tiles['H']
            self.rect = self.image.get_rect(topleft = pos)
              
        if(tile == 'I'):
        
            self.image = self.tiles['I']
            self.rect = self.image.get_rect(topleft = pos)
        
        if(tile == 'J'):
        
            self.image = self.tiles['J']
            self.rect = self.image.get_rect(topleft = pos)
            
        if(tile == 'K'):
        
            self.image = self.tiles['K']
            self.rect = self.image.get_rect(topleft = pos)

        if(tile == 'L'):
        
            self.image = self.tiles['L']
            self.rect = self.image.get_rect(topleft = pos)       
        
        if(tile == 'M'):
        
            self.image = self.tiles['M']
            self.rect = self.image.get_rect(topleft = pos)
        
        if(tile == 'N'):                    
                    
            self.image = self.tiles['N']
            self.rect = self.image.get_rect(topleft = pos)
              
        if(tile == 'O'):
        
            self.image = self.tiles['O']
            self.rect = self.image.get_rect(topleft = pos)
        
        if(tile == 'Q'):
        
            self.image = self.tiles['Q']
            self.rect = self.image.get_rect(topleft = pos)
            
        if(tile == 'R'):
        
            self.image = self.tiles['R']
            self.rect = self.image.get_rect(topleft = pos)

        if(tile == 'T'):
        
            self.image = self.tiles['T']
            self.rect = self.image.get_rect(topleft = pos)       
        
        if(tile == 'V'):
        
            self.image = self.tiles['V']
            self.rect = self.image.get_rect(topleft = pos)
        
        if(tile == 'W'):                    
                    
            self.image = self.tiles['W']
            self.rect = self.image.get_rect(topleft = pos)
              
        if(tile == 'X'):
        
            self.image = self.tiles['X']
            self.rect = self.image.get_rect(topleft = pos)
        
        if(tile == 'Y'):
        
            self.image = self.tiles['Y']
            self.rect = self.image.get_rect(topleft = pos)
            
        if(tile == 'Z'):
        
            self.image = self.tiles['Z']
            self.rect = self.image.get_rect(topleft = pos)     