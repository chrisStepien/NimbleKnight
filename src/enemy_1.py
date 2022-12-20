import pygame
import random
from import_assets import import_enemy_1

class Enemy_1(pygame.sprite.Sprite):
    def __init__(self, pos, data):
        
        super().__init__()
        self.import_enemy_1_assets()
        
        self.attack_frame_index = 0
        self.death_frame_index = 0
        self.hurt_frame_index = 0
        self.idle_frame_index = 0
        self.react_frame_index = 0
        self.walk_frame_index = 0
        
        self.attack_frame_speed = 0.5
        self.death_frame_speed = 0.7
        self.hurt_frame_speed = 0.2
        self.idle_frame_speed = 0.2
        self.react_frame_speed = 0.2
        self.walk_frame_speed = 0.3
        
        self.isAggro = False
        self.isAnimating = False
        self.isAttacking = False
        self.isWalking = False
        self.isHurt = False
        self.isIdle = True
        self.isDead = False
        self.isReact = False
        
        self.facing_right = True
        self.wall_right = False
        self.wall_left = False
        
        self.speed = 2
        #health or just one hit
        self.direction = pygame.math.Vector2(0, 0)
        self.gravity = 0.5
        
        self.health = data['health']
        self.damage = 1
        self.points = data['points']
        self.time = data['time']
        self.start_time = 0
        
        self.image = self.animations['idle'][self.idle_frame_index]
        self.rect = self.image.get_rect(topleft=pos)        
    
        
    def import_enemy_1_assets(self):
        
        self.animations = {'attack': [], 'death': [], 'hurt': [], 'idle': [], 'react': [], 'walk': []}    
        
        for animation in self.animations.keys():
            
            self.default_path = './assets/enemies/skeleton/'
            self.default_path += animation
            self.animations[animation] = import_enemy_1(self.default_path)
    
    def apply_gravity(self):
        
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    
    def calculate_distance(self, player): 
    
        skeleton_x = self.rect.x
        skeleton_y = self.rect.y
        
        player_x = player.rect.x
        player_y = player.rect.y
        
        loc_x_diff = skeleton_x - player_x
        loc_y_diff = skeleton_y - player_y
        #Check for animation and movement
        if loc_x_diff < 1000 and loc_x_diff > -1000:
            self.isAnimating = True
        else:
            self.isAnimating = False
            self.start_time = 0
                
        if self.health <= 0:
            self.isDead = True
            self.isAttacking = False
            self.isWalking = False
            self.isHurt = False
            self.isIdle = False
            self.isReact = False
        else:    
            
            #Check for player aggro    
            if (loc_x_diff < 200 and loc_x_diff > -200) and (loc_y_diff < 100 and loc_y_diff > -100) and self.isAggro:
                self.isAggro = True
            elif (loc_x_diff < 200 and loc_x_diff > -200) and (loc_y_diff < 100 and loc_y_diff > -100) and not self.isAggro:
                self.isAggro = True
                self.isReact = True
            else:
                self.isAggro = False                
            #Check for attacking distance    
            if (loc_x_diff < 50 and loc_x_diff > -50) and (loc_y_diff < 32 and loc_y_diff > -32) or self.isAttacking:
                self.isAttacking = True
            else:
                self.isAttacking = False    
            
            self.enemy_logic(loc_x_diff, loc_y_diff)
            
    #Randomizes when event occurs and what event occurs
    def randomize_movement(self):
        time = pygame.time.get_ticks() - self.start_time
        random_time = random.randint(4000, 8000)
        if(time > random_time):
            result = random.randint(1, 4)
            self.start_time = pygame.time.get_ticks()
            #Turn right and walk
            if(result == 1):
                self.facing_right = True
                self.isWalking = True
                
            #Turn left and walk
            elif(result == 2):
                self.facing_right = False
                self.isWalking = True
            
            #Turn right and idle
            elif(result == 3):
                self.facing_right = True
                self.isWalking = False
                self.isIdle = True
                
            #Turn left and idle 
            elif(result == 4):
                self.isWalking = False
                self.isIdle = True
                self.facing_right = False

    def enemy_logic(self, x_diff, y_diff):
        # Get direction
        if x_diff > 0 and self.isAggro and not self.isAttacking:
            self.facing_right = False
        elif x_diff < 0 and self.isAggro and not self.isAttacking:    
            self.facing_right = True
        
        #Collision
        if (self.wall_left and not self.facing_right):
            self.isWalking = False
            self.isIdle = True  
        elif(self.wall_right and self.facing_right):
            self.isWalking = False
            self.isIdle = True  
    
        #Movement logic    
        if not self.isAggro and self.isAnimating:
              
            self.randomize_movement()
            
            if self.isWalking:
                
                if self.facing_right and not self.wall_right:
                    self.walk_frame_speed = 0.3
                    self.speed = 2
                    self.rect.x += self.speed
                elif not self.facing_right and not self.wall_left:
                    self.speed = 2
                    self.rect.x -= self.speed
                    self.walk_frame_speed = 0.3     
                else:
                    self.isWalking = False    
        elif self.isReact:
            if x_diff > 0:
                self.isWalking = False
                #Add more maybe
            if x_diff < 0:    
                self.isWalking = False
        else:    
            if self.isAggro:
                if x_diff <= 10 and x_diff >= -10 and not self.isAttacking:

                    self.isWalking = False
                    self.isIdle = True
                    
                if x_diff > 10 and not self.isAttacking and not self.wall_left:
                    self.isWalking = True
                    self.walk_frame_speed = 0.6
                    self.speed = 4
                    self.rect.x -= self.speed
                    
                if x_diff < -10 and not self.isAttacking and not self.wall_right:
                    self.isWalking = True
                    self.walk_frame_speed = 0.6   
                    self.speed = 4 
                    self.rect.x += self.speed
                    
                if (x_diff < 20 and x_diff > -20) and  (y_diff < 20 and y_diff > -20) or self.isAttacking:
                    self.isAttacking = True    
                    self.isWalking = False 
            else:
                #Maybe take out when adding random movement
                #add to put everything top false maybe
                self.isWalking = False
                    
        #Add another boolean to check for react and set false if true and check to activate if both true    
            
    def animate(self):
        
        if not self.isAnimating:
            return
        if self.isAnimating:
           
            if self.facing_right:
                
                if self.isIdle:
                    self.idle_frame_index += self.idle_frame_speed

                    if int(self.idle_frame_index) > len(self.animations['idle']) - 1:

                        self.idle_frame_index = 0

                    self.image = self.animations['idle'][int(self.idle_frame_index)]
                    self.rect = self.image.get_rect(topleft=self.rect.topleft)   

                if self.isWalking:
                    self.walk_frame_index += self.walk_frame_speed

                    if int(self.walk_frame_index) > len(self.animations['walk']) - 1:

                        self.walk_frame_index = 0

                    self.image = self.animations['walk'][int(self.walk_frame_index)]
                    self.rect = self.image.get_rect(topleft=self.rect.topleft)   

                if self.isReact:
                    self.react_frame_index += self.react_frame_speed

                    if int(self.react_frame_index) > len(self.animations['react']) - 1:

                        self.react_frame_index = 0
                        self.isReact = False 
                        
                        
                    self.image = self.animations['react'][int(self.react_frame_index)]
                    self.rect = self.image.get_rect(topleft=self.rect.topleft)   

                if self.isAttacking:
                    self.attack_frame_index += self.attack_frame_speed

                    if int(self.attack_frame_index) > len(self.animations['attack']) - 1:

                        self.attack_frame_index = 0
                        self.isAttacking = False 
                            
                    self.image = self.animations['attack'][int(self.attack_frame_index)]
                    self.rect = self.image.get_rect(topleft=self.rect.topleft)   

                if self.isHurt:
                    self.hurt_frame_index += self.hurt_frame_speed

                    if int(self.hurt_frame_index) > len(self.animations['hurt']) - 1:

                        self.hurt_frame_index = 0

                    self.image = self.animations['hurt'][int(self.hurt_frame_index)]
                    self.rect = self.image.get_rect(topleft=self.rect.topleft)   

                if self.isDead:
                    self.death_frame_index += self.death_frame_speed

                    if int(self.death_frame_index) > len(self.animations['death']) - 1:

                        self.death_frame_index = 0
                        self.kill()
                        
                    self.image = self.animations['death'][int(self.death_frame_index)]
                    self.rect = self.image.get_rect(topleft=self.rect.topleft)   
            
            # Facing Left
            else:
                
                if self.isIdle:
                    self.idle_frame_index += self.idle_frame_speed

                    if int(self.idle_frame_index) > len(self.animations['idle']) - 1:

                        self.idle_frame_index = 0

                    image = self.animations['idle'][int(self.idle_frame_index)]
                    flipped_image = pygame.transform.flip(image, True, False)
                    self.image = flipped_image
                    
                    self.rect = self.image.get_rect(topleft=self.rect.topleft)   

                if self.isWalking:
                    self.walk_frame_index += self.walk_frame_speed

                    if int(self.walk_frame_index) > len(self.animations['walk']) - 1:

                        self.walk_frame_index = 0

                    image = self.animations['walk'][int(self.walk_frame_index)]
                    flipped_image = pygame.transform.flip(image, True, False)
                    self.image = flipped_image
                    self.rect = self.image.get_rect(topleft=self.rect.topleft)   

                if self.isReact:
                    self.react_frame_index += self.react_frame_speed

                    if int(self.react_frame_index) > len(self.animations['react']) - 1:

                        self.react_frame_index = 0
                        self.isReact = False 

                    image = self.animations['react'][int(self.react_frame_index)]
                    flipped_image = pygame.transform.flip(image, True, False)
                    self.image = flipped_image
                    self.rect = self.image.get_rect(topleft=self.rect.topleft)   

                if self.isAttacking:
                    self.attack_frame_index += self.attack_frame_speed

                    if int(self.attack_frame_index) > len(self.animations['attack']) - 1:

                        self.attack_frame_index = 0
                        self.isAttacking = False 
                        

                    image = self.animations['attack'][int(self.attack_frame_index)]
                    flipped_image = pygame.transform.flip(image, True, False)
                    self.image = flipped_image
                    self.rect = self.image.get_rect(topleft=self.rect.topleft)   

                if self.isHurt:
                    self.hurt_frame_index += self.hurt_frame_speed

                    if int(self.hurt_frame_index) > len(self.animations['hurt']) - 1:

                        self.hurt_frame_index = 0

                    image = self.animations['hurt'][int(self.hurt_frame_index)]
                    flipped_image = pygame.transform.flip(image, True, False)
                    self.image = flipped_image
                    self.rect = self.image.get_rect(topleft=self.rect.topleft)   

                if self.isDead:
                    self.death_frame_index += self.death_frame_speed

                    if int(self.death_frame_index) > len(self.animations['death']) - 1:

                        self.death_frame_index = 0
                        self.kill()
                        

                    image = self.animations['death'][int(self.death_frame_index)]
                    flipped_image = pygame.transform.flip(image, True, False)
                    self.image = flipped_image
                    self.rect = self.image.get_rect(topleft=self.rect.topleft) 
                
    def set_offset(self, offset):
        
        self.rect.x += offset.x
        self.rect.y += offset.y
        
                
    def update(self, offset, player):
        
        self.set_offset(offset)
        self.calculate_distance(player)
        self.apply_gravity()
        self.animate()    