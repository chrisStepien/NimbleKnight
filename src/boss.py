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
        
        self.image = self.animations['idle'][self.idle_frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        
        # Frame speeds
        self.spell_frame_speed = 0.5
        self.cleave_frame_speed = 0.5
        self.death_frame_speed = 0.5
        self.breath_frame_speed = 0.5
        self.hit_frame_speed = 0.5
        self.idle_frame_speed = 0.5
        self.s_hit_frame_speed = 0.5
        self.s_idle_frame_speed = 0.5
        self.s_walk_frame_speed = 0.5
        self.smash_frame_speed = 0.5
        self.transform_frame_speed = 0.5
        self.walk_frame_speed = 0.5

        # Demon slime status
        self.isSlime = True
        self.isTransforming = False
        self.isDemon = False
        
        
        
        self.isAnimating = True
        self.isAggro = False
        self.isWalking = False
        self.isCasting = False
        self.isCleaving = False
        self.isDead = False
        self.isBreathing = False
        self.isHurt = False
        self.isIdle = True
        self.isS_Hurt = False
        self.isS_Idle = False
        self.isS_Walk = False
        self.isSmash = False
        self.isTransforming = False
        self.isWalking = False
        
        self.facing_right = False
        self.wall_right = False
        self.wall_left = False
        
        self.speed = 6
        
        self.start_time = 0
        
        
        
        
    def import_boss_assets(self):
        
        self.animations = {'cast_spell': [], 'cleave': [], 'death': [], 'fire_breath': [], 'hit': [], 'idle': [], 'slime_hit': [], 'slime_idle': [], 'slime_walk': [], 'smash': [], 'transform': [], 'walk': []}    
        
        for animation in self.animations.keys():
            
            self.default_path = './assets/boss/'
            self.default_path += animation
            self.animations[animation] = import_boss(self.default_path)
    
    #apply gravity
    
    #calculate distance
    
    #random attack
    
    #spells maybe?
    
    
    
    
    def animate(self):
        
        if not self.isAnimating:
            return
        if self.isAnimating:
            
            if not self.facing_right:
            
                if self.isCasting:
                    self.spell_frame_index += self.spell_frame_speed

                    if int(self.spell_frame_index) > len(self.animations['cast_spell']) - 1:

                        self.spell_frame_index = 0

                    self.image = self.animations['cast_spell'][int(self.spell_frame_index)]
                    self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isCleaving:
                    self.cleave_frame_index += self.cleave_frame_speed

                    if int(self.cleave_frame_index) > len(self.animations['cleave']) - 1:

                        self.cleave_frame_index = 0

                    self.image = self.animations['cleave'][int(self.cleave_frame_index)]
                    self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isDead:
                    self.death_frame_index += self.death_frame_speed

                    if int(self.death_frame_index) > len(self.animations['death']) - 1:

                        self.death_frame_index = 0

                    self.image = self.animations['death'][int(self.death_frame_index)]
                    self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isBreathing:
                    self.breath_frame_index += self.breath_frame_speed

                    if int(self.breath_frame_index) > len(self.animations['fire_breath']) - 1:

                        self.breath_frame_index = 0

                    self.image = self.animations['fire_breath'][int(self.breath_frame_index)]
                    self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isHurt:
                    self.hit_frame_index += self.hit_frame_speed

                    if int(self.hit_frame_index) > len(self.animations['hit']) - 1:

                        self.hit_frame_index = 0

                    self.image = self.animations['hit'][int(self.hit_frame_index)]
                    self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isIdle:
                    self.idle_frame_index += self.idle_frame_speed

                    if int(self.idle_frame_index) > len(self.animations['idle']) - 1:

                        self.idle_frame_index = 0

                    self.image = self.animations['idle'][int(self.idle_frame_index)]
                    self.rect = self.image.get_rect(topleft=self.rect.topleft)

                if self.isS_Hurt:
                    self.s_hit_frame_index += self.s_hit_frame_speed

                    if int(self.s_hit_frame_index) > len(self.animations['slime_hit']) - 1:

                        self.s_hit_frame_index = 0

                    self.image = self.animations['slime_hit'][int(self.s_hit_frame_index)]
                    self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isS_Idle:
                    self.s_idle_frame_index += self.s_idle_frame_speed

                    if int(self.s_idle_frame_index) > len(self.animations['slime_idle']) - 1:

                        self.s_idle_frame_index = 0

                    self.image = self.animations['slime_idle'][int(self.s_idle_frame_index)]
                    self.rect = self.image.get_rect(topleft=self.rect.topleft)

                if self.isS_Walk:
                    self.s_walk_frame_index += self.s_walk_frame_speed

                    if int(self.s_walk_frame_index) > len(self.animations['slime_walk']) - 1:

                        self.s_walk_frame_index = 0

                    self.image = self.animations['slime_walk'][int(self.s_walk_frame_index)]
                    self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isSmash:
                    self.smash_frame_index += self.smash_frame_speed

                    if int(self.smash_frame_index) > len(self.animations['smash']) - 1:

                        self.smash_frame_index = 0

                    self.image = self.animations['smash'][int(self.smash_frame_index)]
                    self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isTransforming:
                    self.transform_frame_index += self.transform_frame_speed

                    if int(self.transform_frame_index) > len(self.animations['transform']) - 1:

                        self.transform_frame_index = 0

                    self.image = self.animations['transform'][int(self.transform_frame_index)]
                    self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isWalking:
                    self.walk_frame_index += self.walk_frame_speed

                    if int(self.walk_frame_index) > len(self.animations['walk']) - 1:

                        self.walk_frame_index = 0

                    self.image = self.animations['walk'][int(self.walk_frame_index)]
                    self.rect = self.image.get_rect(topleft=self.rect.topleft)                                
            # Facing Left    
            else:     
                if self.isCasting:
                    self.spell_frame_index += self.spell_frame_speed

                    if int(self.spell_frame_index) > len(self.animations['cast_spell']) - 1:

                        self.spell_frame_index = 0

                    image = self.animations['cast_spell'][int(self.spell_frame_index)]
                    flipped_image = pygame.transform.flip(image, True, False)
                    self.image = flipped_image
                    self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isCleaving:
                    self.cleave_frame_index += self.cleave_frame_speed

                    if int(self.cleave_frame_index) > len(self.animations['cleave']) - 1:

                        self.cleave_frame_index = 0

                    image = self.animations['cleave'][int(self.cleave_frame_index)]
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
                
                if self.isBreathing:
                    self.breath_frame_index += self.breath_frame_speed

                    if int(self.breath_frame_index) > len(self.animations['fire_breath']) - 1:

                        self.breath_frame_index = 0

                    image = self.animations['fire_breath'][int(self.breath_frame_index)]
                    flipped_image = pygame.transform.flip(image, True, False)
                    self.image = flipped_image
                    self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isHurt:
                    self.hit_frame_index += self.hit_frame_speed

                    if int(self.hit_frame_index) > len(self.animations['hit']) - 1:

                        self.hit_frame_index = 0

                    image = self.animations['hit'][int(self.hit_frame_index)]
                    flipped_image = pygame.transform.flip(image, True, False)
                    self.image = flipped_image
                    self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isIdle:
                    self.idle_frame_index += self.idle_frame_speed

                    if int(self.idle_frame_index) > len(self.animations['idle']) - 1:

                        self.idle_frame_index = 0

                    image = self.animations['idle'][int(self.idle_frame_index)]
                    flipped_image = pygame.transform.flip(image, True, False)
                    self.image = flipped_image
                    self.rect = self.image.get_rect(topleft=self.rect.topleft)

                if self.isS_Hurt:
                    self.s_hit_frame_index += self.s_hit_frame_speed

                    if int(self.s_hit_frame_index) > len(self.animations['slime_hit']) - 1:

                        self.s_hit_frame_index = 0

                    image = self.animations['slime_hit'][int(self.s_hit_frame_index)]
                    flipped_image = pygame.transform.flip(image, True, False)
                    self.image = flipped_image
                    self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isS_Idle:
                    self.s_idle_frame_index += self.s_idle_frame_speed

                    if int(self.s_idle_frame_index) > len(self.animations['slime_idle']) - 1:

                        self.s_idle_frame_index = 0

                    image = self.animations['slime_idle'][int(self.s_idle_frame_index)]
                    flipped_image = pygame.transform.flip(image, True, False)
                    self.image = flipped_image
                    self.rect = self.image.get_rect(topleft=self.rect.topleft)

                if self.isS_Walk:
                    self.s_walk_frame_index += self.s_walk_frame_speed

                    if int(self.s_walk_frame_index) > len(self.animations['slime_walk']) - 1:

                        self.s_walk_frame_index = 0

                    image = self.animations['slime_walk'][int(self.s_walk_frame_index)]
                    flipped_image = pygame.transform.flip(image, True, False)
                    self.image = flipped_image
                    self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isSmash:
                    self.smash_frame_index += self.smash_frame_speed

                    if int(self.smash_frame_index) > len(self.animations['smash']) - 1:

                        self.smash_frame_index = 0

                    image = self.animations['smash'][int(self.smash_frame_index)]
                    flipped_image = pygame.transform.flip(image, True, False)
                    self.image = flipped_image
                    self.rect = self.image.get_rect(topleft=self.rect.topleft)
                
                if self.isTransforming:
                    self.transform_frame_index += self.transform_frame_speed

                    if int(self.transform_frame_index) > len(self.animations['transform']) - 1:

                        self.transform_frame_index = 0

                    image = self.animations['transform'][int(self.transform_frame_index)]
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
        
        
    def update(self, player):        
    
        self.animate()