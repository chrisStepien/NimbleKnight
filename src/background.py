import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (1280, 720))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        