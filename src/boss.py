import pygame
import random
from import_assets import import_boss

class Boss(pygame.sprite.Sprite):
    def __init__(self, pos, data):
        
        super().__init__()
        
        #Import Assets
        self.import_boss_assets()
        
        # Frame indexes
        self.cleave_frame_index = 0
        self.death_frame_index = 0
        self.hit_frame_index = 0
        self.idle_frame_index = 0
        self.walk_frame_index = 0
        
        # Frame Speeds
        self.cleave_frame_speed = 0.5
        self.death_frame_speed = 0.5
        self.hit_frame_speed = 0.5
        self.idle_frame_speed = 0.5
        self.walk_frame_speed = 0.5
        
        # Init Frame
        self.image = self.animations['walk'][self.walk_frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        
        # Status
        self.isAnimating = False
        self.isAttacking = False
        self.isAggro = False
        self.isWalking = True
        self.isCleaving = False
        self.isDead = False
        self.isHurt = False
        
        # Sound
        self.death_sound = pygame.mixer.Sound("./media/demon_death.wav")
        self.death_slash = pygame.mixer.Sound("./media/demon_slash.wav")
        
        # Directional Info       
        self.facing_right = False
        self.wall_right = False
        self.wall_left = False
        self.direction = pygame.math.Vector2(0, 0)
        
        # Velocities
        self.speed = 2
        self.gravity = 0.5
        
        # Stats
        self.health = data['health']
        self.points = data['points']
        self.damage = 10
        
        #Coming Soon!
        # self.start_time = 0
        # self.spell_timer = 0 
        # self.breath_frame_index = 0
        # self.spell_frame_index = 0
        # self.s_hit_frame_index = 0
        # self.s_idle_frame_index = 0
        # self.s_walk_frame_index = 0
        # self.smash_frame_index = 0
        # self.transform_frame_index = 0
        # self.breath_frame_speed = 0.5
        # self.spell_frame_speed = 0.5
        # self.s_hit_frame_speed = 0.5
        # self.s_idle_frame_speed = 0.4
        # self.s_walk_frame_speed = 0.5
        # self.smash_frame_speed = 0.5
        # self.transform_frame_speed = 0.6
        # self.isSlime = True
        # self.isTransforming = False
        # self.isDemon = False
        # self.isCasting = False
        # self.isBreathing = False
        # self.isS_Hurt = False
        # self.isS_Idle = True
        # self.isS_Walk = False
        # self.isSmash = False
        # self.isIdle = False
        # self.slime_health = 80
        # self.fire_column = False
        # self.fire_ball = False
        
    def import_boss_assets(self):
        #Add Later: 'cast_spell': [], 'fire_breath': [], 'idle': [], 'slime_hit': [], 'slime_idle': [], 'slime_walk': [], 'smash': [], 'transform': []
        self.animations = {'cleave': [], 'death': [], 'hit': [], 'walk': []}    
        
        for animation in self.animations.keys():
            
            self.default_path = './assets/boss/'
            self.default_path += animation
            self.animations[animation] = import_boss(self.default_path)
    
    #Apply Gravity
    #Not required at this point in time
    def apply_gravity(self):
        
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    
    #Adjustment for scroller
    def set_offset(self, offset):

        self.rect.x += offset.x
        self.rect.y += offset.y
            
    #Determine event depending on distance from player
    def calculate_distance(self, player):
        
        boss_x = self.rect.centerx
        boss_y = self.rect.centery
        
        player_x = player.rect.centerx
        player_y = player.rect.centery

        loc_x_diff = boss_x - player_x
        loc_y_diff = boss_y - player_y
        
        if loc_x_diff < 1000 and loc_x_diff > -1000 and loc_y_diff < 600 and loc_y_diff > -600:
            self.isAnimating = True
            self.isAggro = True
        else:
            self.isAnimating = False
            #self.start_time = 0    

        if self.health <= 0:
            
            self.death_sound.play()
            self.isDead = True
            self.isAttacking = False
            self.isAggro = False
            self.isWalking = False
            #self.isCasting = False
            self.isCleaving = False
            #self.isBreathing = False
            self.isHurt = False
            #self.isIdle = False
            #self.isS_Hurt = False
            #self.isS_Idle = False
            #self.isS_Walk = False
            #self.isSmash = False
        #Issue: Need to trigger only once
        #elif self.health < (self.health/2) and self.isHurt == False and self.isDead == False:
            #self.isDead = False
            #self.isAttacking = False
            #self.isAggro = False
            #self.isWalking = False
            #self.isCasting = False
            #self.isCleaving = False
            #self.isBreathing = False
            #self.isHurt = True
            #self.isIdle = False
            #self.isS_Hurt = False
            #self.isS_Idle = True
            #self.isS_Walk = False
            #self.isSmash = False
        else:
            self.isHurt = False    
            self.boss_logic(loc_x_diff, loc_y_diff)
        
    def boss_logic(self, x_diff, y_diff):
         
        # Get direction
        if x_diff > 0 and self.isAggro and self.isCleaving == False:
            self.facing_right = False
        elif x_diff < 0 and self.isAggro and self.isCleaving == False:    
            self.facing_right = True
        
        #Coming Soon!
        #Collision 
        # if (self.wall_left and not self.facing_right) and self.isSlime:
        #     self.isS_Walk = False
        #     self.isS_Idle = True
        # elif(self.wall_right and self.facing_right) and self.isSlime:
        #     self.isS_Walk = False
        #     self.isS_Idle = True
        # elif(self.wall_left and not self.facing_right) and self.isDemon:
        #     self.isWalking = False
        #     self.isIdle = True
        # elif(self.wall_right and self.facing_right) and self.isDemon:
        #     self.isWalking = False
        #     self.isIdle = True
        
        #Add later: self.isCasting, self.isBreathing, self.isSmash      
        #Check if attacking
        # if  self.isCleaving:
        #     self.isAttacking = True
        #     self.isWalking = False
        #     #self.isIdle = False
        # else:
        #     self.isAttacking = False 
            
        # if not self.isAggro and self.isAnimating and not self.isTransforming and self.isSlime:
        #     self.randomize_movement()

        #     if self.isS_Walk and self.isSlime:
        #         self.isS_Idle = False
        #         if self.facing_right and not self.wall_right:
        #             self.s_walk_frame_speed = 0.3
        #             self.speed = 2
        #             self.rect.x += self.speed
                    
        #         elif not self.facing_right and not self.wall_left:
        #             self.speed = 2
        #             self.rect.x -= self.speed
                    
        #             self.walk_frame_speed = 0.3
        #Add later: self.isDemon 
        if self.isAggro:    
            if x_diff <= 60 and x_diff >= -60 and self.isAttacking == False:

                self.isWalking = False
                self.isCleaving = True
                    
            if x_diff > 60 and self.isCleaving== False and not self.wall_left:
                self.isWalking = True
                self.walk_frame_speed = 0.6
                self.speed = 6
                self.rect.x -= self.speed        
                    
            if x_diff < -60 and self.isCleaving == False and not self.wall_right:
                self.isWalking = True
                self.walk_frame_speed = 0.6   
                self.speed = 6 
                self.rect.x += self.speed
            
            #Coming Soon!        
            #Random attack        
            # if (x_diff < 20 and x_diff > -20) and (y_diff < 20 and y_diff > -20) and not self.isAttacking:
            #     self.randomize_movement()
            #     self.isWalking = False 
        
        #Coming Soon!
        #Transform
        # if(self.slime_health <= 0 and not self.isTransforming and not self.isAggro):
        #     self.isTransforming = True
        #     self.isS_Walk = False
        #     self.isS_Idle = False
        #     self.isS_Hurt = False                    
        #     self.isSlime = False

          
    #Coming Soon!
    #Randomize event if boss isSlime or isDemon        
    def randomize_movement(self):
        
        time = pygame.time.get_ticks() - self.start_time
        random_time = random.randint(3000, 5000)
        
        if(time > random_time) and self.isSlime:
            
            result = random.randint(1,4)
            self.start_time = pygame.time.get_ticks()
            
            #Turn right and walk
            if(result == 1):
                self.facing_right = True
                self.isS_Walk = True
                
            #Turn left and walk
            elif(result == 2):
                self.facing_right = False
                self.isS_Walk = True
            
            #Turn right and idle
            elif(result == 3):
                self.facing_right = True
                self.isS_Walk = False
                self.isS_Idle = True
                
            #Turn left and idle 
            elif(result == 4):
                self.isS_Walk = False
                self.isS_Idle = True
                self.facing_right = False      
        
        elif(time > random_time) and self.isDemon:
            
            result = random.randint(1,4)
            self.start_time = pygame.time.get_ticks()
            
            if(result == 1):
                self.isCleaving = True
                
            elif(result == 2):
                self.isBreathing = True
            
            elif(result == 3):
                self.isSmash = True
                
            elif(result == 4):
                self.isCleaving = True
                
    #Commented sections are work in progress    
    def animate(self):
        
        if not self.isAnimating:
            return
        if self.isAnimating:
            
            if not self.facing_right:
            
                # if self.isCasting:
                #     self.spell_frame_index += self.spell_frame_speed

                #     if int(self.spell_frame_index) > len(self.animations['cast_spell']) - 1:

                #         self.spell_frame_index = 0
                #         self.isCasting = False
                #     else:
                #         self.image = self.animations['cast_spell'][int(self.spell_frame_index)]
                #         self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isCleaving:
                    self.cleave_frame_index += self.cleave_frame_speed

                    if int(self.cleave_frame_index) > len(self.animations['cleave']) - 1:

                        self.cleave_frame_index = 0
                        self.isCleaving = False
                    else:
                        self.image = self.animations['cleave'][int(self.cleave_frame_index)]
                        self.rect = self.image.get_rect(topleft=self.rect.topleft)

                    if self.cleave_frame_index >= 10 and self.cleave_frame_index < 11:
                        self.death_slash.play()
                    
                    if self.cleave_frame_index >= 10 and self.cleave_frame_index <= 12:
                        self.isAttacking = True
                    else:
                        self.isAttacking = False
                if self.isDead:
                    self.death_frame_index += self.death_frame_speed

                    if int(self.death_frame_index) > len(self.animations['death']) - 1:

                        self.death_frame_index = 0
                        self.kill()
                    else:
                        self.image = self.animations['death'][int(self.death_frame_index)]
                        self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                # if self.isBreathing:
                #     self.breath_frame_index += self.breath_frame_speed

                #     if int(self.breath_frame_index) > len(self.animations['fire_breath']) - 1:

                #         self.breath_frame_index = 0
                #         self.isBreathing = False
                #     else:
                #         self.image = self.animations['fire_breath'][int(self.breath_frame_index)]
                #         self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isHurt:
                    self.hit_frame_index += self.hit_frame_speed

                    if int(self.hit_frame_index) > len(self.animations['hit']) - 1:

                        self.hit_frame_index = 0
                        self.isHurt = False
                    else:
                        self.image = self.animations['hit'][int(self.hit_frame_index)]
                        self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                # if self.isIdle:
                #     self.idle_frame_index += self.idle_frame_speed

                #     if int(self.idle_frame_index) > len(self.animations['idle']) - 1:

                #         self.idle_frame_index = 0
                #     else:
                #         self.image = self.animations['idle'][int(self.idle_frame_index)]
                #         self.rect = self.image.get_rect(topleft=self.rect.topleft)

                # if self.isS_Hurt and self.isSlime:
                #     self.s_hit_frame_index += self.s_hit_frame_speed

                #     if int(self.s_hit_frame_index) > len(self.animations['slime_hit']) - 1:

                #         self.s_hit_frame_index = 0
                #         self.isS_Hurt = False
                        
                #     else:
                #         self.image = self.animations['slime_hit'][int(self.s_hit_frame_index)]
                #         self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                # if self.isS_Idle and self.isSlime:
                #     self.s_idle_frame_index += self.s_idle_frame_speed

                #     if int(self.s_idle_frame_index) > len(self.animations['slime_idle']) - 1:

                #         self.s_idle_frame_index = 0
                #     else:
                #         self.image = self.animations['slime_idle'][int(self.s_idle_frame_index)]
                #         self.rect = self.image.get_rect(topleft=self.rect.topleft)

                # if self.isS_Walk and self.isSlime:
                #     self.s_walk_frame_index += self.s_walk_frame_speed

                #     if int(self.s_walk_frame_index) > len(self.animations['slime_walk']) - 1:

                #         self.s_walk_frame_index = 0
                #     else:
                #         self.image = self.animations['slime_walk'][int(self.s_walk_frame_index)]
                #         self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                # if self.isSmash:
                #     self.smash_frame_index += self.smash_frame_speed

                #     if int(self.smash_frame_index) > len(self.animations['smash']) - 1:

                #         self.smash_frame_index = 0
                #         self.isSmash = False
                #     else:
                #         self.image = self.animations['smash'][int(self.smash_frame_index)]
                #         self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                # if self.isTransforming:
                #     self.transform_frame_index += self.transform_frame_speed
                #     if int(self.transform_frame_index) > len(self.animations['transform']) - 1:

                #         self.transform_frame_index = 0
                #         self.isTransforming = False
                #         self.isDemon = True
                #         self.isAggro = True
                    
                #     else:
                #         self.image = self.animations['transform'][int(self.transform_frame_index)]
                #         self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isWalking:
                    self.walk_frame_index += self.walk_frame_speed

                    if int(self.walk_frame_index) > len(self.animations['walk']) - 1:

                        self.walk_frame_index = 0
                    else:
                        self.image = self.animations['walk'][int(self.walk_frame_index)]
                        self.rect = self.image.get_rect(topleft=self.rect.topleft)                                
            # Facing Right    
            else:     
                # if self.isCasting:
                #     self.spell_frame_index += self.spell_frame_speed

                #     if int(self.spell_frame_index) > len(self.animations['cast_spell']) - 1:

                #         self.spell_frame_index = 0
                #         self.isCasting = False
                #     else:
                #         image = self.animations['cast_spell'][int(self.spell_frame_index)]
                #         flipped_image = pygame.transform.flip(image, True, False)
                #         self.image = flipped_image
                #         self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
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

                    if self.cleave_frame_index >= 10 and self.cleave_frame_index < 11:
                        self.death_slash.play()
                    
                    if self.cleave_frame_index >= 10 and self.cleave_frame_index <= 12:
                        self.isAttacking = True
                    else:
                        self.isAttacking = False
                    
                if self.isDead:
                    self.death_frame_index += self.death_frame_speed

                    if int(self.death_frame_index) > len(self.animations['death']) - 1:

                        self.death_frame_index = 0
                        self.kill()
                        
                    else:
                        image = self.animations['death'][int(self.death_frame_index)]
                        flipped_image = pygame.transform.flip(image, True, False)
                        self.image = flipped_image
                        self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                # if self.isBreathing:
                #     self.breath_frame_index += self.breath_frame_speed

                #     if int(self.breath_frame_index) > len(self.animations['fire_breath']) - 1:

                #         self.breath_frame_index = 0
                #         self.isBreathing = False
                #     else:
                #         image = self.animations['fire_breath'][int(self.breath_frame_index)]
                #         flipped_image = pygame.transform.flip(image, True, False)
                #         self.image = flipped_image
                #         self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isHurt:
                    self.hit_frame_index += self.hit_frame_speed

                    if int(self.hit_frame_index) > len(self.animations['hit']) - 1:

                        self.hit_frame_index = 0
                        self.isHurt = False
                        
                    else:
                        image = self.animations['hit'][int(self.hit_frame_index)]
                        flipped_image = pygame.transform.flip(image, True, False)
                        self.image = flipped_image
                        self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                # if self.isIdle:
                #     self.idle_frame_index += self.idle_frame_speed

                #     if int(self.idle_frame_index) > len(self.animations['idle']) - 1:

                #         self.idle_frame_index = 0
                #     else:
                #         image = self.animations['idle'][int(self.idle_frame_index)]
                #         flipped_image = pygame.transform.flip(image, True, False)
                #         self.image = flipped_image
                #         self.rect = self.image.get_rect(topleft=self.rect.topleft)

                # if self.isS_Hurt and self.isSlime:
                #     self.s_hit_frame_index += self.s_hit_frame_speed

                #     if int(self.s_hit_frame_index) > len(self.animations['slime_hit']) - 1:

                #         self.s_hit_frame_index = 0
                #         self.isS_Hurt = False
                        
                #     else:
                #         image = self.animations['slime_hit'][int(self.s_hit_frame_index)]
                #         flipped_image = pygame.transform.flip(image, True, False)
                #         self.image = flipped_image
                #         self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                # if self.isS_Idle and self.isSlime:
                #     self.s_idle_frame_index += self.s_idle_frame_speed

                #     if int(self.s_idle_frame_index) > len(self.animations['slime_idle']) - 1:

                #         self.s_idle_frame_index = 0
                #     else:
                #         image = self.animations['slime_idle'][int(self.s_idle_frame_index)]
                #         flipped_image = pygame.transform.flip(image, True, False)
                #         self.image = flipped_image
                #         self.rect = self.image.get_rect(topleft=self.rect.topleft)

                # if self.isS_Walk and self.isSlime:
                #     self.s_walk_frame_index += self.s_walk_frame_speed

                #     if int(self.s_walk_frame_index) > len(self.animations['slime_walk']) - 1:

                #         self.s_walk_frame_index = 0
                #     else:
                #         image = self.animations['slime_walk'][int(self.s_walk_frame_index)]
                #         flipped_image = pygame.transform.flip(image, True, False)
                #         self.image = flipped_image
                #         self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                # if self.isSmash:
                #     self.smash_frame_index += self.smash_frame_speed

                #     if int(self.smash_frame_index) > len(self.animations['smash']) - 1:

                #         self.smash_frame_index = 0
                #         self.isSmash = False
                #     else:
                #         image = self.animations['smash'][int(self.smash_frame_index)]
                #         flipped_image = pygame.transform.flip(image, True, False)
                #         self.image = flipped_image
                #         self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                # if self.isTransforming:
                #     self.transform_frame_index += self.transform_frame_speed
                #     if int(self.transform_frame_index) > len(self.animations['transform']) - 1:

                #         self.transform_frame_index = 0
                #         self.isTransforming = False
                #         self.isDemon = True
                #         self.isAggro = True

                #     else:
                #         image = self.animations['transform'][int(self.transform_frame_index)]
                #         flipped_image = pygame.transform.flip(image, True, False)
                #         self.image = flipped_image
                #         self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
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