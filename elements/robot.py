# class robot
import pygame
import numpy as np
from elements.bullet import bullet
from define import *

vec = pygame.math.Vector2
class robot(pygame.sprite.Sprite):
    def __init__(self, image_path, player, x, y, yaw, bullet_num=100, hp=100):
        pygame.sprite.Sprite.__init__(self)
        self.bullet_group = pygame.sprite.Group()
        self.player = player
        self.yaw = yaw
        self.image_path = image_path
        self.origin = pygame.image.load(self.image_path).convert()
        rect_origin = self.origin.get_rect()
        self.w = rect_origin.w
        self.h = rect_origin.h
        self.image = pygame.transform.rotate(self.origin, yaw)
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        self.rect.center = self.pos
        self.bullet_num = bullet_num
        self.hp = hp
        self.shoot_time = 30

    def shoot(self, sh, robot_group, block_group, color=red):
        if self.shoot_time > 0:
            self.shoot_time -= 1
        if (self.bullet_num > 0) and (self.shoot_time == 0) and (sh == 1):
            new_bullet_x = self.pos[0] - self.h/2 * np.math.sin(self.yaw * 3.1415926 / 180)
            new_bullet_y = self.pos[1] - self.h/2 * np.math.cos(self.yaw * 3.1415926 / 180)
            self.bullet_group.add(bullet(self.player, new_bullet_x, new_bullet_y, self.yaw,v=10,color=color))
            self.bullet_num -= 1
            self.shoot_time = 30

        for b in self.bullet_group:
            b.move(robot_group, block_group)
        hit = pygame.sprite.groupcollide(self.bullet_group, block_group, True, False)
        # reward 

        for robot in robot_group:
            hit = pygame.sprite.spritecollide(robot, self.bullet_group, True, False)
            hit_num = len(hit)
            while hit_num > 0:
                # reward
                robot.be_hit()
                hit_num -= 1


    def move(self, vx, vy, rotate, robot_group, block_group):
        new_pos = self.pos + vec(vx, vy)
        new_yaw = self.yaw + rotate
        self.image = pygame.transform.rotate(self.origin, new_yaw)
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = new_pos
        if pygame.sprite.spritecollide(self, block_group, False, False) or \
           pygame.sprite.spritecollide(self, robot_group, False, False):
            self.rect.center = self.pos
            return False
        else:
            self.pos = new_pos
            self.yaw = new_yaw
            return True
    
    def be_hit(self):
        self.hp -= 10
        print(self.player + ' be hit ' + 'hp = ' + str(self.hp))

    def reset(self):
        return
        
    


