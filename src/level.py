import pygame
from level_settings import tile_size, screen_width
from tiles import Tile
from player import Player

# iterate through level_map 

class Level:
    def __init__(self,level_layout_data,surface):
        super().__init__()
    
        self.display_surface = surface
        self.setup_level(level_layout_data)
        self.world_shift = 0
        self.current_x = 0   
            
    def setup_level(self,level_layout):
        
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        
        for row_index, row in enumerate(level_layout):
            for col_index, cell in enumerate(row):
                
                x = col_index * tile_size
                y = row_index * tile_size
                
                if cell == 'X':
                    
                    tile = Tile((x,y), tile_size)
                    self.tiles.add(tile)
                
                if cell == 'P':
                
                    player_sprite = Player((x,y)) 
                    self.player.add(player_sprite)
               # if cell == 'E':        
    
    # Player Camera
    #Fix climbing walls
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        
        if player_x < screen_width / 5 and direction_x < 0:
            
            self.world_shift = 8
            player.speed = 0
            
        elif player_x > screen_width / 2 and direction_x > 0:
            
            self.world_shift = -8
            player.speed = 0
            
        else:
            
            self.world_shift = 0
            player.speed = 8
    
    
    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed          
    
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.wall_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.wall_right = True
                    self.current_x = player.rect.right    

        #            
        if(player.wall_left and player.rect.left < self.current_x or player.direction.x >= 0):
            player.wall_left = False 
        #                 
        if(player.wall_right and player.rect.right > self.current_x or player.direction.x <= 0):
            player.wall_right = False
        
        
        
    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
       
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom 
                    player.direction.y = 0
                    player.on_ceiling = True
        
        #            
        if(player.on_ground and player.direction.y < 0 or player.direction.y > 1):
            player.on_ground = False
        #                 
        if(player.on_ceiling and player.direction.y > 0):
            player.on_ceiling = False            
                    
    def run(self, single_press):
        BLUE = (0,0,255)
        player = self.player.sprite
        #print(player.rect[0])
        #print(int(player.rect[1]))
        #Change to hit_box rect?
        pygame.draw.rect(self.display_surface, BLUE, (int(player.hit_box[0]), int(player.hit_box[1]), 80, 20))
        # Level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()
        
        
        
        # Player 
        self.player.update(single_press)
        self.vertical_movement_collision()
        self.horizontal_movement_collision()
        self.player.draw(self.display_surface)
        