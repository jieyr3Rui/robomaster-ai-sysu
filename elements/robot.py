# class robot
import pygame
import numpy as np
from elements.bullet import bullet

class robot(pygame.sprite.Sprite):
    def __init__(self, image_path, player, x, y, yaw, bullet=100, hp=100):
        pygame.sprite.Sprite.__init__(self)
        self.bullet_group = pygame.sprite.Group()
        self.player = player
        self.yaw = yaw
        self.image_path = image_path
        self.origin = pygame.image.load(self.image_path).convert()
        self.image = pygame.transform.rotate(self.origin, yaw)
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.bullet = bullet
        self.hp = hp
        

    def shoot(self):
        return False, [0,0,0]

    def move(self, vx, vy, rotate):

        return True

