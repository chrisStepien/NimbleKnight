import pygame
from import_assets import import_player_animations

# hitbox rect for enemy interactions
# collision rect smaller than image for better visual


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):

        # Initialize Player
        super().__init__()

        # Import Assets
        self.import_player_assets()

        # Frame Indexes
        self.mov_frame_index = 0
        self.att_frame_index = 0
        self.death_frame_index = 0
        self.image = self.animations['idle'][self.mov_frame_index]

        # Player Rects
        self.rect = self.image.get_rect(topleft=pos)
        self.env_rect = self.rect.inflate(-4, -2)
        self.hit_box = self.rect.inflate(-8, -1)

        # Sound
        self.lose_sound = pygame.mixer.Sound("./media/game_over.wav")
        self.slash = pygame.mixer.Sound("./media/player_slash.wav")

        # Player Stats
        self.player_status = {'attack_1': False, 'attack_crouch': False, 'crouch': False, 'crouch_walk': False,
                              'death': False, 'fall': False, 'hurt': False, 'idle': True, 'jump': False, 'run': False, 'wall_slide': False}
        self.health = 1000
        self.damage = 25
        self.isAttacking = False

        # Frame speeds
        self.attack_1_frame_speed = 0.8
        self.attack_crouch_frame_speed = 0.4
        self.crouch_frame_speed = 0.1
        self.crouch_walk_frame_speed = 0.2
        self.death_frame_speed = 0.3
        self.fall_frame_speed = 0.6
        self.hurt_frame_speed = 0.1
        self.idle_frame_speed = 0.09
        self.jump_frame_speed = 0.6
        self.run_frame_speed = 0.6
        self.wall_slide_frame_speed = 0.4

        # Directional Checks
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.wall_right = False
        self.wall_left = False
        self.direction = pygame.math.Vector2(0, 0)

        # Velocities
        self.speed = 8
        self.jump_height = -9
        self.gravity = 0.5

        self.stop = False

    # Import
    def import_player_assets(self):
        self.animations = {'attack_1': [], 'attack_crouch': [], 'crouch': [], 'crouch_walk': [
        ], 'death': [], 'fall': [], 'hurt': [], 'idle': [], 'jump': [], 'run': [], 'wall_slide': []}

        for animation in self.animations.keys():

            self.default_path = './assets/player/'
            self.default_path += animation
            self.animations[animation] = import_player_animations(
                self.default_path)

    # Animate
    def animate(self):
        if self.player_status['death'] == True:

            if int(self.death_frame_index) < len(self.animations['death']) - 1:
                self.death_frame_index += self.death_frame_speed

            self.image = self.animations['death'][int(self.death_frame_index)]
            self.direction.x = 0
            self.speed = 0

            if int(self.death_frame_index) == 1:
                self.lose_sound.play()
                pygame.mixer.music.stop()
                pygame.mixer.music.load("./media/menu_music.mp3")

        else:
            if(self.facing_right == True):
                # Facing Right
                if self.player_status['attack_1'] == True and self.player_status['jump'] == False and self.player_status['fall'] == False and self.player_status['idle'] == False and self.player_status['run'] == False:

                    self.att_frame_index += self.attack_1_frame_speed

                    if int(self.att_frame_index) > len(self.animations['attack_1']) - 1:

                        self.att_frame_index = 0
                        self.player_status['attack_1'] = False
                        self.isAttacking = False

                    self.image = self.animations['attack_1'][int(
                        self.att_frame_index)]

                    if int(self.att_frame_index) == 1:
                        self.slash.play()

                if self.player_status['attack_crouch'] == True and self.player_status['idle'] == False and self.player_status['run'] == False and self.on_ground:

                    self.att_frame_index += self.attack_crouch_frame_speed

                    if int(self.att_frame_index) > len(self.animations['attack_crouch']) - 1:

                        self.att_frame_index = 0
                        self.player_status['attack_crouch'] = False
                        self.isAttacking = False

                    self.image = self.animations['attack_crouch'][int(
                        self.att_frame_index)]

                    if int(self.att_frame_index) == 1:
                        self.slash.play()

                if self.player_status['crouch'] == True and self.player_status['idle'] == False and self.on_ground:

                    self.mov_frame_index += self.crouch_frame_speed

                    if int(self.mov_frame_index) > len(self.animations['crouch']) - 1:

                        self.mov_frame_index = 0

                    self.image = self.animations['crouch'][int(
                        self.mov_frame_index)]

                if self.player_status['crouch_walk'] == True and self.player_status['idle'] == False and self.on_ground:

                    self.mov_frame_index += self.crouch_walk_frame_speed

                    if int(self.mov_frame_index) > len(self.animations['crouch_walk']) - 1:

                        self.mov_frame_index = 0

                    self.image = self.animations['crouch_walk'][int(
                        self.mov_frame_index)]

                if self.player_status['fall'] == True and self.player_status['jump'] == False:

                    self.mov_frame_index += self.fall_frame_speed

                    if int(self.mov_frame_index) > len(self.animations['fall']) - 1:

                        self.mov_frame_index = 0

                    self.image = self.animations['fall'][int(
                        self.mov_frame_index)]

                if self.player_status['hurt'] == True and self.player_status['idle'] == False:

                    self.mov_frame_index += self.hurt_frame_speed

                    if int(self.mov_frame_index) > len(self.animations['hurt']) - 1:

                        self.mov_frame_index = 0

                    self.image = self.animations['hurt'][int(
                        self.mov_frame_index)]

                if self.player_status['idle'] == True and self.on_ground:

                    self.mov_frame_index += self.idle_frame_speed

                    if int(self.mov_frame_index) > len(self.animations['idle']) - 1:

                        self.mov_frame_index = 0

                    self.image = self.animations['idle'][int(
                        self.mov_frame_index)]

                if self.player_status['jump'] == True:

                    self.mov_frame_index += self.jump_frame_speed

                    if int(self.mov_frame_index) > len(self.animations['jump']) - 1:

                        self.mov_frame_index = 0

                    self.image = self.animations['jump'][int(
                        self.mov_frame_index)]

                if self.player_status['run'] == True and self.player_status['idle'] == False and self.on_ground:

                    self.mov_frame_index += self.run_frame_speed

                    if int(self.mov_frame_index) > len(self.animations['run']) - 1:

                        self.mov_frame_index = 0

                    self.image = self.animations['run'][int(
                        self.mov_frame_index)]

                if self.player_status['wall_slide'] == True and self.player_status['fall'] == True and self.player_status['idle'] == False and not self.on_ground:

                    self.mov_frame_index += self.wall_slide_frame_speed

                    if int(self.mov_frame_index) > len(self.animations['wall_slide']) - 1:

                        self.mov_frame_index = 0

                    image = self.animations['wall_slide'][int(
                        self.mov_frame_index)]
                    flipped_image = pygame.transform.flip(image, True, False)
                    self.image = flipped_image
                    self.rect = self.image.get_rect(topleft=self.rect.topleft)
                    self.env_rect = self.rect.inflate(-4, -2)
                    self.hit_box = self.rect.inflate(-8, -1)

            # Facing Left
            else:

                if self.player_status['attack_1'] == True and self.player_status['jump'] == False and self.player_status['fall'] == False and self.player_status['idle'] == False and self.player_status['run'] == False:

                    self.att_frame_index += self.attack_1_frame_speed

                    if int(self.att_frame_index) > len(self.animations['attack_1']) - 1:

                        self.att_frame_index = 0
                        self.player_status['attack_1'] = False
                        self.isAttacking = False

                    image = self.animations['attack_1'][int(
                        self.att_frame_index)]
                    flipped_image = pygame.transform.flip(image, True, False)
                    self.image = flipped_image

                    if int(self.att_frame_index) == 1:
                        self.slash.play()

                if self.player_status['attack_crouch'] == True and self.player_status['idle'] == False and self.player_status['run'] == False and self.on_ground:

                    self.att_frame_index += self.attack_crouch_frame_speed

                    if int(self.att_frame_index) > len(self.animations['attack_crouch']) - 1:

                        self.att_frame_index = 0
                        self.player_status['attack_crouch'] = False
                        self.isAttacking = False

                    image = self.animations['attack_crouch'][int(
                        self.att_frame_index)]
                    flipped_image = pygame.transform.flip(image, True, False)
                    self.image = flipped_image

                    if int(self.att_frame_index) == 1:
                        self.slash.play()

                if self.player_status['crouch'] == True and self.player_status['idle'] == False and self.on_ground:

                    self.mov_frame_index += self.crouch_frame_speed

                    if int(self.mov_frame_index) > len(self.animations['crouch']) - 1:

                        self.mov_frame_index = 0

                    image = self.animations['crouch'][int(
                        self.mov_frame_index)]
                    flipped_image = pygame.transform.flip(image, True, False)
                    self.image = flipped_image

                if self.player_status['crouch_walk'] == True and self.player_status['idle'] == False and self.on_ground:

                    self.mov_frame_index += self.crouch_walk_frame_speed

                    if int(self.mov_frame_index) > len(self.animations['crouch_walk']) - 1:

                        self.mov_frame_index = 0

                    image = self.animations['crouch_walk'][int(
                        self.mov_frame_index)]
                    flipped_image = pygame.transform.flip(image, True, False)
                    self.image = flipped_image

                if self.player_status['fall'] == True and self.player_status['wall_slide'] == False:

                    self.mov_frame_index += self.fall_frame_speed

                    if int(self.mov_frame_index) > len(self.animations['fall']) - 1:

                        self.mov_frame_index = 0

                    image = self.animations['fall'][int(self.mov_frame_index)]
                    flipped_image = pygame.transform.flip(image, True, False)
                    self.image = flipped_image

                if self.player_status['hurt'] == True and self.player_status['idle'] == False:

                    self.mov_frame_index += self.hurt_frame_speed

                    if int(self.mov_frame_index) > len(self.animations['hurt']) - 1:

                        self.mov_frame_index = 0

                    image = self.animations['hurt'][int(self.mov_frame_index)]
                    flipped_image = pygame.transform.flip(image, True, False)
                    self.image = flipped_image

                if self.player_status['idle'] == True and self.on_ground:

                    self.mov_frame_index += self.idle_frame_speed

                    if int(self.mov_frame_index) > len(self.animations['idle']) - 1:

                        self.mov_frame_index = 0

                    image = self.animations['idle'][int(self.mov_frame_index)]
                    flipped_image = pygame.transform.flip(image, True, False)
                    self.image = flipped_image

                if self.player_status['jump'] == True and self.player_status['fall'] == False and self.player_status['idle'] == False:

                    self.mov_frame_index += self.jump_frame_speed

                    if int(self.mov_frame_index) > len(self.animations['jump']) - 1:

                        self.mov_frame_index = 0

                    image = self.animations['jump'][int(self.mov_frame_index)]
                    flipped_image = pygame.transform.flip(image, True, False)
                    self.image = flipped_image

                if self.player_status['run'] == True and self.player_status['idle'] == False and self.on_ground:

                    self.mov_frame_index += self.run_frame_speed

                    if int(self.mov_frame_index) > len(self.animations['run']) - 1:

                        self.mov_frame_index = 0

                    image = self.animations['run'][int(self.mov_frame_index)]
                    flipped_image = pygame.transform.flip(image, True, False)
                    self.image = flipped_image

                if self.player_status['wall_slide'] == True and self.player_status['idle'] == False:

                    self.mov_frame_index += self.wall_slide_frame_speed

                    if int(self.mov_frame_index) > len(self.animations['wall_slide']) - 1:

                        self.mov_frame_index = 0

                    self.image = self.animations['wall_slide'][int(
                        self.mov_frame_index)]

        if (self.on_ground and self.wall_right):
            
            self.rect = self.image.get_rect(bottomright=self.rect.bottomright)
            self.env_rect = self.rect.inflate(-4, -2)
            self.hit_box = self.rect.inflate(-8, -1)

        elif (self.on_ground and self.wall_left):
            
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
            self.env_rect = self.rect.inflate(-4, -2)
            self.hit_box = self.rect.inflate(-8, -1)

        elif (self.on_ground):
            
            self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
            self.env_rect = self.rect.inflate(-4, -2)
            self.hit_box = self.rect.inflate(-8, -1)

        elif (self.on_ceiling and self.wall_right):
            
            self.rect = self.image.get_rect(topright=self.rect.topright)
            self.env_rect = self.rect.inflate(-4, -2)
            self.hit_box = self.rect.inflate(-8, -1)

        elif (self.on_ceiling and self.wall_left):
            
            self.rect = self.image.get_rect(topleft=self.rect.topleft)
            self.env_rect = self.rect.inflate(-4, -2)
            self.hit_box = self.rect.inflate(-8, -1)

        elif (self.on_ceiling):
            self.rect = self.image.get_rect(midtop=self.rect.midtop)
            self.env_rect = self.rect.inflate(-4, -2)
            self.hit_box = self.rect.inflate(-8, -1)

    def input(self, attacking):

        # Ordered by priority
        if self.stop == False:
            keys = pygame.key.get_pressed()
            # BUG: Player still runs when not pushing these keys but still pressing another key
            if (keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d]):
                # 1
                if (keys[pygame.K_LEFT] == False and keys[pygame.K_DOWN] == False and keys[pygame.K_RIGHT] == False and self.player_status['attack_1'] == False and self.player_status['attack_crouch'] == False and self.player_status['hurt'] == False) and (keys[pygame.K_s] and keys[pygame.K_d]) or (keys[pygame.K_s] and keys[pygame.K_a]):

                    if keys[pygame.K_s] and keys[pygame.K_d]:

                        self.player_status['crouch_walk'] = True
                        self.player_status['crouch'] = False
                        self.player_status['fall'] = False
                        self.player_status['hurt'] = False
                        self.player_status['idle'] = False
                        self.player_status['jump'] = False
                        self.player_status['run'] = False
                        self.player_status['wall_slide'] = False

                        self.direction.x = 0.5
                        self.facing_right = True

                    else:

                        self.player_status['crouch_walk'] = True
                        self.player_status['crouch'] = False
                        self.player_status['fall'] = False
                        self.player_status['hurt'] = False
                        self.player_status['idle'] = False
                        self.player_status['jump'] = False
                        self.player_status['run'] = False
                        self.player_status['wall_slide'] = False

                        self.direction.x = -0.5
                        self.facing_right = False
                elif (keys[pygame.K_LEFT] == False and keys[pygame.K_DOWN] == False and keys[pygame.K_RIGHT] == False and self.player_status['attack_1'] == False and self.player_status['attack_crouch'] == False and self.player_status['hurt'] == False):
                    if (keys[pygame.K_w] and self.on_ground == True):

                        self.player_status['jump'] = True
                        self.player_status['crouch'] = False
                        self.player_status['crouch_walk'] = False
                        self.player_status['fall'] = False
                        self.player_status['hurt'] = False
                        self.player_status['idle'] = False
                        self.player_status['run'] = False
                        self.direction.x = 0

                        self.jump()

                    elif keys[pygame.K_a]:

                        if(self.on_ground == False and self.player_status['fall'] == True and self.wall_left == True and self.facing_right == False):

                            self.player_status['wall_slide'] = True
                            self.player_status['crouch'] = False
                            self.player_status['crouch_walk'] = False
                            self.player_status['hurt'] = False
                            self.player_status['idle'] = False
                            self.player_status['run'] = False

                            self.facing_right = False

                        elif self.on_ground == False and self.player_status['jump'] == False and self.wall_left == False:

                            self.player_status['fall'] = True
                            self.player_status['crouch'] = False
                            self.player_status['crouch_walk'] = False
                            self.player_status['hurt'] = False
                            self.player_status['idle'] = False
                            self.player_status['run'] = False
                            self.player_status['wall_slide'] = False

                            self.direction.x = -1

                            self.facing_right = False

                        elif not self.wall_left:
                            self.player_status['run'] = True
                            self.player_status['crouch'] = False
                            self.player_status['crouch_walk'] = False
                            self.player_status['fall'] = False
                            self.player_status['hurt'] = False
                            self.player_status['idle'] = False
                            self.player_status['wall_slide'] = False

                            self.direction.x = -1
                            self.facing_right = False

                    elif keys[pygame.K_d] and self.stop == False:
                     
                        if(self.on_ground == False and self.player_status['fall'] == True and self.wall_right == True and self.facing_right == True):

                            self.player_status['wall_slide'] = True
                            self.player_status['crouch'] = False
                            self.player_status['crouch_walk'] = False
                            self.player_status['hurt'] = False
                            self.player_status['idle'] = False
                            self.player_status['run'] = False

                            self.facing_right = True

                        elif self.on_ground == False and self.player_status['wall_slide'] == False and self.player_status['jump'] == False and self.wall_right == False:

                            self.player_status['fall'] = True
                            self.player_status['crouch'] = False
                            self.player_status['crouch_walk'] = False
                            self.player_status['hurt'] = False
                            self.player_status['idle'] = False
                            self.player_status['run'] = False
                            self.player_status['wall_slide'] = False

                            self.direction.x = 1
                            self.facing_right = True

                        elif not self.wall_right:
                            self.player_status['run'] = True
                            self.player_status['crouch'] = False
                            self.player_status['crouch_walk'] = False
                            self.player_status['fall'] = False
                            self.player_status['hurt'] = False
                            self.player_status['idle'] = False
                            self.player_status['wall_slide'] = False

                            self.direction.x = 1
                            self.facing_right = True

                    if keys[pygame.K_s]:

                        self.player_status['crouch'] = True
                        self.player_status['crouch_walk'] = False
                        self.player_status['fall'] = False
                        self.player_status['hurt'] = False
                        self.player_status['idle'] = False
                        self.player_status['jump'] = False
                        self.player_status['run'] = False
                        self.player_status['wall_slide'] = False
                        self.direction.x = 0

            elif(keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_DOWN]):
                if keys[pygame.K_LEFT] and self.on_ground and attacking:

                    self.player_status['attack_1'] = True
                    self.player_status['attack_crouch'] = False
                    self.player_status['crouch'] = False
                    self.player_status['crouch_walk'] = False
                    self.player_status['fall'] = False
                    self.player_status['hurt'] = False
                    self.player_status['idle'] = False
                    self.player_status['jump'] = False
                    self.player_status['run'] = False
                    self.player_status['wall_slide'] = False

                    self.isAttacking = True
                    self.facing_right = False
                    self.direction.x = 0

                if keys[pygame.K_RIGHT] and self.on_ground and attacking:
                    self.player_status['attack_1'] = True
                    self.player_status['attack_crouch'] = False
                    self.player_status['crouch'] = False
                    self.player_status['crouch_walk'] = False
                    self.player_status['fall'] = False
                    self.player_status['hurt'] = False
                    self.player_status['idle'] = False
                    self.player_status['jump'] = False
                    self.player_status['run'] = False
                    self.player_status['wall_slide'] = False

                    self.isAttacking = True
                    self.facing_right = True
                    self.direction.x = 0

                if keys[pygame.K_DOWN] and self.on_ground and attacking:

                    self.player_status['attack_crouch'] = True
                    self.player_status['attack_1'] = False
                    self.player_status['crouch'] = False
                    self.player_status['crouch_walk'] = False
                    self.player_status['fall'] = False
                    self.player_status['hurt'] = False
                    self.player_status['idle'] = False
                    self.player_status['jump'] = False
                    self.player_status['run'] = False
                    self.player_status['wall_slide'] = False

                    self.isAttacking = True
                    self.direction.x = 0

            if self.wall_right == False and self.wall_left == False and self.player_status['idle'] == False and self.player_status['jump'] == False and self.direction.y > 1 and self.on_ground == False:

                self.player_status['fall'] = True
                self.player_status['run'] = False
                self.player_status['wall_slide'] = False

            if(self.on_ground == True):

                self.player_status['jump'] = False
                self.player_status['fall'] = False

            if sum(keys) == 0 and self.player_status['fall'] == False and self.player_status['jump'] == False and self.player_status['attack_1'] == False and self.player_status['attack_crouch'] == False:

                self.player_status['idle'] = True
                self.player_status['crouch'] = False
                self.player_status['crouch_walk'] = False
                self.player_status['fall'] = False
                self.player_status['hurt'] = False
                self.player_status['jump'] = False
                self.player_status['run'] = False
                self.player_status['wall_slide'] = False

                self.direction.x = 0

        print(self.player_status['attack_1'], self.player_status['attack_crouch'], self.player_status['crouch'], self.player_status['crouch_walk'], self.player_status['death'],
              self.player_status['fall'], self.player_status['hurt'], self.player_status['idle'], self.player_status['jump'], self.player_status['run'], self.player_status["wall_slide"])

    def apply_gravity(self):

        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        self.env_rect.y += self.direction.y
        self.hit_box.y += self.direction.y

    def status(self):

        # Jumping
        if(self.direction.y < 0):

            for status in self.player_status:
                self.player_status['jump'] = True

                if self.player_status != self.player_status['jump']:
                    self.player_status[status] = False
        # Falling
        elif(self.direction.y > 1):

            for status in self.player_status:
                self.player_status['fall'] = True

                if self.player_status != self.player_status['fall']:
                    self.player_status[status] = False
        # Running
        if(self.direction.x != 0 and self.direction.y == 0):
            for status in self.player_status:
                self.player_status['run'] = True

                if self.player_status != self.player_status['run']:
                    self.player_status[status] = False
        # Idling
        elif(self.direction.x == 0 and self.direction.y == 0 and self.player_status['attack_1'] == False and self.player_status['attack_crouch'] == False):

            for status in self.player_status:
                self.player_status['idle'] = True

                if self.player_status[status] != self.player_status['idle']:
                    self.player_status[status] = False

    def jump(self):

        self.direction.y = self.jump_height

    def update(self, attacking):
        
        # Check if Player is dead
        if self.player_status['death'] == False:
            self.status()
            self.input(attacking)
            self.apply_gravity()
        self.animate()
