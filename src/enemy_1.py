import pygame
import random
from import_assets import import_enemy_1

class Enemy_1(pygame.sprite.Sprite):
    def __init__(self, pos):
        
        super().__init__()
        self.import_enemy_1_assets()
        
        self.attack_frame_index = 0
        self.death_frame_index = 0
        self.hurt_frame_index = 0
        self.idle_frame_index = 0
        self.react_frame_index = 0
        self.walk_frame_index = 0
        
        self.attack_frame_speed = 0.5
        self.death_frame_speed = 0.2
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
        
        self.image = self.animations['idle'][self.idle_frame_index]
        self.rect = self.image.get_rect(topleft=pos)        
    
    def import_enemy_1_assets(self):
        
        self.animations = {'attack': [], 'death': [], 'hurt': [], 'idle': [], 'react': [], 'walk': []}    
        
        for animation in self.animations.keys():
            
            self.default_path = './assets/enemies/skeleton/'
            self.default_path += animation
            self.animations[animation] = import_enemy_1(self.default_path)
    
    def calculate_distance(self, player): 
    
        skeleton_x = self.rect.x
        skeleton_y = self.rect.y
        
        player_x = player.rect.x
        player_y = player.rect.y
        
        loc_x_diff = skeleton_x - player_x
        loc_y_diff = skeleton_y - player_y
        
        
        print("Skel:" + str(skeleton_x))
        print("player:" + str(player_x))
        print("diff:" + str(loc_x_diff))
        
        #Check for animation and movement
        if loc_x_diff < 400 and loc_x_diff > -400:
            self.isAnimating = True
        else:
            self.isAnimating = False   
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
    
    def randomize_movement(self):
        
        result = random.randint(1,)
    
        #idle - even
       
        #walk - odd
       
        #turn right and walk
        
        #turn right and idle
        
        #turn left and walk
        
        #turn left and idle 


    def enemy_logic(self, x_diff, y_diff):
        
        if x_diff > 0 and self.isAggro and not self.isAttacking:
            self.facing_right = False
        elif x_diff < 0 and self.isAggro and not self.isAttacking:    
            self.facing_right = True
            
        if not self.isAggro:
            return
        
        elif self.isReact:
            if x_diff > 0:
                self.isWalking = False
                #Add more maybe
            if x_diff < 0:    
                self.isWalking = False
        else:    
            if self.isAggro:    
                if x_diff > 10 and not self.isAttacking:
                    self.isAttacking = False
                    self.isWalking = True
                    self.rect.x -= 3
                    
                if x_diff < -10 and not self.isAttacking:
                    self.isAttacking = False
                    self.isWalking = True    
                    self.rect.x += 3
                    
                if (x_diff < 20 and x_diff > -20) and  (y_diff < 20 and y_diff > -20) or self.isAttacking:
                    self.isAttacking = True    
                    self.isWalking = False 
            else:
                #Maybe take out when adding random movement
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

                    image = self.animations['death'][int(self.death_frame_index)]
                    flipped_image = pygame.transform.flip(image, True, False)
                    self.image = flipped_image
                    self.rect = self.image.get_rect(topleft=self.rect.topleft) 
                
                
    def update(self, player):
        
        self.calculate_distance(player)
        self.animate()    