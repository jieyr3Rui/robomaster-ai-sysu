# class robot
import pygame
import numpy as np
from elements.bullet import bullet

vec = pygame.math.Vector2
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
        self.pos = vec(x, y)
        self.rect.center = self.pos
        self.bullet = bullet
        self.hp = hp
        self.shoot_time = 30

    def shoot(self):
        if bullet > 0:
            self.bullet
        return False, [0,0,0]

    def move(self, vx, vy, rotate, block_group):
        new_pos = self.pos + vec(vx, vy)
        new_yaw = self.yaw + rotate
        self.image = pygame.transform.rotate(self.origin, new_yaw)
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = new_pos
        if pygame.sprite.spritecollide(self,block_group,False,False):
            self.rect.center = self.pos
            return False
        else:
            self.pos = new_pos
            self.yaw = new_yaw
            return True
        
    


