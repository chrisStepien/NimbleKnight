import pygame
import json
from level_settings import tile_size, screen_width, screen_height
from tiles import Tile
from player import Player
from npc import NPC
from enemy_1 import Enemy_1
from enemy_2 import Enemy_2
from boss import Boss

#Get Difficulty Data
config = open('config.json')
data = json.load(config)

class Level:
    def __init__(self,level_layout,surface,game_state):
        super().__init__()
        
        # Screen Variables
        self.display_surface = surface
        self.font = pygame.font.Font("./fonts/RINGM___.TTF", 24)
        self.font2 = pygame.font.Font("./fonts/RINGM___.TTF", 55)
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        
        # Directional Info 
        self.offset = pygame.math.Vector2()
        self.p_offset = pygame.math.Vector2()
       
        self.current_x = 0
        self.current_y = 0

        self.enemy_current_x = 0
        self.enemy_current_y = 0
        
        self.boss_current_x = 0
        self.boss_current_y = 0

        self.game_state = game_state
        self.setup_level(level_layout)

        #Sound
        self.win_sound = pygame.mixer.Sound("./media/victory.wav")

        #Auto-scrolling Cameras
        self.xScroll_on = True
        self.yScroll_on = False
        
        self.game_over_flag = False
        self.win_flag = False
        self.score = 0
      
   
    def setup_level(self,level_layout):

        #Collidable Entities
        self.hard_tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.boss = pygame.sprite.GroupSingle()
        self.skeletons = pygame.sprite.Group()
        
        #Coming Soon!
        # self.necromancer = pygame.sprite.GroupSingle()
        # self.summoned_skeletons = pygame.sprite.Group()

        #Non-collidable Entities
        self.soft_tiles = pygame.sprite.Group()
        
        #Coming Soon!
        #self.npc = pygame.sprite.GroupSingle()

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

                    #Coming Soon!
                    #NECROMANCER
                    #elif cell == '*':

                        #necromancer = Enemy_2((x, y))
                        #self.necromancer.add(necromancer)

                    #SKELETON
                    elif cell == 'E':

                        skeleton = Enemy_1((x, y), data['difficulty'][str(self.game_state)]['skeletons'])
                        self.skeletons.add(skeleton)

                    #BOSS
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
                    
                    #Coming Soon!
                    #NPC
                    #elif cell == '?':

                        #npc_sprite = NPC((x, y))
                        #self.npc.add(npc_sprite)

    # Player HUD
    def HUD(self):
        
        player = self.player.sprite
        boss = self.boss.sprite
        
        health_header =  self.font.render("hp: "+str(player.health), True, (136, 8, 8))
        self.display_surface.blit(health_header, (50, 15))
        
        
        time_header =  self.font.render("boss hp: "+ str(boss.health), True, (255, 255, 255))
        self.display_surface.blit(time_header, ((screen_width / 2) - 80, 15))
        
        score_header = self.font.render("score: "+str(self.score), True, (255, 192, 0))
        self.display_surface.blit(score_header, (920, 15))
        
    # Game Over Overlay
    def game_over(self):
        
        game_over_header =  self.font2.render("GAME OVER", True, (255, 255, 255))
        self.display_surface.blit(game_over_header, ((screen_width / 2) - 165, (screen_height / 2) - 100))
        
        dead_header = self.font2.render("You are DEAD!", True, (255, 255, 255))
        self.display_surface.blit(dead_header, (((screen_width / 2) - 190), (screen_height / 2)))    
        
        restart_header = self.font.render("Press SPACE to Restart", True, (255, 255, 255))
        self.display_surface.blit(restart_header, (((screen_width / 3) - 200), (screen_height) - 60))  
        
        quit_header = self.font.render("Press ESC to Quit", True, (255, 255, 255))
        self.display_surface.blit(quit_header, (((screen_width) - 350), (screen_height) - 60))  
        
        self.game_over_flag = True
    
    # Win Overlay
    def win(self):
        
        win_header = self.font.render("CASTLE LIBERATED", True, (255, 255, 255))
        self.display_surface.blit(win_header, (screen_width / 2, screen_height / 2))
        
        highscore_header = self.font.render("Highscore: "+ str(self.score), True, (255, 255, 255))
        self.display_surface.blit(highscore_header, (screen_height / 2, screen_width / 2))
        
        time_header =  self.font.render("Time Completed: "+ str(self.time), True, (255, 255, 255))
        self.display_surface.blit(time_header, (screen_width / 2, screen_height / 2))
        
        restart_header = self.font.render("Press SPACE to Restart", True, (255, 255, 255))
        self.display_surface.blit(restart_header, (((screen_width) - 50), screen_height / 2))  
        
        quit_header = self.font.render("Press ESC to Quit", True, (255, 255, 255))
        self.display_surface.blit(quit_header, (((screen_width) - 50), screen_height / 2))  
           
        self.game_over_flag = True
        
    # Player Camera
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        self.offset.x = data['difficulty'][str(self.game_state)]['offset.x']
        self.p_offset.x = data['difficulty'][str(self.game_state)]['p_offset.x'] 
        boss = self.boss.sprite
 
        if player.direction.x == 0:
            self.p_offset.x = data['difficulty'][str(self.game_state)]['offset.x']       
      
        for sprite in self.hard_tiles.sprites():
            
            if sprite.rect.colliderect(player.env_rect):
                
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

    def player_horizontal_collision(self):

        player = self.player.sprite
        player.rect.x += (player.direction.x * player.speed) + self.p_offset.x
        player.env_rect.x += (player.direction.x * player.speed) + self.p_offset.x
            
        for sprite in self.hard_tiles.sprites():
                    
            if sprite.rect.colliderect(player.env_rect):
                if player.direction.x < 0:

                    player.env_rect.left = sprite.rect.right
                    player.rect.left = player.env_rect.left - 2
                    player.wall_left = True
                    self.current_x = player.env_rect.left
                    
                elif player.direction.x > 0:
                    player.env_rect.right = sprite.rect.left - 1
                    player.rect.right = player.env_rect.right + 2
                    player.wall_right = True
                    self.current_x = player.env_rect.right + 1
        
        if player.wall_left and (player.env_rect.left < self.current_x or player.direction.x >= 0):
            player.wall_left = False
            

        if player.wall_right and (player.env_rect.right > self.current_x or player.direction.x <= 0):
            player.wall_right = False
            player.stop = False





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

        if(player.on_ground and player.direction.y < 0 or player.direction.y > 1):
            player.on_ground = False
        
        if(player.on_ceiling and player.direction.y > 0):
            player.on_ceiling = False


    def enemy_horizontal_collision(self):
        
        for skeleton in self.skeletons.sprites():
            skeleton.rect.x += skeleton.direction.x * skeleton.speed

            for sprite in self.hard_tiles.sprites():

                if sprite.rect.colliderect(skeleton.rect):

                    if skeleton.direction.x < 0:

                        skeleton.rect.left = sprite.rect.right
                        skeleton.wall_left = True
                        self.enemy_current_x = skeleton.rect.left
                        
                    elif skeleton.direction.x > 0:

                        skeleton.rect.right = sprite.rect.left
                        skeleton.wall_right = True
                        self.enemy_current_x = skeleton.rect.right

    def enemy_vertical_collision(self):
        for skeleton in self.skeletons.sprites():
            skeleton.apply_gravity()
        #Check for specific tile (The cliff one to turn before falling)
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
                        self.enemy_current_y = skeleton.rect.top
       
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
                    self.boss_current_y = boss.rect.top
                elif boss.direction.y < 0:
                    boss.rect.top = sprite.rect.bottom
                    boss.direction.y = 0
                    self.boss_current_y = boss.rect.bottom

    def check_player(self):
        
        player = self.player.sprite
        boss = self.boss.sprite
        
        for sprite in self.hard_tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if sprite.id == 'U' or sprite.id == 'D':
                    player.health = 0
                    player.player_status['death'] = True
        
        # Check Skeleton collision
        if self.skeletons.sprites():
            for skeleton in self.skeletons.sprites():
                if skeleton.rect.colliderect(player.env_rect) and player.isAttacking == False and skeleton.isDead == False and skeleton.isHurt == False and skeleton.isAttacking == True:
                    player.health -= skeleton.damage    
                if skeleton.rect.colliderect(player.rect) and player.isAttacking == True and skeleton.isDead == False and skeleton.isHurt == False:
                    skeleton.health -= player.damage
                    if skeleton.health <= 0:
                        self.score += skeleton.points
        
        # Check Boss collision
        if boss:
            if boss.rect.colliderect(player.rect) and player.isAttacking == False and boss.isDead == False and boss.isHurt == False and boss.isAttacking == True:               
                player.health -= boss.damage    
            if boss.rect.colliderect(player.rect) and player.isAttacking == True and boss.isDead == False and boss.isHurt == False and boss.isAttacking == False:               
                
                boss.health -= player.damage
                
            if boss.health <= 0:
                boss.isDead = True
                self.score += boss.points
                self.win_flag = True    

        # Player Dies if off screen (Not Front)
        if player.rect.x < -40 or player.rect.y < -40 or player.rect.y > screen_height or player.health <= 0:
            player.health = 0
            player.player_status['death'] = True
            
            
    def run(self, attacking):

        player = self.player.sprite
        skeletons = self.skeletons.sprites()
        boss = self.boss.sprite
        
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

        if self.win_flag == True:
            self.win_sound.play()
            self.win()

        return player, skeletons, boss, self.game_over_flag 
        
        #npc,  summoned_skeletons, necromancer