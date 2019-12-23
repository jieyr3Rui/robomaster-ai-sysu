# class block
import pygame
from elements.block import block
from define import *
class ground(pygame.sprite.Sprite):
    def __init__(self, image_path):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.block_group = pygame.sprite.Group()
        self.block_group.add(block(10, 120, 100, 10))

