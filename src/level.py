import pygame
import json
from level_settings import tile_size, screen_width, screen_height
from tiles import Tile
from player import Player
from npc import NPC
from enemy_1 import Enemy_1
from enemy_2 import Enemy_2
from boss import Boss

config = open('config.json')
data = json.load(config)

# iterate through level_map

class Level:
    def __init__(self,level_layout,surface,game_state):
        super().__init__()

        self.display_surface = surface
        self.font = pygame.font.Font("./fonts/Square.ttf", 24)
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
        self.p_offset = pygame.math.Vector2()
        #player = self.player.sprite
        self.current_x = 0
        self.current_y = 0

        self.enemy_current_x = 0
        self.enemy_current_y = 0
        
        self.boss_current_x = 0
        self.boss_current_y = 0
        #self.offset.x = self.half_width - player.rect.centerx
        #self.offset.y = self.half_height - player.rect.centery
        self.game_state = game_state
        self.setup_level(level_layout)
        #self.scroll_x()
        #similar to below
        #self.x_shift = 0
        #self.y_shift = 0
        self.xScroll_on = True
        self.yScroll_on = False
        
        
        self.game_over_flag = False
        self.score = 0
        self.time = 0
        self.time_difference = 0
    # def spawn_fire(self, spawn_locations):
    #     #Seperate attacks
    #     self.fire_column = pygame.sprite.Group()
        
    #     for row_index, row in enumerate(spawn_locations):
    #         for col_index, cell in enumerate(row):

    #             x = col_index * tile_size
    #             y = row_index * tile_size   

    #             if cell == 'X' and self.fire_column:
    #                 result = random.randint(1,2)        
                    
    #                 if result == 2:
    #                     fire_column = Fire_Column((x, y))
    #                     self.fire_column.add(fire_column)
    #                 else:
    #                     return    

    def setup_level(self,level_layout):

        #Backgound path


        #collidable
        self.hard_tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.necromancer = pygame.sprite.GroupSingle()
        self.skeletons = pygame.sprite.Group()
        self.boss = pygame.sprite.GroupSingle()
        #Figure out how to use this
        self.summoned_skeletons = pygame.sprite.Group()

        #non collidable
        self.soft_tiles = pygame.sprite.Group()
        self.npc = pygame.sprite.GroupSingle()

        for level_layer in level_layout:
            for row_index, row in enumerate(level_layer):
                for col_index, cell in enumerate(row):

                    x = col_index * tile_size
                    y = row_index * tile_size

                    #Most Common
                    if cell == 'B':

                        tile = Tile((x, y), tile_size, 'B')
                        self.soft_tiles.add(tile) 
                    
                    elif cell == 'X':

                        tile = Tile((x, y), tile_size, 'X')
                        self.soft_tiles.add(tile)     
                    
                    #Hard tiles
                    elif cell == '-':

                        tile = Tile((x, y), tile_size, '-')
                        self.hard_tiles.add(tile)

                    elif cell == '[':

                        tile = Tile((x, y), tile_size, '[')
                        self.hard_tiles.add(tile)

                    elif cell == ']':

                        tile = Tile((x, y), tile_size, ']')
                        self.hard_tiles.add(tile)

                    elif cell == '_':

                        tile = Tile((x, y), tile_size, '_')
                        self.hard_tiles.add(tile)

                    elif cell == '{':

                        tile = Tile((x, y), tile_size, '{')
                        self.hard_tiles.add(tile)

                    elif cell == '}':

                        tile = Tile((x, y), tile_size, '}')
                        self.hard_tiles.add(tile)

                    elif cell == '/':

                        tile = Tile((x, y), tile_size, '/')
                        self.hard_tiles.add(tile)

                    elif cell == '|':

                        tile = Tile((x, y), tile_size, '|')
                        self.hard_tiles.add(tile)

                    elif cell == ':':

                        tile = Tile((x, y), tile_size, ':')
                        self.hard_tiles.add(tile)

                    elif cell == '<':

                        tile = Tile((x, y), tile_size, '<')
                        self.hard_tiles.add(tile)

                    elif cell == '=':

                        tile = Tile((x, y), tile_size, '=')
                        self.hard_tiles.add(tile)

                    elif cell == '>':

                        tile = Tile((x, y), tile_size, '>')
                        self.hard_tiles.add(tile)

                    elif cell == '8':

                        tile = Tile((x, y), tile_size, '8')
                        self.hard_tiles.add(tile)

                    elif cell == '9':

                        tile = Tile((x, y), tile_size, '9')
                        self.hard_tiles.add(tile)

                    elif cell == 'D':

                        tile = Tile((x, y), tile_size, 'D')
                        self.hard_tiles.add(tile)

                    elif cell == 'U':

                        tile = Tile((x, y), tile_size, 'U')
                        self.hard_tiles.add(tile)

                    elif cell == 'P':

                        player_sprite = Player((x, y))

                        self.player.add(player_sprite)

                    #NECROMANCER
                    elif cell == '*':

                        necromancer = Enemy_2((x, y))
                        self.necromancer.add(necromancer)

                    #SKELETON

                    elif cell == 'E':

                        skeleton = Enemy_1((x, y), data['difficulty'][str(self.game_state)]['skeletons'])
                        self.skeletons.add(skeleton)

                    #SLIME BOSS
                    elif cell == 'S':
                        
                        boss_sprite = Boss((x, y), data['difficulty'][str(self.game_state)]['boss'])
                        self.boss.add(boss_sprite)

                    #Soft tiles
                    elif cell == '!':

                        tile = Tile((x, y), tile_size, '!')
                        self.soft_tiles.add(tile)

                    elif cell == '#':

                        tile = Tile((x, y), tile_size, '#')
                        self.soft_tiles.add(tile)

                    elif cell == '$':

                        tile = Tile((x, y), tile_size, '$')
                        self.soft_tiles.add(tile)

                    elif cell == '%':

                        tile = Tile((x, y), tile_size, '%')
                        self.soft_tiles.add(tile)

                    elif cell == '&':

                        tile = Tile((x, y), tile_size, '&')
                        self.soft_tiles.add(tile)

                    elif cell == '(':

                        tile = Tile((x, y), tile_size, '(')
                        self.soft_tiles.add(tile)

                    elif cell == ')':

                        tile = Tile((x, y), tile_size, ')')
                        self.soft_tiles.add(tile)

                    elif cell == '@':

                        tile = Tile((x, y), tile_size, '@')
                        self.soft_tiles.add(tile)

                    elif cell == '^':

                        tile = Tile((x, y), tile_size, '^')
                        self.soft_tiles.add(tile)

                    elif cell == '~':

                        tile = Tile((x, y), tile_size, '~')
                        self.soft_tiles.add(tile)

                    elif cell == '0':

                        tile = Tile((x, y), tile_size, '0')
                        self.soft_tiles.add(tile)

                    elif cell == '1':

                        tile = Tile((x, y), tile_size, '1')
                        self.soft_tiles.add(tile)

                    elif cell == '2':

                        tile = Tile((x, y), tile_size, '2')
                        self.soft_tiles.add(tile)

                    elif cell == '3':

                        tile = Tile((x, y), tile_size, '3')
                        self.soft_tiles.add(tile)

                    elif cell == '4':

                        tile = Tile((x, y), tile_size, '4')
                        self.soft_tiles.add(tile)

                    elif cell == '5':

                        tile = Tile((x, y), tile_size, '5')
                        self.soft_tiles.add(tile)

                    elif cell == '6':

                        tile = Tile((x, y), tile_size, '6')
                        self.soft_tiles.add(tile)

                    elif cell == '7':

                        tile = Tile((x, y), tile_size, '7')
                        self.soft_tiles.add(tile)

                    elif cell == 'A':

                        tile = Tile((x, y), tile_size, 'A')
                        self.soft_tiles.add(tile)

                    elif cell == 'C':

                        tile = Tile((x, y), tile_size, 'C')
                        self.soft_tiles.add(tile)

                    elif cell == 'F':

                        tile = Tile((x, y), tile_size, 'F')
                        self.soft_tiles.add(tile)

                    elif cell == 'G':

                        tile = Tile((x, y), tile_size, 'G')
                        self.soft_tiles.add(tile)

                    elif cell == 'H':

                        tile = Tile((x, y), tile_size, 'H')
                        self.soft_tiles.add(tile)

                    elif cell == 'I':

                        tile = Tile((x, y), tile_size, 'I')
                        self.soft_tiles.add(tile)

                    elif cell == 'J':

                        tile = Tile((x, y), tile_size, 'J')
                        self.soft_tiles.add(tile)

                    elif cell == 'K':

                        tile = Tile((x, y), tile_size, 'K')
                        self.soft_tiles.add(tile)

                    elif cell == 'L':

                        tile = Tile((x, y), tile_size, 'L')
                        self.soft_tiles.add(tile)

                    elif cell == 'M':

                        tile = Tile((x, y), tile_size, 'M')
                        self.soft_tiles.add(tile)

                    elif cell == 'N':

                        tile = Tile((x, y), tile_size, 'N')
                        self.soft_tiles.add(tile)

                    elif cell == 'O':

                        tile = Tile((x, y), tile_size, 'O')
                        self.soft_tiles.add(tile)

                    elif cell == 'Q':

                        tile = Tile((x, y), tile_size, 'Q')
                        self.soft_tiles.add(tile)

                    elif cell == 'R':

                        tile = Tile((x, y), tile_size, 'R')
                        self.soft_tiles.add(tile)

                    elif cell == 'T':

                        tile = Tile((x, y), tile_size, 'T')
                        self.soft_tiles.add(tile)

                    elif cell == 'V':

                        tile = Tile((x, y), tile_size, 'V')
                        self.soft_tiles.add(tile)

                    elif cell == 'W':

                        tile = Tile((x, y), tile_size, 'W')
                        self.soft_tiles.add(tile)

                    elif cell == 'Y':

                        tile = Tile((x, y), tile_size, 'Y')
                        self.soft_tiles.add(tile)

                    elif cell == 'Z':

                        tile = Tile((x, y), tile_size, 'Z')
                        self.soft_tiles.add(tile)

                    #NPC
                    elif cell == '?':

                        npc_sprite = NPC((x, y))
                        self.npc.add(npc_sprite)


    def HUD(self):
        
        player = self.player.sprite
        
        health_header =  self.font.render("HP: "+str(player.health), True, (255, 255, 255))
        self.display_surface.blit(health_header, (0, 0))
        
        time = self.time - self.time_difference
        
        
        # seconds = 
        # milliseconds = 
        
        time_header =  self.font.render(self.calculate_time(time), True, (255, 255, 255))
        self.display_surface.blit(time_header, (100, 0))
        
        score_header = self.font.render("Score: "+str(self.score), True, (255, 255, 255))
        self.display_surface.blit(score_header, (200, 0))


    def calculate_time(self, millis):
        seconds = (millis/1000)%60
        minutes = (millis/(1000*60))%60
        return str(minutes + seconds)
        

    def game_over(self):
        
        
        
        game_over_header =  self.font.render("GAME OVER", True, (255, 255, 255))
        self.display_surface.blit(game_over_header, (screen_height / 2, screen_width / 2))
        
        dead_header = self.font.render("You are DEAD!", True, (255, 255, 255))
        self.display_surface.blit(dead_header, (((screen_height / 2) - 50), screen_width / 2))    
        
        restart_header = self.font.render("Press SPACE to Restart", True, (255, 255, 255))
        self.display_surface.blit(restart_header, (((screen_height) - 50), screen_width / 2))  
        
        quit_header = self.font.render("Press ESC to Quit", True, (255, 255, 255))
        self.display_surface.blit(quit_header, (((screen_height) - 50), screen_width / 2))  
        
        self.game_over_flag = True
    
    def win(self):
        
        
        win_header = self.font.render("GAME OVER", True, (255, 255, 255))
        self.display_surface.blit(win_header, (screen_height / 2, screen_width / 2))
        
        highscore_header = self.font.render("Highscore: "+ str(self.score), True, (255, 255, 255))
        self.display_surface.blit(highscore_header, (screen_height / 2, screen_width / 2))
        
        time_header =  self.font.render("Time Completed: "+ str(self.time), True, (255, 255, 255))
        self.display_surface.blit(time_header, (screen_height / 2, screen_width / 2))
        
        restart_header = self.font.render("Press SPACE to Restart", True, (255, 255, 255))
        self.display_surface.blit(restart_header, (((screen_height) - 50), screen_width / 2))  
        
        quit_header = self.font.render("Press ESC to Quit", True, (255, 255, 255))
        self.display_surface.blit(quit_header, (((screen_height) - 50), screen_width / 2))  
           
        self.game_over_flag = True
        
    # Player Camera
    #Fix climbing walls
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        self.offset.x = data['difficulty'][str(self.game_state)]['offset.x']
        self.p_offset.x = data['difficulty'][str(self.game_state)]['p_offset.x'] 
        boss = self.boss.sprite
        # if player_x < tile_size * 1 and direction_x < 0:
        #     self.offset.x = 8
        #     player.speed = 0
            
        # elif (player_x > tile_size * 21)  and direction_x > 0:

        #     self.offset.x = -8
        #     player.speed = 0
        
        
        
        if player.direction.x == 0:
            self.p_offset.x = data['difficulty'][str(self.game_state)]['offset.x']       
        # else:
        #     self.offset.x = 0
        #     player.speed = 8
        for sprite in self.hard_tiles.sprites():
            #if sprite.rect.colliderect(player.rect) and sprite

            # if sprite.rect.colliderect(player.rect):
            #     if sprite.id == 'U' or sprite.id == 'D':
            #         player.player_status['death'] = True
                    
            if sprite.rect.colliderect(player.env_rect):
                #issue with camera may be caused here
                
                if player.direction.x > 0:
                    
                    player.env_rect.right = sprite.rect.left - 1
                    player.rect.right = player.env_rect.right + 2
                    player.wall_right = True
                    self.current_x = player.env_rect.right
                    player.stop = True
                    player.direction.x = 0
                    self.p_offset.x = data['difficulty'][str(self.game_state)]['offset.x']       
        
        if (boss.rect.x - player.rect.x) <= 500:
            self.yScroll_on = True
        
        if boss.rect.x <= (screen_width / 2):
            self.p_offset.x = 0
            self.offset.x = 0
            self.xScroll_on = False
   
    def scroll_y(self):
        player = self.player.sprite
        player_y = player.rect.centery
        direction_y = player.direction.y
        boss = self.boss.sprite
        # if player_y < screen_height / 2 and direction_y < 0 :

        #     self.offset.y += 0.5
        #     player.gravity = 0

        if player_y > screen_height / 2 and direction_y > 0:

            self.offset.y += -2.5
            player.gravity = 0

        else:

            self.offset.y = 0
            player.gravity = 0.5
        
        if (boss.rect.y - player.rect.y) <= 100:
            self.yScroll_on = False
            self.offset.y = 0
            player.gravity = 0.5
        # if player.rect.centery >= screen_height / 2:
        #     self.yScroll_on = False

    def player_horizontal_collision(self):

        player = self.player.sprite
        player.rect.x += (player.direction.x * player.speed) + self.p_offset.x
        player.env_rect.x += (player.direction.x * player.speed) + self.p_offset.x
            
        for sprite in self.hard_tiles.sprites():
            #if sprite.rect.colliderect(player.rect) and sprite

            # if sprite.rect.colliderect(player.rect):
            #     if sprite.id == 'U' or sprite.id == 'D':
            #         player.player_status['death'] = True
            #         print(player.player_status['death'] ) 
                    
            if sprite.rect.colliderect(player.env_rect):
                #issue with camera may be caused here
                if player.direction.x < 0:

                    player.env_rect.left = sprite.rect.right
                    player.rect.left = player.env_rect.left - 2
                    player.wall_left = True
                    self.current_x = player.env_rect.left
                    
                    # player.isXScrolling = False
                elif player.direction.x > 0:
                    player.env_rect.right = sprite.rect.left - 1
                    player.rect.right = player.env_rect.right + 2
                    player.wall_right = True
                    self.current_x = player.env_rect.right + 1
                    # player.isXScrolling = False

            
        
                 #
        
        if player.wall_left and (player.env_rect.left < self.current_x or player.direction.x >= 0):
            player.wall_left = False
            
    # #
        if player.wall_right and (player.env_rect.right > self.current_x or player.direction.x <= 0):
            player.wall_right = False
            player.stop = False

        #self.player.update(False)



    def player_vertical_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.hard_tiles.sprites():
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


    def enemy_horizontal_collision(self):
        
        for skeleton in self.skeletons.sprites():
            skeleton.rect.x += skeleton.direction.x * skeleton.speed

            # skeleton.rect.x += skeleton.direction.x * skeleton.speed
        # player.env_rect.x += player.direction.x * player.speed

            for sprite in self.hard_tiles.sprites():


                if sprite.rect.colliderect(skeleton.rect):

                    #issue with camera may be caused here
                    if skeleton.direction.x < 0:

                        skeleton.rect.left = sprite.rect.right
                        skeleton.wall_left = True
                        self.enemy_current_x = skeleton.rect.left
                        
                    elif skeleton.direction.x > 0:


                        skeleton.rect.right = sprite.rect.left
                        skeleton.wall_right = True
                        self.enemy_current_x = skeleton.rect.right


                        #

            # if(skeleton.wall_left and skeleton.rect.left < self.enemy_current_x or skeleton.direction.x >= 0):
            #     skeleton.wall_left = False
            # # #
            # if(skeleton.wall_right and skeleton.rect.right > self.enemy_current_x or skeleton.direction.x <= 0):
            #     skeleton.wall_right = False

        #self.player.update(False)

    def enemy_vertical_collision(self):
        for skeleton in self.skeletons.sprites():
            skeleton.apply_gravity()
        #check for specific tile (the cliff one to turn before falling)
            for sprite in self.hard_tiles.sprites():
                if sprite.rect.colliderect(skeleton.rect):
                    if sprite.id == ']' or sprite.id == '>':
                        skeleton.wall_right = True
                        skeleton.speed = 0
                    elif sprite.id == '[' or sprite.id == '<':
                        skeleton.wall_left = True
                        skeleton.speed = 0    
                    else:
                        skeleton.wall_left = False
                        skeleton.wall_right = False
                    
                    if skeleton.direction.y > 0:
                        skeleton.rect.bottom = sprite.rect.top

                        skeleton.direction.y = 0
                        # skeleton.on_ground = True
                        self.enemy_current_y = skeleton.rect.top
                    # elif skeleton.direction.y < 0:
                    #     skeleton.rect.top = sprite.rect.bottom

                    #     skeleton.direction.y = 0
                    #     # skeleton.on_ceiling = True
                    #     self.enemy_current_y = skeleton.rect.bottom

            #
            #if(player.on_ground and player.direction.y < 0 or player.direction.y > 1):
            #     player.on_ground = False
            # #
            # if(player.on_ceiling and player.direction.y > 0):
            #     player.on_ceiling = False

    def boss_horizontal_collision(self):

        boss = self.boss.sprite
        boss.rect.x += boss.direction.x * boss.speed

        for sprite in self.hard_tiles.sprites():
            if sprite.rect.colliderect(boss.rect):
                
                #issue with camera may be caused here
                if boss.direction.x < 0:

                    boss.rect.left = sprite.rect.right
                    boss.wall_left = True
                    self.boss_current_x = boss.rect.left
                elif boss.direction.x > 0:

                    boss.rect.right = sprite.rect.left
                    boss.wall_right = True
                    self.boss_current_x = boss.rect.right


        #             #
        # if(boss.wall_left and boss.rect.left < self.boss_current_x or boss.direction.x >= 0):
        #     boss.wall_left = False
        # #
        # if(boss.wall_right and boss.rect.right > self.boss_current_x or boss.direction.x <= 0):
        #     boss.wall_right = False

        #self.player.update(False)



    def boss_vertical_collision(self):
        boss = self.boss.sprite
        boss.apply_gravity()

        for sprite in self.hard_tiles.sprites():
            if sprite.rect.colliderect(boss.rect):
                if sprite.id == ']' or sprite.id == '>':
                    boss.wall_right = True
                    boss.speed = 0
                elif sprite.id == '[' or sprite.id == '<':
                    boss.wall_left = True
                    boss.speed = 0    
                else:
                    boss.wall_left = False
                    boss.wall_right = False
                        
                if boss.direction.y > 0:
                    boss.rect.bottom = sprite.rect.top

                    boss.direction.y = 0
                   # boss.on_ground = True
                    self.boss_current_y = boss.rect.top
                elif boss.direction.y < 0:
                    boss.rect.top = sprite.rect.bottom

                    boss.direction.y = 0
                    # boss.on_ceiling = True
                    self.boss_current_y = boss.rect.bottom

        #
       #if(boss.on_ground and boss.direction.y < 0 or boss.direction.y > 1):
       #     boss.on_ground = False
        #
        #if(boss.on_ceiling and boss.direction.y > 0):
        #    boss.on_ceiling = False


    def check_player(self):
        
        player = self.player.sprite
        boss = self.boss.sprite
        
        for sprite in self.hard_tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if sprite.id == 'U' or sprite.id == 'D':
                    player.health = 0
                    player.player_status['death'] = True
        
        if self.skeletons.sprites():
            for skeleton in self.skeletons.sprites():
                if skeleton.rect.colliderect(player.env_rect) and player.isAttacking == False and skeleton.isDead == False and skeleton.isHurt == False and skeleton.isAttacking == True:
                    player.health -= skeleton.damage    
                if skeleton.rect.colliderect(player.rect) and player.isAttacking == True and skeleton.isDead == False and skeleton.isHurt == False:
                    skeleton.health -= player.damage
                    if skeleton.health <= 0:
                        self.score += skeleton.points
                        self.time_difference += skeleton.time
        
        if boss:
            if boss.rect.colliderect(player.rect) and player.isAttacking == False and boss.isDead == False and boss.isHurt == False and boss.isAttacking == True:               
                player.health -= boss.damage    
            if boss.rect.colliderect(player.rect) and player.isAttacking == True and boss.isDead == False and boss.isHurt == False and boss.isAttacking == False:               
                
                boss.health -= player.damage
                
            if boss.health <= 0:
                boss.isDead = True
                self.score += boss.points    
                
                
            
            
        if player.rect.x < -40 or player.rect.y < -40 or player.rect.y > screen_height or player.health <= 0:
            player.health = 0
            player.player_status['death'] = True
            
            
    def run(self, attacking, time):

        player = self.player.sprite
        skeletons = self.skeletons.sprites()
        boss = self.boss.sprite
        
        self.time = time
        #COMING SOON!
        # npc = self.npc.sprite
        # summoned_skeletons = self.summoned_skeletons.sprites()
        # necromancer = self.necromancer.sprite
        
        
        # Level tiles
        self.soft_tiles.update(self.offset)
        self.soft_tiles.draw(self.display_surface)
        
        self.hard_tiles.update(self.offset)
        self.hard_tiles.draw(self.display_surface)
        
        if self.xScroll_on == True:
            self.scroll_x()
        
        if self.yScroll_on == True:
            self.scroll_y()

        #NPC - COMING SOON!
        # self.npc.update(self.offset)
        # self.npc.draw(self.display_surface)
        
        # Player
        self.check_player()
        self.player.update(attacking)
        self.player_vertical_collision()
        self.player_horizontal_collision()
        self.player.draw(self.display_surface)

        

        #Skeletons
        self.skeletons.update(self.offset, player)
        self.enemy_vertical_collision()
        self.enemy_horizontal_collision()
        self.skeletons.draw(self.display_surface)


        self.boss.update(self.offset, player)
        if self.boss:
            self.boss_vertical_collision()
            self.boss_horizontal_collision()
        self.boss.draw(self.display_surface)
        
        self.HUD()
        
        if player.health == 0:
            self.game_over()    

        if boss:
            if player.health != 0 and boss.health <= 0:
                self.win()

        return player, skeletons, boss, self.game_over_flag 
        
        #npc,  summoned_skeletons, necromancer