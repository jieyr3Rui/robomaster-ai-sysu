# class robot
import pygame
import numpy as np

class robot_virtual(pygame.sprite.Sprite):
    def __init__(self, image, player, x, y, yaw, bullet=100, hp=100):
        pygame.sprite.Sprite.__init__(self)
        self.player = player
        self.x, self.y, self.yaw = x, y, yaw
        self.r = 90
        self.bullet = bullet
        self.hp = hp

    def shoot(self):
        if self.bullet > 0:
            self.bullet -= 1
            return True, [self.x, self.y, self.yaw]
        return False, [0,0,0]

    def move(self, vx, vy, rotate, plist_block):
        new_x   = self.x     + vx
        new_y   = self.y     + vy
        new_yaw = self.yaw   + rotate
        for block in plist_block:
            if block.hit_robot(new_x, new_y, self.r):
                return False
        self.x = new_x
        self.y = new_y
        self.yaw = new_yaw
        return True

