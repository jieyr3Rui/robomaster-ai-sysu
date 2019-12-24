# class ray
import pygame
from elements.define import *

vec = pygame.math.Vector2

class ray(pygame.sprite.Sprite):
    def __init__(self, x, y, yaw):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        self.rect.center = self.pos
        self.yaw = yaw
        self.v = 10
    
    def move(self, robot_group, block_group):
        time = 500
        while time > 0:
            time -= 1
            new_x = self.pos[0] - self.v * np.math.sin(self.yaw * 3.1415926 / 180)
            new_y = self.pos[1] - self.v * np.math.cos(self.yaw * 3.1415926 / 180)
            self.pos = vec(new_x, new_y)
            self.rect.center = self.pos
            hit = pygame.sprite.spritecollide(self, block_group, False, False)
            if len(hit) > 0:
                return False
            hit = pygame.sprite.spritecollide(self, robot_group, False, False)
            if len(hit) > 0:
                return True
        return False