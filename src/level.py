import pygame, sys
from level_settings import tile_size, screen_width, screen_height
from tiles import Tile
from player import Player
from npc import NPC
from enemy_1 import Enemy_1
from enemy_2 import Enemy_2

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
        
        
        #collidable
        self.hard_tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.necromancer = pygame.sprite.GroupSingle()
        self.skeletons = pygame.sprite.Group()
        #Figure out how to use this
        self.summoned_skeletons = pygame.sprite.Group()
        
        #non collidable
        self.soft_tiles = pygame.sprite.Group()
        self.npc = pygame.sprite.GroupSingle()
        
        
        for row_index, row in enumerate(level_layout):
            for col_index, cell in enumerate(row):
                
                x = col_index * tile_size
                y = row_index * tile_size
            
                #maybe ( and ) but only if decreasing size of rect stairs needs that
                #Why tile_size exist?
                #Hard tiles
                if cell == '-':
                
                    tile = Tile((x, y), tile_size, '-')
                    self.hard_tiles.add(tile)
                    
                if cell == '[':
                
                    tile = Tile((x, y), tile_size, '[')
                    self.hard_tiles.add(tile)
                
                if cell == ']':
                    
                    tile = Tile((x, y), tile_size, ']')
                    self.hard_tiles.add(tile)
                    
                if cell == '_':
                        
                    tile = Tile((x, y), tile_size, '_')
                    self.hard_tiles.add(tile)
                            
                if cell == '{':
                    
                    tile = Tile((x, y), tile_size, '{')
                    self.hard_tiles.add(tile)
                    
                if cell == '}':    
                    
                    tile = Tile((x, y), tile_size, '}')
                    self.hard_tiles.add(tile)
                    
                if cell == '/':
                    
                    tile = Tile((x, y), tile_size, '/')
                    self.hard_tiles.add(tile)
                    
                if cell == '|':    
                    
                    tile = Tile((x, y), tile_size, '|')
                    self.hard_tiles.add(tile)
                    
                if cell == ':':
                    
                    tile = Tile((x, y), tile_size, ':')
                    self.hard_tiles.add(tile)
                
                if cell == '<':
                    
                    tile = Tile((x, y), tile_size, '<')
                    self.hard_tiles.add(tile)
                    
                if cell == '=':
                    
                    tile = Tile((x, y), tile_size, '=')
                    self.hard_tiles.add(tile)
                    
                if cell == '>':
                    
                    tile = Tile((x, y), tile_size, '>')
                    self.hard_tiles.add(tile)
                             
                if cell == '8':
                    
                    tile = Tile((x, y), tile_size, '8')
                    self.hard_tiles.add(tile)
                    
                if cell == '9':    
                    
                    tile = Tile((x, y), tile_size, '9')
                    self.hard_tiles.add(tile)
                
                if cell == 'D':
                    
                    tile = Tile((x, y), tile_size, 'D')
                    self.hard_tiles.add(tile)
                        
                if cell == 'U':
                    
                    tile = Tile((x, y), tile_size, 'U')
                    self.hard_tiles.add(tile)
                    
                if cell == 'P':
                
                    player_sprite = Player((x, y))
                  
                    #print(player_sprite.rect.centerx) 
                    self.player.add(player_sprite)
                  
                #NECROMANCER
                if cell == '*':
                    
                    necromancer = Enemy_2((x, y))
                    self.necromancer.add(necromancer)
                    
                #SKELETON
                
                if cell == 'E':
                    
                    skeleton = Enemy_1((x, y))
                    self.skeletons.add(skeleton)
                
                #SLIME BOSS
                # if cell == 'S':
                
                #Soft tiles
                if cell == '!':
                
                    tile = Tile((x, y), tile_size, '!')
                    self.soft_tiles.add(tile)
                    
                if cell == '#':
                
                    tile = Tile((x, y), tile_size, '#')
                    self.soft_tiles.add(tile)
                
                if cell == '$':
                    
                    tile = Tile((x, y), tile_size, '$')
                    self.soft_tiles.add(tile)
                    
                if cell == '%':
                        
                    tile = Tile((x, y), tile_size, '%')
                    self.soft_tiles.add(tile)
                            
                if cell == '&':
                    
                    tile = Tile((x, y), tile_size, '&')
                    self.soft_tiles.add(tile)
              
                if cell == '(':    
                    
                    tile = Tile((x, y), tile_size, '(')
                    self.soft_tiles.add(tile)
                    
                if cell == ')':
                    
                    tile = Tile((x, y), tile_size, ')')
                    self.soft_tiles.add(tile)
                    
                if cell == '@':    
                    
                    tile = Tile((x, y), tile_size, '@')
                    self.soft_tiles.add(tile)
                    
                if cell == '^':
                    
                    tile = Tile((x, y), tile_size, '^')
                    self.soft_tiles.add(tile)
                
                if cell == '~':
                    
                    tile = Tile((x, y), tile_size, '~')
                    self.soft_tiles.add(tile)
                    
                if cell == '0':
                    
                    tile = Tile((x, y), tile_size, '0')
                    self.soft_tiles.add(tile)
                    
                if cell == '1':
                    
                    tile = Tile((x, y), tile_size, '1')
                    self.soft_tiles.add(tile)
                
                if cell == '2':
                    
                    tile = Tile((x, y), tile_size, '2')
                    self.soft_tiles.add(tile)
                        
                if cell == '3':
                    
                    tile = Tile((x, y), tile_size, '3')
                    self.soft_tiles.add(tile)
                
                if cell == '4':
                
                    tile = Tile((x, y), tile_size, '4')
                    self.soft_tiles.add(tile)
                    
                if cell == '5':
                
                    tile = Tile((x, y), tile_size, '5')
                    self.soft_tiles.add(tile)
                
                if cell == '6':
                    
                    tile = Tile((x, y), tile_size, '6')
                    self.soft_tiles.add(tile)
                    
                if cell == '7':
                        
                    tile = Tile((x, y), tile_size, '7')
                    self.soft_tiles.add(tile)
               
                if cell == 'A':
                    
                    tile = Tile((x, y), tile_size, 'A')
                    self.soft_tiles.add(tile)
                    
                if cell == 'B':    
                    
                    tile = Tile((x, y), tile_size, 'B')
                    self.soft_tiles.add(tile)
                    
                if cell == 'C':
                    
                    tile = Tile((x, y), tile_size, 'C')
                    self.soft_tiles.add(tile)
                
                if cell == 'F':
                    
                    tile = Tile((x, y), tile_size, 'F')
                    self.soft_tiles.add(tile)
                    
                if cell == 'G':
                    
                    tile = Tile((x, y), tile_size, 'G')
                    self.soft_tiles.add(tile)
                    
                if cell == 'H':
                    
                    tile = Tile((x, y), tile_size, 'H')
                    self.soft_tiles.add(tile)
                
                if cell == 'I':
                    
                    tile = Tile((x, y), tile_size, 'I')
                    self.soft_tiles.add(tile)
                        
                if cell == 'J':
                    
                    tile = Tile((x, y), tile_size, 'J')
                    self.soft_tiles.add(tile)
                
                if cell == 'K':
                
                    tile = Tile((x, y), tile_size, 'K')
                    self.soft_tiles.add(tile)
                    
                if cell == 'L':
                
                    tile = Tile((x, y), tile_size, 'L')
                    self.soft_tiles.add(tile)
                
                if cell == 'M':
                    
                    tile = Tile((x, y), tile_size, 'M')
                    self.soft_tiles.add(tile)
                    
                if cell == 'N':
                        
                    tile = Tile((x, y), tile_size, 'N')
                    self.soft_tiles.add(tile)
                            
                if cell == 'O':
                    
                    tile = Tile((x, y), tile_size, 'O')
                    self.soft_tiles.add(tile)
                    
                if cell == 'Q':    
                    
                    tile = Tile((x, y), tile_size, 'Q')
                    self.soft_tiles.add(tile)
                    
                if cell == 'R':
                    
                    tile = Tile((x, y), tile_size, 'R')
                    self.soft_tiles.add(tile)
                    
                if cell == 'T':    
                    
                    tile = Tile((x, y), tile_size, 'T')
                    self.soft_tiles.add(tile)
                    
                if cell == 'V':
                    
                    tile = Tile((x, y), tile_size, 'V')
                    self.soft_tiles.add(tile)
                
                if cell == 'W':
                    
                    tile = Tile((x, y), tile_size, 'W')
                    self.soft_tiles.add(tile)
                    
                if cell == 'X':
                    
                    tile = Tile((x, y), tile_size, 'X')
                    self.soft_tiles.add(tile)
                    
                if cell == 'Y':
                    
                    tile = Tile((x, y), tile_size, 'Y')
                    self.soft_tiles.add(tile)
                
                if cell == 'Z':
                    
                    tile = Tile((x, y), tile_size, 'Z')
                    self.soft_tiles.add(tile)

                #NPC
                if cell == '?':
                    
                    npc_sprite = NPC((x, y))
                    self.npc.add(npc_sprite)                                                
    
    def player_camera(self, sprite):
       
       self.offset.x += sprite.rect.centerx - self.half_width 
       self.offset.y += sprite.rect.centery - self.half_height 
                            
                
    # Player Camera
    #Fix climbing walls
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        
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
        player.env_rect.x += player.direction.x * player.speed          
        print("CHECK 1")
        
        for sprite in self.hard_tiles.sprites():
            
            if sprite.rect.colliderect(player.env_rect) and sprite.id == 'U':
                player.player_status['death'] == True
            #if sprite.rect.colliderect(player.rect) and sprite
            
            
            if sprite.rect.colliderect(player.env_rect):
                
                #issue with camera may be caused here
                if player.direction.x < 0:
                    
                    player.env_rect.left = sprite.rect.right
                    player.rect.left = player.env_rect.left - 2
                    player.wall_left = True
                    self.current_x = player.env_rect.left
                elif player.direction.x > 0:
                    
                    
                    player.env_rect.right = sprite.rect.left
                    player.rect.right = player.env_rect.right + 2
                    player.wall_right = True
                    self.current_x = player.env_rect.right    
                    
                    
                    #           
         
        if(player.wall_left and player.env_rect.left < self.current_x or player.direction.x >= 0):
            player.wall_left = False 
        #                 
        if(player.wall_right and player.env_rect.right > self.current_x or player.direction.x <= 0):
            player.wall_right = False
        
        #self.player.update(False)
       
        
        
    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
       
        for sprite in self.hard_tiles.sprites():
            if sprite.rect.colliderect(player.env_rect) and sprite.id == 'U':
                player.player_status['death'] == True
            if sprite.rect.colliderect(player.env_rect):
                if player.direction.y > 0:
                    player.env_rect.bottom = sprite.rect.top
                    player.rect.bottom = player.env_rect.bottom + 2
                    
                    player.direction.y = 0
                    player.on_ground = True
                    self.current_y = player.env_rect.top
                elif player.direction.y < 0:
                    player.env_rect.top = sprite.rect.bottom
                    player.rect.top = player.env_rect.top
                     
                    player.direction.y = 0
                    player.on_ceiling = True
                    self.current_y = player.env_rect.bottom
                    
        #            
        if(player.on_ground and player.direction.y < 0 or player.direction.y > 1):
            player.on_ground = False
        #                 
        if(player.on_ceiling and player.direction.y > 0):
            player.on_ceiling = False            
                    
    def run(self, single_press):
        
        player = self.player.sprite
        npc = self.npc.sprite
        skeletons = self.skeletons.sprites
        summoned_skeletons = self.summoned_skeletons.sprites
        necromancer = self.necromancer.sprite
        
        # Level tiles
        self.hard_tiles.update(self.offset)
        self.hard_tiles.draw(self.display_surface)
        
        #self.display_surface.blit(self.tiles)
        #self.scroll_y()
        self.scroll_x()
        
        # Player 
        self.player.update(single_press)
        self.vertical_movement_collision()
        self.horizontal_movement_collision()
        self.scroll_x()
        self.player.draw(self.display_surface)
        
        #NPC
        self.npc.update(self.offset)
        self.npc.draw(self.display_surface)
        
        #Skeletons
        #MIGHT SCREW UP STUFF
        self.skeletons.update(player)
        self.skeletons.draw(self.display_surface)
        
        #SummonedSkeletons?
        
        #Necromancer
        
              
        return player, npc, skeletons, summoned_skeletons, necromancer