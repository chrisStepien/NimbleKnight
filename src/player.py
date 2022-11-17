import pygame
from import_assets import import_player_animations


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):

        # Initialize Player
        super().__init__()
        self.import_player_assets()
        self.frame_index = 0
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        
        #print(self.rect)
        #print(self.rect.height)
        #print(self.rect.width)
        
        self.hit_box = self.image.get_rect(bottomleft=pos)
        #self.hit_box = self.rect.inflate(-20,-10)
        # self.hit_box.midbottom = self.rect.midbottom

        # Player statistics
        self.direction = pygame.math.Vector2(0, 0)
        self.player_status = {'attack_1': False, 'attack_combo': False, 'attack_crouch': False, 'crouch': False, 'crouch_walk': False,
            'death': False, 'fall': False, 'hurt': False, 'idle': True, 'jump': False, 'roll': False, 'run': False, 'wall_slide': False}
        self.health = 100
        self.stamina = 100
        self.gravity = 0.5
        self.jump_height = -8

        # self.player_status['attack_1'] = False self.player_status['attack_combo'] = False self.player_status['attack_crouch'] = False self.player_status['crouch'] = False self.player_status['crouch_walk'] = False self.player_status['death'] = False self.player_status['fall'] = False self.player_status['hurt'] = False self.player_status['idle'] = False self.player_status['jump'] = False self.player_status['roll'] = False self.player_status['run'] = False self.player_status['slide'] = False self.player_status['wall_slide'] = False

        # Frame speeds
        self.attack_1_frame_speed = 0.4
        self.attack_combo_frame_speed = 0.5
        self.attack_crouch_frame_speed = 0.4
        self.crouch_frame_speed = 0.1
        self.crouch_walk_frame_speed = 0.2
        self.death_frame_speed = 0.3
        self.fall_frame_speed = 0.6
        self.hurt_frame_speed = 0.1
        self.idle_frame_speed = 0.09
        self.jump_frame_speed = 0.6
        self.roll_frame_speed = 0.5
        self.run_frame_speed = 0.6
        self.slide_frame_speed = 0.3
        self.wall_slide_frame_speed = 0.4

        # Checks
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.wall_right = False
        self.wall_left = False

    # import
    def import_player_assets(self):
        self.animations = {'attack_1': [], 'attack_combo': [], 'attack_crouch': [], 'crouch': [], 'crouch_walk': [
            ], 'death': [], 'fall': [], 'hurt': [], 'idle': [], 'jump': [], 'roll': [], 'run': [], 'wall_slide': []}

        for animation in self.animations.keys():

            self.default_path = './assets/player/'
            self.default_path += animation
            self.animations[animation] = import_player_animations(
                self.default_path)

    # animate
    def animate(self):
        if(self.facing_right == True):
            # Facing Right
            if self.player_status['attack_1'] == True and self.player_status['idle'] == False and self.player_status['roll'] == False and self.player_status['run'] == False:

                self.frame_index += self.attack_1_frame_speed

                if int(self.frame_index) > len(self.animations['attack_1']) - 1:

                    self.frame_index = 0

                self.image = self.animations['attack_1'][int(self.frame_index)]

            if self.player_status['attack_combo'] == True and self.player_status['idle'] == False and self.player_status['roll'] == False and self.player_status['run'] == False:

                self.frame_index += self.attack_combo_frame_speed

                if int(self.frame_index) > len(self.animations['attack_combo']) - 1:

                    self.frame_index = 0

                self.image = self.animations['attack_combo'][int(
                    self.frame_index)]

            if self.player_status['attack_crouch'] == True and self.player_status['idle'] == False and self.player_status['roll'] == False and self.player_status['run'] == False and self.on_ground:

                self.frame_index += self.attack_crouch_frame_speed

                if int(self.frame_index) > len(self.animations['attack_crouch']) - 1:

                    self.frame_index = 0

                self.image = self.animations['attack_crouch'][int(
                    self.frame_index)]

            if self.player_status['crouch'] == True and self.player_status['idle'] == False and self.player_status['roll'] == False and self.on_ground:

                self.frame_index += self.crouch_frame_speed

                if int(self.frame_index) > len(self.animations['crouch']) - 1:

                    self.frame_index = 0

                self.image = self.animations['crouch'][int(self.frame_index)]

            if self.player_status['crouch_walk'] == True and self.player_status['idle'] == False and self.player_status['roll'] == False and self.on_ground:

                self.frame_index += self.crouch_walk_frame_speed

                if int(self.frame_index) > len(self.animations['crouch_walk']) - 1:

                    self.frame_index = 0

                self.image = self.animations['crouch_walk'][int(
                    self.frame_index)]

            if self.player_status['death'] == True:

                self.frame_index += self.death_frame_speed

                if int(self.frame_index) > len(self.animations['death']) - 1:

                    self.frame_index = 0

                self.image = self.animations['death'][int(self.frame_index)]

            if self.player_status['fall'] == True and self.player_status['roll'] == False:

                self.frame_index += self.fall_frame_speed

                if int(self.frame_index) > len(self.animations['fall']) - 1:

                    self.frame_index = 0

                self.image = self.animations['fall'][int(self.frame_index)]

            if self.player_status['hurt'] == True and self.player_status['idle'] == False and self.player_status['roll'] == False:

                self.frame_index += self.hurt_frame_speed

                if int(self.frame_index) > len(self.animations['hurt']) - 1:

                    self.frame_index = 0

                self.image = self.animations['hurt'][int(self.frame_index)]

            if self.player_status['idle'] == True and self.player_status['roll'] == False and self.on_ground:

                self.frame_index += self.idle_frame_speed

                if int(self.frame_index) > len(self.animations['idle']) - 1:

                    self.frame_index = 0

                self.image = self.animations['idle'][int(self.frame_index)]

            if self.player_status['jump'] == True and self.player_status['roll'] == False:

                self.frame_index += self.jump_frame_speed

                if int(self.frame_index) > len(self.animations['jump']) - 1:

                    self.frame_index = 0

                self.image = self.animations['jump'][int(self.frame_index)]

            if self.player_status['roll'] == True and self.player_status['idle'] == False and self.on_ground:

                self.frame_index += self.roll_frame_speed

                if int(self.frame_index) > len(self.animations['roll']) - 1:

                    self.frame_index = 0
                    self.player_status['roll'] = False
                    self.direction.x = 0

                self.image = self.animations['roll'][int(self.frame_index)]

            if self.player_status['run'] == True and self.player_status['idle'] == False and self.player_status['roll'] == False and self.on_ground:

                self.frame_index += self.run_frame_speed

                if int(self.frame_index) > len(self.animations['run']) - 1:

                    self.frame_index = 0

                self.image = self.animations['run'][int(self.frame_index)]

            if self.player_status['wall_slide'] == True and self.player_status['idle'] == False and self.player_status['roll'] == False and not self.on_ground:

                self.frame_index += self.wall_slide_frame_speed

                if int(self.frame_index) > len(self.animations['wall_slide']) - 1:

                    self.frame_index = 0

                image = self.animations['wall_slide'][int(self.frame_index)]
                flipped_image = pygame.transform.flip(image, True, False)
                self.image = flipped_image

        else:
            # Facing Left
            if self.player_status['attack_1'] == True and self.player_status['idle'] == False and self.player_status['roll'] == False and self.player_status['run'] == False:

                self.frame_index += self.attack_1_frame_speed

                if int(self.frame_index) > len(self.animations['attack_1']) - 1:

                    self.frame_index = 0

                image = self.animations['attack_1'][int(self.frame_index)]
                flipped_image = pygame.transform.flip(image, True, False)
                self.image = flipped_image

            if self.player_status['attack_combo'] == True and self.player_status['idle'] == False and self.player_status['roll'] == False and self.player_status['run'] == False:

                self.frame_index += self.attack_combo_frame_speed

                if int(self.frame_index) > len(self.animations['attack_combo']) - 1:

                    self.frame_index = 0

                image = self.animations['attack_combo'][int(self.frame_index)]
                flipped_image = pygame.transform.flip(image, True, False)
                self.image = flipped_image

            if self.player_status['attack_crouch'] == True and self.player_status['idle'] == False and self.player_status['roll'] == False and self.player_status['run'] == False and self.on_ground:

                self.frame_index += self.attack_crouch_frame_speed

                if int(self.frame_index) > len(self.animations['attack_crouch']) - 1:

                    self.frame_index = 0

                image = self.animations['attack_crouch'][int(self.frame_index)]
                flipped_image = pygame.transform.flip(image, True, False)
                self.image = flipped_image

            if self.player_status['crouch'] == True and self.player_status['idle'] == False and self.player_status['roll'] == False and self.on_ground:

                self.frame_index += self.crouch_frame_speed

                if int(self.frame_index) > len(self.animations['crouch']) - 1:

                    self.frame_index = 0

                image = self.animations['crouch'][int(self.frame_index)]
                flipped_image = pygame.transform.flip(image, True, False)
                self.image = flipped_image

            if self.player_status['crouch_walk'] == True and self.player_status['idle'] == False and self.player_status['roll'] == False and self.on_ground:

                self.frame_index += self.crouch_walk_frame_speed

                if int(self.frame_index) > len(self.animations['crouch_walk']) - 1:

                    self.frame_index = 0

                image = self.animations['crouch_walk'][int(self.frame_index)]
                flipped_image = pygame.transform.flip(image, True, False)
                self.image = flipped_image

            if self.player_status['death'] == True:

                self.frame_index += self.death_frame_speed

                if int(self.frame_index) > len(self.animations['death']) - 1:

                    self.frame_index = 0

                image = self.animations['death'][int(self.frame_index)]
                flipped_image = pygame.transform.flip(image, True, False)
                self.image = flipped_image

            if self.player_status['fall'] == True and self.player_status['roll'] == False:

                self.frame_index += self.fall_frame_speed

                if int(self.frame_index) > len(self.animations['fall']) - 1:

                    self.frame_index = 0

                image = self.animations['fall'][int(self.frame_index)]
                flipped_image = pygame.transform.flip(image, True, False)
                self.image = flipped_image

            if self.player_status['hurt'] == True and self.player_status['idle'] == False and self.player_status['roll'] == False:

                self.frame_index += self.hurt_frame_speed

                if int(self.frame_index) > len(self.animations['hurt']) - 1:

                    self.frame_index = 0

                image = self.animations['hurt'][int(self.frame_index)]
                flipped_image = pygame.transform.flip(image, True, False)
                self.image = flipped_image

            if self.player_status['idle'] == True and self.player_status['roll'] == False and self.on_ground:

                self.frame_index += self.idle_frame_speed

                if int(self.frame_index) > len(self.animations['idle']) - 1:

                    self.frame_index = 0

                image = self.animations['idle'][int(self.frame_index)]
                flipped_image = pygame.transform.flip(image, True, False)
                self.image = flipped_image

            if self.player_status['jump'] == True and self.player_status['idle'] == False and self.player_status['roll'] == False:

                self.frame_index += self.jump_frame_speed

                if int(self.frame_index) > len(self.animations['jump']) - 1:

                    self.frame_index = 0

                image = self.animations['jump'][int(self.frame_index)]
                flipped_image = pygame.transform.flip(image, True, False)
                self.image = flipped_image

            if self.player_status['roll'] == True and self.player_status['idle'] == False and self.on_ground:

                self.frame_index += self.roll_frame_speed

                if int(self.frame_index) > len(self.animations['roll']) - 1:

                    self.frame_index = 0
                    self.player_status['roll'] = False

                image = self.animations['roll'][int(self.frame_index)]
                flipped_image = pygame.transform.flip(image, True, False)
                self.image = flipped_image

            if self.player_status['run'] == True and self.player_status['idle'] == False and self.player_status['roll'] == False and self.on_ground:

                self.frame_index += self.run_frame_speed

                if int(self.frame_index) > len(self.animations['run']) - 1:

                    self.frame_index = 0

                image = self.animations['run'][int(self.frame_index)]
                flipped_image = pygame.transform.flip(image, True, False)
                self.image = flipped_image

            if self.player_status['wall_slide'] == True and self.player_status['idle'] == False and self.player_status['roll'] == False:

                self.frame_index += self.wall_slide_frame_speed

                if int(self.frame_index) > len(self.animations['wall_slide']) - 1:

                    self.frame_index = 0

                self.image = self.animations['wall_slide'][int(
                    self.frame_index)]

        if (self.on_ground and self.wall_right):
            self.rect = self.image.get_rect(bottomright=self.rect.bottomright)
           # self.hit_box = self.image.get_rect(bottomright = self.hit_box.bottomright)
        elif (self.on_ground and self.wall_left):
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
           # self.hit_box = self.image.get_rect(bottomleft = self.hit_box.bottomleft)
        elif (self.on_ground):
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
           # self.hit_box = self.image.get_rect(midbottom = self.hit_box.midbottom)
        elif (self.on_ceiling and self.wall_right):
            self.rect = self.image.get_rect(topright=self.rect.topright)
           # self.hit_box = self.image.get_rect(topright = self.hit_box.topright)
        elif (self.on_ceiling and self.wall_left):
            self.rect = self.image.get_rect(topleft=self.rect.topleft)
            # self.hit_box = self.image.get_rect(topleft = self.hit_box.topleft)
        elif (self.on_ceiling):
            self.rect = self.image.get_rect(midtop=self.rect.midtop)
            # self.hit_box = self.image.get_rect(midtop = self.hit_box.midtop)

        #Change rect size to match what it should be or change the size of the PNGs
        
    def input(self, single_press):

        keys = pygame.key.get_pressed()
        # Ordered by priority
        if keys[pygame.K_e] and single_press == True and self.on_ground:

            self.player_status['roll'] = True
            self.player_status['attack_1'] = False
            self.player_status['attack_combo'] = False
            self.player_status['attack_crouch'] = False
            self.player_status['crouch'] = False
            self.player_status['crouch_walk'] = False
            self.player_status['death'] = False
            self.player_status['fall'] = False
            self.player_status['hurt'] = False
            self.player_status['idle'] = False
            self.player_status['jump'] = False
            self.player_status['run'] = False
            self.player_status['wall_slide'] = False
            self.roll()

        elif keys[pygame.K_SPACE] and self.player_status['roll'] == False and single_press == True and self.on_ground:

            self.player_status['attack_combo'] = True
            self.player_status['attack_1'] = False
            self.player_status['attack_crouch'] = False
            self.player_status['crouch'] = False
            self.player_status['crouch_walk'] = False
            self.player_status['death'] = False
            self.player_status['fall'] = False
            self.player_status['hurt'] = False
            self.player_status['idle'] = False
            self.player_status['jump'] = False
            self.player_status['roll'] = False
            self.player_status['run'] = False
            self.player_status['wall_slide'] = False

        elif keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d] and self.player_status['roll'] == False:
            # 1
            if keys[pygame.K_s] and keys[pygame.K_d] or keys[pygame.K_s] and keys[pygame.K_a]:

                if keys[pygame.K_s] and keys[pygame.K_d]:

                    self.player_status['crouch_walk'] = True
                    self.player_status['attack_1'] = False
                    self.player_status['attack_combo'] = False
                    self.player_status['attack_crouch'] = False
                    self.player_status['crouch'] = False
                    self.player_status['death'] = False
                    self.player_status['fall'] = False
                    self.player_status['hurt'] = False
                    self.player_status['idle'] = False
                    self.player_status['jump'] = False
                    self.player_status['roll'] = False
                    self.player_status['run'] = False
                    self.player_status['wall_slide'] = False

                    self.direction.x = 0.5
                    self.facing_right = True

                else:

                    self.player_status['crouch_walk'] = True
                    self.player_status['attack_1'] = False
                    self.player_status['attack_combo'] = False
                    self.player_status['attack_crouch'] = False
                    self.player_status['crouch'] = False
                    self.player_status['death'] = False
                    self.player_status['fall'] = False
                    self.player_status['hurt'] = False
                    self.player_status['idle'] = False
                    self.player_status['jump'] = False
                    self.player_status['roll'] = False
                    self.player_status['run'] = False
                    self.player_status['wall_slide'] = False

                    self.direction.x = -0.5
                    self.facing_right = False
            else:
                if (keys[pygame.K_w] and self.on_ground == True):
                  
                    self.player_status['jump'] = True
                    self.player_status['attack_1'] = False
                    self.player_status['attack_combo'] = False
                    self.player_status['attack_crouch'] = False
                    self.player_status['crouch'] = False
                    self.player_status['crouch_walk'] = False
                    self.player_status['death'] = False
                    self.player_status['fall'] = False
                    self.player_status['hurt'] = False
                    self.player_status['idle'] = False
                    self.player_status['roll'] = False
                    self.player_status['run'] = False
                    self.player_status['wall_slide'] = False
                    self.gravity = 0.5
                    self.jump()

                elif keys[pygame.K_a]:

                    if(self.on_ground == False and self.player_status['fall'] == True and self.wall_left == True and self.facing_right == False):

                        self.player_status['wall_slide'] = True
                        self.player_status['attack_1'] = False
                        self.player_status['attack_combo'] = False
                        self.player_status['attack_crouch'] = False
                        self.player_status['crouch'] = False
                        self.player_status['crouch_walk'] = False
                        self.player_status['death'] = False
                        self.player_status['fall'] = False
                        self.player_status['hurt'] = False
                        self.player_status['idle'] = False
                        self.player_status['roll'] = False
                        self.player_status['run'] = False

                        self.gravity = 0.05
                        self.facing_right = False

                    elif self.on_ground == False and self.player_status['fall'] == True and self.player_status['jump'] == False and self.wall_left == False:

                        self.player_status['fall'] = True
                        self.player_status['attack_1'] = False
                        self.player_status['attack_combo'] = False
                        self.player_status['attack_crouch'] = False
                        self.player_status['crouch'] = False
                        self.player_status['crouch_walk'] = False
                        self.player_status['death'] = False
                        self.player_status['hurt'] = False
                        self.player_status['idle'] = False
                        self.player_status['roll'] = False
                        self.player_status['run'] = False
                        self.player_status['wall_slide'] = False

                        self.direction.x = -1
                        self.gravity = 0.5
                        self.facing_right = False

                    else:
                        self.player_status['run'] = True
                        self.player_status['attack_1'] = False
                        self.player_status['attack_combo'] = False
                        self.player_status['attack_crouch'] = False
                        self.player_status['crouch'] = False
                        self.player_status['crouch_walk'] = False
                        self.player_status['death'] = False
                        self.player_status['fall'] = False
                        self.player_status['hurt'] = False
                        self.player_status['idle'] = False
                        self.player_status['roll'] = False
                        self.player_status['wall_slide'] = False

                        if(self.wall_left):
                            self.direction.x = 0
                        else:
                            self.direction.x = -1

                        self.facing_right = False

                elif keys[pygame.K_d]:
                        # CHANGE FOR ALL
                    if(self.on_ground == False and self.player_status['fall'] == True and self.wall_right == True and self.facing_right == True):

                        self.player_status['wall_slide'] = True
                        self.player_status['attack_1'] = False
                        self.player_status['attack_combo'] = False
                        self.player_status['attack_crouch'] = False
                        self.player_status['crouch'] = False
                        self.player_status['crouch_walk'] = False
                        self.player_status['death'] = False
                        self.player_status['fall'] = False
                        self.player_status['hurt'] = False
                        self.player_status['idle'] = False
                        self.player_status['roll'] = False
                        self.player_status['run'] = False

                        self.gravity = 0.05
                        self.facing_right = True

                    elif self.on_ground == False and self.player_status['wall_slide'] == False and self.player_status['jump'] == False and self.wall_right == False:

                        self.player_status['fall'] = True
                        self.player_status['attack_1'] = False
                        self.player_status['attack_combo'] = False
                        self.player_status['attack_crouch'] = False
                        self.player_status['crouch'] = False
                        self.player_status['crouch_walk'] = False
                        self.player_status['death'] = False
                        self.player_status['hurt'] = False
                        self.player_status['idle'] = False
                        self.player_status['roll'] = False
                        self.player_status['run'] = False
                        self.player_status['wall_slide'] = False

                        self.direction.x = 1
                        self.gravity = 0.5
                        self.facing_right = True

                    else:

                        self.player_status['run'] = True
                        self.player_status['attack_1'] = False
                        self.player_status['attack_combo'] = False
                        self.player_status['attack_crouch'] = False
                        self.player_status['crouch'] = False
                        self.player_status['crouch_walk'] = False
                        self.player_status['death'] = False
                        self.player_status['fall'] = False
                        self.player_status['hurt'] = False
                        self.player_status['idle'] = False
                        self.player_status['roll'] = False
                        self.player_status['wall_slide'] = False
                        # CHANGE FOR ALL
                        if(self.wall_right):
                            self.direction.x = 0
                        else:
                            self.direction.x = 1

                        self.facing_right = True

                else:

                    self.player_status['idle'] = True

                    self.direction.x = 0

                if keys[pygame.K_s]:

                    self.player_status['crouch'] = True
                    self.player_status['attack_1'] = False
                    self.player_status['attack_combo'] = False
                    self.player_status['attack_crouch'] = False
                    self.player_status['crouch_walk'] = False
                    self.player_status['death'] = False
                    self.player_status['fall'] = False
                    self.player_status['hurt'] = False
                    self.player_status['idle'] = False
                    self.player_status['jump'] = False
                    self.player_status['roll'] = False
                    self.player_status['run'] = False
                    self.player_status['wall_slide'] = False

        elif(keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_DOWN] and self.player_status['roll'] == False and single_press == True):
            if keys[pygame.K_LEFT]:

                self.player_status['attack_1'] = True
                self.player_status['attack_combo'] = False
                self.player_status['attack_crouch'] = False
                self.player_status['crouch'] = False
                self.player_status['crouch_walk'] = False
                self.player_status['death'] = False
                self.player_status['fall'] = False
                self.player_status['hurt'] = False
                self.player_status['idle'] = False
                self.player_status['jump'] = False
                self.player_status['roll'] = False
                self.player_status['run'] = False
                self.player_status['wall_slide'] = False

                self.facing_right = False

            if keys[pygame.K_RIGHT]:

                self.player_status['attack_1'] = True
                self.player_status['attack_combo'] = False
                self.player_status['attack_crouch'] = False
                self.player_status['crouch'] = False
                self.player_status['crouch_walk'] = False
                self.player_status['death'] = False
                self.player_status['fall'] = False
                self.player_status['hurt'] = False
                self.player_status['idle'] = False
                self.player_status['jump'] = False
                self.player_status['roll'] = False
                self.player_status['run'] = False
                self.player_status['wall_slide'] = False

                self.facing_right = True

            if keys[pygame.K_DOWN] and self.on_ground:

                self.player_status['attack_crouch'] = True
                self.player_status['attack_1'] = False
                self.player_status['attack_combo'] = False
                self.player_status['crouch'] = False
                self.player_status['crouch_walk'] = False
                self.player_status['death'] = False
                self.player_status['fall'] = False
                self.player_status['hurt'] = False
                self.player_status['idle'] = False
                self.player_status['jump'] = False
                self.player_status['roll'] = False
                self.player_status['run'] = False
                self.player_status['wall_slide'] = False

                self.direction.x = 0
        elif(self.on_ground) and self.player_status['roll'] == False and single_press == False:

            self.player_status['idle'] = True
            self.player_status['attack_1'] = False
            self.player_status['attack_combo'] = False
            self.player_status['attack_crouch'] = False
            self.player_status['crouch'] = False
            self.player_status['fall'] = False
            self.player_status['jump'] = False
            self.player_status['run'] = False

            self.direction.x = 0

        if self.wall_right == False and self.wall_left == False and self.player_status['idle'] == False and self.player_status['jump'] == False and self.on_ground == False:

            self.player_status['fall'] = True
            self.player_status['run'] = False
            self.player_status['wall_slide'] = False
            self.gravity = 0.5

        if(self.on_ground == True):

            self.player_status['jump'] = False
            self.player_status['fall'] = False
        
        if sum(keys) == 0 and self.player_status['fall'] == False and self.player_status['jump'] == False and self.player_status['roll'] == False:

            self.player_status['idle'] = True
            self.player_status['attack_1'] = False
            self.player_status['attack_combo'] = False
            self.player_status['attack_crouch'] = False
            self.player_status['crouch'] = False
            self.player_status['crouch_walk'] = False
            self.player_status['death'] = False
            self.player_status['fall'] = False
            self.player_status['hurt'] = False
            self.player_status['jump'] = False
            self.player_status['roll'] = False
            self.player_status['run'] = False
            self.player_status['wall_slide'] = False

            self.direction.x = 0

       
        
        print(self.player_status['attack_1'], self.player_status['attack_combo'], self.player_status['attack_crouch'], self.player_status['crouch'], self.player_status['crouch_walk'], self.player_status['death'],
              self.player_status['fall'], self.player_status['hurt'], self.player_status['idle'], self.player_status['jump'], self.player_status['roll'], self.player_status['run'], self.player_status["wall_slide"])
        

    def apply_gravity(self):

        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        self.hit_box.y += self.direction.y


    def status(self):

            # Jumping
            if(self.direction.y < 0 and self.player_status['roll'] == False):

                for status in self.player_status:
                    self.player_status['jump'] = True
                
                    if self.player_status != self.player_status['jump'] and self.player_status != self.player_status['roll']:
                        self.player_status[status] = False
                        # Falling
            elif(self.direction.y > 1 and self.player_status['roll'] == False):

                for status in self.player_status:
                    self.player_status['fall'] = True

                    if self.player_status != self.player_status['fall'] and self.player_status != self.player_status['roll']:
                        self.player_status[status] = False
            elif(self.player_status['roll'] == False):
                # Running
                if(self.direction.x != 0):
                    for status in self.player_status:
                        self.player_status['run'] = True 
                        
                        if self.player_status != self.player_status['run'] and self.player_status != self.player_status['roll']:
                            self.player_status[status] = False
                            # Idling
    
            else:
                                
                for status in self.player_status:
                    self.player_status['idle'] = True
                                    
                    if self.player_status[status] != self.player_status['idle'] and self.player_status != self.player_status['roll']:
                        self.player_status[status] = False 
        #Maybe take out                  
    def roll(self):
        
        print(self.direction)
        if(self.facing_right):
            self.direction.x += 1           
                
        elif(not self.facing_right):
            self.direction.x -= 1           
                
    
    def player_hitbox(self):
        
        pass
        
        
    def jump(self):
  
        self.direction.y = self.jump_height     
        
    def update(self, single_press):
            
        print(self.rect.height)
        print(self.rect.width)
        self.status()
        self.input(single_press)
        self.apply_gravity()
        self.animate()  
        
        
        print("playerx:" + str(self.rect.x))
        print("player:" + str(self.rect.bottomright))
        
        
        #print(single_press)
        #print(self.on_ground)
       # print(self.wall_right)
    