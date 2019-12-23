# class block
import pygame

class block(pygame.sprite.Sprite):
    def __init__(self, image, x, y, l, w):
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y, self.l, self.w = x, y, l, w

    def hit_bullet(self, x, y, r):
        if abs(self.x - x) < (self.w + r) and \
           abs(self.y - y) < (self.l + r):
            return True
        return False
        
    def hit_robot(self, x, y, r):
        if abs(self.x - x) < (self.w + r) and \
           abs(self.y - y) < (self.l + r):
            return True
        return False
