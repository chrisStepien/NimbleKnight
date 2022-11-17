import pygame, sys
from level_settings import tile_size, screen_width, screen_height
from tiles import Tile
from player import Player

# iterate through level_map 

class Level:
    def __init__(self,level_layout_data,surface):
        super().__init__()
        
        self.display_surface = surface
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
        
        #player = self.player.sprite
        self.current_x = 0 
        self.current_y = 0  
        #self.offset.x = self.half_width - player.rect.centerx 
        #self.offset.y = self.half_height - player.rect.centery 
        
        self.setup_level(level_layout_data)
        #self.scroll_x()
        
        #similar to below
        #self.x_shift = 0
        #self.y_shift = 0
    
        
            
    def setup_level(self,level_layout):
        
        #Backgound path
        
        
        
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        
        
        
        
        for row_index, row in enumerate(level_layout):
            for col_index, cell in enumerate(row):
                
                x = col_index * tile_size
                y = row_index * tile_size
            
                
                if cell == 'P':
                
                    player_sprite = Player((x, y))
                    print("x = ")
                    print(x)
                    print("y = ")
                    print(y)
                    #print(player_sprite.rect.centerx) 
                    self.player.add(player_sprite)
                    
                if cell == 'X':
                    
                    tile = Tile((x, y), tile_size, 'X')
                    self.tiles.add(tile)
                
                
            #    # if cell == 'E':        
            #     if cell == 'D':
                    
            #         tile = Tile((x, y), tile_size, 'D')
            #         self.tiles.add(tile)
                
            #     if cell == 'C':
                    
            #         tile = Tile((x, y), tile_size, cell)
            #         self.tiles.add(tile)
                
                    
                if cell == 'F':
                    
                    tile = Tile((x, y), tile_size, 'F')
                    self.tiles.add(tile)
                    
            #     if cell == 'B':
                
            #         tile = Tile((x, y), tile_size, 'B')
            #         self.tiles.add(tile)
                
            #     if cell == 'S':
                
            #         tile = Tile((x, y), tile_size, 'S')
            #         self.tiles.add(tile)
                    
                if cell == '1':
                    
                    tile = Tile((x, y), tile_size, '1')
                    self.tiles.add(tile)
                    
                    
                if cell == '2':
                
                    tile = Tile((x, y), tile_size, '2')
                    self.tiles.add(tile)
                
                if cell == '3':               
                
                     tile = Tile((x, y), tile_size, '3')
                     self.tiles.add(tile)
                    
                if cell == '4':               

                    tile = Tile((x, y), tile_size, '4')
                    self.tiles.add(tile)
                         
                if cell == '5':                
                    tile = Tile((x, y), tile_size, '5')
                    self.tiles.add(tile)
                     
                if cell == '6':               
                    tile = Tile((x, y), tile_size, '6')
                    self.tiles.add(tile)
                     
                if cell == '7':               
                    tile = Tile((x, y), tile_size, '7')
                    self.tiles.add(tile)
                                
    
    def player_camera(self, sprite):
       
       self.offset.x += sprite.rect.centerx - self.half_width 
       self.offset.y += sprite.rect.centery - self.half_height 
                            
                
    # Player Camera
    #Fix climbing walls
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        print("Wall:")
        print(player.wall_right)
        if player_x < tile_size * 1 and direction_x < 0 and player.wall_right == False:
            
            self.offset.x = 8
            player.speed = 0
            
        elif player_x > tile_size * 21  and direction_x > 0 and player.wall_right == False:
            
            self.offset.x = -8
            player.speed = 0
            
        else:
            
            self.offset.x = 0
            player.speed = 8
    
    def scroll_y(self):
        player = self.player.sprite
        player_y = player.rect.centery
        direction_y = player.direction.y
        
        print(direction_y)
        
        if player_y < screen_height / 2 and direction_y < 0 :
            
            self.y_shift += 0.5
            player.speed = 0
            
        elif player_y > screen_height / 2 and direction_y < 0:
            
            self.y_shift += -0.5
            player.speed = 0
            
        else:
            
            self.y_shift = 0
            player.speed = 0.5
    
    
    
    def horizontal_movement_collision(self):
        
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed          
        print(player.direction.x)
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                
                #issue with camera may be caused here
                if player.direction.x < 0:
                    print('hello')
                    player.rect.left = sprite.rect.right
                    player.wall_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    print('hello')
                    
                    player.rect.right = sprite.rect.left
                    player.wall_right = True
                    self.current_x = player.rect.right    
                    print("wall right: " + str(player.wall_right))
                    
                    #           
         
        if(player.wall_left and player.rect.left < self.current_x or player.direction.x >= 0):
            player.wall_left = False 
        #                 
        if(player.wall_right and player.rect.right > self.current_x or player.direction.x <= 0):
            player.wall_right = False
        
        #self.player.update(False)
        print("player wall:" + str(player.wall_right))
        
        
    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
       
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                    self.current_y = player.rect.top
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom 
                    player.direction.y = 0
                    player.on_ceiling = True
                    self.current_y = player.rect.bottom
                    
        
        #            
        if(player.on_ground and player.direction.y < 0 or player.direction.y > 1):
            player.on_ground = False
        #                 
        if(player.on_ceiling and player.direction.y > 0):
            player.on_ceiling = False            
                    
    def run(self, single_press):
        
        player = self.player.sprite
        #print(player.rect[0])
        #print(int(player.rect[1]))
        #Change to hit_box rect?
       # pygame.draw.rect(self.display_surface, BLUE, (int(player.hit_box[0]), int(player.hit_box[1]), 80, 20))
        # Level tiles
        #self.player_camera(player)
        self.tiles.update(self.offset)
        self.tiles.draw(self.display_surface)
        
        #self.display_surface.blit(self.tiles)
        #self.scroll_y()
        self.scroll_x()
        
        # Player 
        self.player.update(single_press)
        self.vertical_movement_collision()
        self.horizontal_movement_collision()
        self.scroll_x()
        self.player.draw(self.display_surface)
        
        #if(player.wall_right == True):
         #   pygame.quit()
          #  sys.exit()
        print("player - right:" + str(player.wall_right))
        
    
        print(self.player.sprite.image)    
        print("what: " + str(player.rect))
              
        return player