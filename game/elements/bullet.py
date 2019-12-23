# class bullet
import pygame
import numpy as np

class bullet(pygame.sprite.Sprite):
    def __init__(self, image, player, x, y, yaw):
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y, self.yaw = x, y, yaw
        self.v = 10
        self.player = player
    
    def move(self, plist_block):
        self.x += self.v * np.math.cos(self.yaw)
        self.y += self.v * np.math.sin(self.yaw)
        return

    def hit(self, robot):
        
        return
        