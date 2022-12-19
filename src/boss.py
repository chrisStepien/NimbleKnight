import pygame
import random
from import_assets import import_boss

class Boss(pygame.sprite.Sprite):
    def __init__(self, pos):
        
        super().__init__()
        self.import_boss_assets()

        
        
        # Frame indexs
        self.spell_frame_index = 0
        self.cleave_frame_index = 0
        self.death_frame_index = 0
        self.breath_frame_index = 0
        self.hit_frame_index = 0
        self.idle_frame_index = 0
        self.s_hit_frame_index = 0
        self.s_idle_frame_index = 0
        self.s_walk_frame_index = 0
        self.smash_frame_index = 0
        self.transform_frame_index = 0
        self.walk_frame_index = 0
        
        self.image = self.animations['slime_idle'][self.s_idle_frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        
        
        # Frame speeds
        self.spell_frame_speed = 0.5
        self.cleave_frame_speed = 0.5
        self.death_frame_speed = 0.5
        self.breath_frame_speed = 0.5
        self.hit_frame_speed = 0.5
        self.idle_frame_speed = 0.5
        self.s_hit_frame_speed = 0.5
        self.s_idle_frame_speed = 0.4
        self.s_walk_frame_speed = 0.5
        self.smash_frame_speed = 0.5
        self.transform_frame_speed = 0.6
        self.walk_frame_speed = 0.5

        # Demon slime status
        self.isSlime = True
        self.isTransforming = False
        self.isDemon = False
        
        
        
        self.isAnimating = False
        self.isAttacking = False
        self.isAggro = False
        self.isWalking = False
        self.isCasting = False
        self.isCleaving = False
        self.isDead = False
        self.isBreathing = False
        self.isHurt = False
        self.isIdle = False
        self.isS_Hurt = False
        self.isS_Idle = True
        self.isS_Walk = False
        self.isSmash = False
        
        self.facing_right = False
        self.wall_right = False
        self.wall_left = False
        
        self.speed = 6
        self.direction = pygame.math.Vector2(0, 0)
        self.gravity = 0.5
        
        self.start_time = 0
        self.spell_timer = 0 
        
        self.health = 100
        
        self.fire_column = False
        self.fire_ball = False
        
    def import_boss_assets(self):
        
        self.animations = {'cast_spell': [], 'cleave': [], 'death': [], 'fire_breath': [], 'hit': [], 'idle': [], 'slime_hit': [], 'slime_idle': [], 'slime_walk': [], 'smash': [], 'transform': [], 'walk': []}    
        
        for animation in self.animations.keys():
            
            self.default_path = './assets/boss/'
            self.default_path += animation
            self.animations[animation] = import_boss(self.default_path)

   
    #random attack
    
    #spells maybe?
    
    def apply_gravity(self):
        
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    
    def set_offset(self, offset):

        self.rect.x += offset.x
        self.rect.y += offset.y
            
    
    def calculate_distance(self, player):
        
        boss_x = self.rect.x
        boss_y = self.rect.y
        
        player_x = player.rect.x
        player_y = player.rect.y

        loc_x_diff = boss_x - player_x
        loc_y_diff = boss_y - player_y
        
        if loc_x_diff < 400 and loc_x_diff > -400 and loc_y_diff < 400 and loc_y_diff > -400:
            self.isAnimating = True
        else:
            self.isAnimating = False
            self.start_time = 0    
        
        #Also if spell_time is 0 to only trigger once everytime this happens
        if self.isAggro and loc_y_diff < 10:
            self.isCasting = True

        self.boss_logic(loc_x_diff, loc_y_diff)
        
    def boss_logic(self, x_diff, y_diff):
         
        # Get direction
        if self.direction.x > 0 and self.isAggro and not self.isAttacking:
            self.facing_right = False
        elif self.direction.x < 0 and self.isAggro and not self.isAttacking:    
            self.facing_right = True
        
        #add another for slime version    
        #Collision
        if (self.wall_left and not self.facing_right) and self.isSlime:
            self.isS_Walk = False
            self.isS_Idle = True
        elif(self.wall_right and self.facing_right) and self.isSlime:
            self.isS_Walk = False
            self.isS_Idle = True
        elif(self.wall_left and not self.facing_right) and self.isDemon:
            self.isWalking = False
            self.isIdle = True
        elif(self.wall_right and self.facing_right) and self.isDemon:
            self.isWalking = False
            self.isIdle = True
            
        #Check if attacking
        if self.isCasting or self.isCleaving or self.isBreathing or self.isSmash:
            self.isAttacking = True
            self.isWalking = False
            self.isIdle = False
        else:
            self.isAttacking = False 
            
        if not self.isAggro and self.isAnimating and not self.isTransforming and self.isSlime:
            self.randomize_movement()

            if self.isS_Walk and self.isSlime:
                self.isS_Idle = False
                if self.facing_right and not self.wall_right:
                    self.s_walk_frame_speed = 0.3
                    self.speed = 2
                    self.rect.x += self.speed
                    self.direction.x += self.speed
                    
                elif not self.facing_right and not self.wall_left:
                    self.speed = 2
                    self.rect.x -= self.speed
                    self.direction.x -= self.speed
                    
                    self.walk_frame_speed = 0.3
        elif self.isAggro and self.isDemon:    
                if x_diff <= 10 and x_diff >= -10 and not self.isAttacking:

                    self.isWalking = False
                    self.isIdle = True
                    
                if x_diff > 10 and not self.isAttacking and not self.wall_left:
                    self.isWalking = True
                    self.walk_frame_speed = 0.6
                    self.speed = 6
                    self.rect.x -= self.speed
                    self.direction.x -= self.speed
                    
                    
                if x_diff < -10 and not self.isAttacking and not self.wall_right:
                    self.isWalking = True
                    self.walk_frame_speed = 0.6   
                    self.speed = 6 
                    self.rect.x += self.speed
                    self.direction.x += self.speed
                    
                    
                if (x_diff < 20 and x_diff > -20) and (y_diff < 20 and y_diff > -20) and not self.isAttacking:
                    self.randomize_movement()
                    self.isWalking = False 
        
        
        self.health -= 1
        if(self.health <= 0 and not self.isTransforming and not self.isAggro):
            self.isTransforming = True
            self.isS_Walk = False
            self.isS_Idle = False
            self.isS_Hurt = False                    
            self.isSlime = False

          
            
    def randomize_movement(self):
        
        time = pygame.time.get_ticks() - self.start_time
        random_time = random.randint(3000, 5000)
        
        if(time > random_time) and self.isSlime:
            
            result = random.randint(1,4)
            self.start_time = pygame.time.get_ticks()
            
            #turn right and walk
            if(result == 1):
                self.facing_right = True
                self.isS_Walk = True
                
            #turn left and walk
            elif(result == 2):
                self.facing_right = False
                self.isS_Walk = True
            
            #turn right and idle
            elif(result == 3):
                self.facing_right = True
                self.isS_Walk = False
                self.isS_Idle = True
                
            #turn left and idle 
            elif(result == 4):
                self.isS_Walk = False
                self.isS_Idle = True
                self.facing_right = False      
        
        elif(time > random_time) and self.isDemon:
            
            result = random.randint(1,4)
            self.start_time = pygame.time.get_ticks()
            
            #turn right and walk
            if(result == 1):
                self.isCleaving = True
                
            #turn left and walk
            elif(result == 2):
                self.isBreathing = True
            
            #turn right and idle
            elif(result == 3):
                self.isSmash = True
                
            #turn left and idle 
            elif(result == 4):
                self.isCleaving = True
                
        
    def animate(self):
        
        if not self.isAnimating:
            return
        if self.isAnimating:
            
            if not self.facing_right:
            
                if self.isCasting:
                    self.spell_frame_index += self.spell_frame_speed

                    if int(self.spell_frame_index) > len(self.animations['cast_spell']) - 1:

                        self.spell_frame_index = 0
                        self.isCasting = False
                    else:
                        self.image = self.animations['cast_spell'][int(self.spell_frame_index)]
                        self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isCleaving:
                    self.cleave_frame_index += self.cleave_frame_speed

                    if int(self.cleave_frame_index) > len(self.animations['cleave']) - 1:

                        self.cleave_frame_index = 0
                        self.isCleaving = False
                    else:
                        self.image = self.animations['cleave'][int(self.cleave_frame_index)]
                        self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isDead:
                    self.death_frame_index += self.death_frame_speed

                    if int(self.death_frame_index) > len(self.animations['death']) - 1:

                        self.death_frame_index = 0
                    else:
                        self.image = self.animations['death'][int(self.death_frame_index)]
                        self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isBreathing:
                    self.breath_frame_index += self.breath_frame_speed

                    if int(self.breath_frame_index) > len(self.animations['fire_breath']) - 1:

                        self.breath_frame_index = 0
                        self.isBreathing = False
                    else:
                        self.image = self.animations['fire_breath'][int(self.breath_frame_index)]
                        self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isHurt:
                    self.hit_frame_index += self.hit_frame_speed

                    if int(self.hit_frame_index) > len(self.animations['hit']) - 1:

                        self.hit_frame_index = 0
                    else:
                        self.image = self.animations['hit'][int(self.hit_frame_index)]
                        self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isIdle:
                    self.idle_frame_index += self.idle_frame_speed

                    if int(self.idle_frame_index) > len(self.animations['idle']) - 1:

                        self.idle_frame_index = 0
                    else:
                        self.image = self.animations['idle'][int(self.idle_frame_index)]
                        self.rect = self.image.get_rect(topleft=self.rect.topleft)

                if self.isS_Hurt and self.isSlime:
                    self.s_hit_frame_index += self.s_hit_frame_speed

                    if int(self.s_hit_frame_index) > len(self.animations['slime_hit']) - 1:

                        self.s_hit_frame_index = 0
                    else:
                        self.image = self.animations['slime_hit'][int(self.s_hit_frame_index)]
                        self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isS_Idle and self.isSlime:
                    self.s_idle_frame_index += self.s_idle_frame_speed

                    if int(self.s_idle_frame_index) > len(self.animations['slime_idle']) - 1:

                        self.s_idle_frame_index = 0
                    else:
                        self.image = self.animations['slime_idle'][int(self.s_idle_frame_index)]
                        self.rect = self.image.get_rect(topleft=self.rect.topleft)

                if self.isS_Walk and self.isSlime:
                    self.s_walk_frame_index += self.s_walk_frame_speed

                    if int(self.s_walk_frame_index) > len(self.animations['slime_walk']) - 1:

                        self.s_walk_frame_index = 0
                    else:
                        self.image = self.animations['slime_walk'][int(self.s_walk_frame_index)]
                        self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isSmash:
                    self.smash_frame_index += self.smash_frame_speed

                    if int(self.smash_frame_index) > len(self.animations['smash']) - 1:

                        self.smash_frame_index = 0
                        self.isSmash = False
                    else:
                        self.image = self.animations['smash'][int(self.smash_frame_index)]
                        self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isTransforming:
                    self.transform_frame_index += self.transform_frame_speed
                    if int(self.transform_frame_index) > len(self.animations['transform']) - 1:

                        self.transform_frame_index = 0
                        self.isTransforming = False
                        self.isDemon = True
                        self.isAggro = True
                    
                    else:
                        self.image = self.animations['transform'][int(self.transform_frame_index)]
                        self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isWalking:
                    self.walk_frame_index += self.walk_frame_speed

                    if int(self.walk_frame_index) > len(self.animations['walk']) - 1:

                        self.walk_frame_index = 0
                    else:
                        self.image = self.animations['walk'][int(self.walk_frame_index)]
                        self.rect = self.image.get_rect(topleft=self.rect.topleft)                                
            # Facing Right    
            else:     
                if self.isCasting:
                    self.spell_frame_index += self.spell_frame_speed

                    if int(self.spell_frame_index) > len(self.animations['cast_spell']) - 1:

                        self.spell_frame_index = 0
                        self.isCasting = False
                    else:
                        image = self.animations['cast_spell'][int(self.spell_frame_index)]
                        flipped_image = pygame.transform.flip(image, True, False)
                        self.image = flipped_image
                        self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isCleaving:
                    self.cleave_frame_index += self.cleave_frame_speed

                    if int(self.cleave_frame_index) > len(self.animations['cleave']) - 1:

                        self.cleave_frame_index = 0
                        self.isCleaving = False
                    else:
                        image = self.animations['cleave'][int(self.cleave_frame_index)]
                        flipped_image = pygame.transform.flip(image, True, False)
                        self.image = flipped_image
                        self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isDead:
                    self.death_frame_index += self.death_frame_speed

                    if int(self.death_frame_index) > len(self.animations['death']) - 1:

                        self.death_frame_index = 0
                    else:
                        image = self.animations['death'][int(self.death_frame_index)]
                        flipped_image = pygame.transform.flip(image, True, False)
                        self.image = flipped_image
                        self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isBreathing:
                    self.breath_frame_index += self.breath_frame_speed

                    if int(self.breath_frame_index) > len(self.animations['fire_breath']) - 1:

                        self.breath_frame_index = 0
                        self.isBreathing = False
                    else:
                        image = self.animations['fire_breath'][int(self.breath_frame_index)]
                        flipped_image = pygame.transform.flip(image, True, False)
                        self.image = flipped_image
                        self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isHurt:
                    self.hit_frame_index += self.hit_frame_speed

                    if int(self.hit_frame_index) > len(self.animations['hit']) - 1:

                        self.hit_frame_index = 0
                    else:
                        image = self.animations['hit'][int(self.hit_frame_index)]
                        flipped_image = pygame.transform.flip(image, True, False)
                        self.image = flipped_image
                        self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isIdle:
                    self.idle_frame_index += self.idle_frame_speed

                    if int(self.idle_frame_index) > len(self.animations['idle']) - 1:

                        self.idle_frame_index = 0
                    else:
                        image = self.animations['idle'][int(self.idle_frame_index)]
                        flipped_image = pygame.transform.flip(image, True, False)
                        self.image = flipped_image
                        self.rect = self.image.get_rect(topleft=self.rect.topleft)

                if self.isS_Hurt and self.isSlime:
                    self.s_hit_frame_index += self.s_hit_frame_speed

                    if int(self.s_hit_frame_index) > len(self.animations['slime_hit']) - 1:

                        self.s_hit_frame_index = 0
                    else:
                        image = self.animations['slime_hit'][int(self.s_hit_frame_index)]
                        flipped_image = pygame.transform.flip(image, True, False)
                        self.image = flipped_image
                        self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isS_Idle and self.isSlime:
                    self.s_idle_frame_index += self.s_idle_frame_speed

                    if int(self.s_idle_frame_index) > len(self.animations['slime_idle']) - 1:

                        self.s_idle_frame_index = 0
                    else:
                        image = self.animations['slime_idle'][int(self.s_idle_frame_index)]
                        flipped_image = pygame.transform.flip(image, True, False)
                        self.image = flipped_image
                        self.rect = self.image.get_rect(topleft=self.rect.topleft)

                if self.isS_Walk and self.isSlime:
                    self.s_walk_frame_index += self.s_walk_frame_speed

                    if int(self.s_walk_frame_index) > len(self.animations['slime_walk']) - 1:

                        self.s_walk_frame_index = 0
                    else:
                        image = self.animations['slime_walk'][int(self.s_walk_frame_index)]
                        flipped_image = pygame.transform.flip(image, True, False)
                        self.image = flipped_image
                        self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isSmash:
                    self.smash_frame_index += self.smash_frame_speed

                    if int(self.smash_frame_index) > len(self.animations['smash']) - 1:

                        self.smash_frame_index = 0
                        self.isSmash = False
                    else:
                        image = self.animations['smash'][int(self.smash_frame_index)]
                        flipped_image = pygame.transform.flip(image, True, False)
                        self.image = flipped_image
                        self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isTransforming:
                    self.transform_frame_index += self.transform_frame_speed
                    if int(self.transform_frame_index) > len(self.animations['transform']) - 1:

                        self.transform_frame_index = 0
                        self.isTransforming = False
                        self.isDemon = True
                        self.isAggro = True

                    else:
                        image = self.animations['transform'][int(self.transform_frame_index)]
                        flipped_image = pygame.transform.flip(image, True, False)
                        self.image = flipped_image
                        self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isWalking:
                    self.walk_frame_index += self.walk_frame_speed

                    if int(self.walk_frame_index) > len(self.animations['walk']) - 1:

                        self.walk_frame_index = 0
                    else:
                        image = self.animations['walk'][int(self.walk_frame_index)]
                        flipped_image = pygame.transform.flip(image, True, False)
                        self.image = flipped_image
                        self.rect = self.image.get_rect(topleft=self.rect.topleft) 
        
        
    def update(self, offset, player):        
        
        self.set_offset(offset)
        self.calculate_distance(player)
        self.apply_gravity()
        self.animate()