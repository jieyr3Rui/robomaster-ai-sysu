# class bullet
import pygame
import numpy as np

class bullet(pygame.sprite.Sprite):
    def __init__(self, image, player, x, y, yaw, v=10):
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y, self.yaw = x, y, yaw
        self.v = v
        self.player = player
    
    def move(self, plist_block, robot):
        new_x = self.x + self.v * np.math.cos(self.yaw)
        new_y = self.y + self.v * np.math.sin(self.yaw)
        for block in plist_block:
            if block.hit_bullet(new_x, new_y, self.r):
                return 'block'
        if ((robot.x - self.x) * (robot.x - self.x) + (robot.y - self.y) * (robot.y - self.y)) < (self.r * self.r):
            return 'robot'
        self.x = new_x
        self.y = new_y
        return 'move'

        