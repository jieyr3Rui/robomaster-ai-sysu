# class bullet
import pygame
import numpy as np
from define import *
vec = pygame.math.Vector2

class bullet(pygame.sprite.Sprite):
    def __init__(self, player, x, y, yaw, v=10, color=red):
        pygame.sprite.Sprite.__init__(self)
        self.player = player
        self.yaw = yaw
        self.v = v
        self.image = pygame.Surface((10, 10))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        self.rect.center = self.pos
    
    def move(self, robot_group, block_group):
        new_x = self.pos[0] + self.v * np.math.cos(self.yaw)
        new_y = self.pos[1] + self.v * np.math.sin(self.yaw)
        self.pos = vec(new_x, new_y)
        self.rect.center = self.pos


        