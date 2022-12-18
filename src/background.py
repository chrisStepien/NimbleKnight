import pygame
#Add screen_height and screen_width in here
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, pos, resolution):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, resolution)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        