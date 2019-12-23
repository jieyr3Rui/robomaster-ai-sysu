import numpy as np

# block.py
class block_virtual(object):
    def __init__(self, x, y, l, w):
        self.x, self.y, self.l, self.w = x, y, l, w

    def hit_bullet(self, bullet):
        if abs(self.x - bullet.x) < (self.w + bullet.r) and \
           abs(self.y - bullet.y) < (self.l + bullet.r) :
            return True
        return False
        
    
    def hit_robot(self, robot):
        
        return


# bullet.py
class bullet_virtaul(object):
    def __init__(self, player, x, y, yaw):
        self.x, self.y, self.yaw = x, y, yaw
        self.v = 10
        self.player = player
    
    def move(self, plist_block):
        self.x += self.v * np.math.cos(self.yaw)
        self.y += self.v * np.math.sin(self.yaw)
        return

    def hit(self, player):

        return

# robot.py
class robot_virtual(object):
    def __init__(self, player, x, y, yaw):
        self.x, self.y, self.yaw = x, y, yaw
        self.r = 90
        self.bullet = 100
        self.hp = 100
        self.p = np.zeros([4, 2])
        self.bullet = []

    def shoot(self):

        return

    def move(self, vx, vy, rotate, plist_block):
        new_bullet = bullet_virtaul()
        return

    def act(self, action):

        return

    def shape(self):
        return




# game.py
#   5100
#   ^ y
#   |
#   |   o
#   |  
# --|---------> x 8100
#   |
class game_virtual(object):
    def __init__(self):
        self.me = robot_virtual(100, 100, 0)
        self.em = robot_virtual(7500, 4500, 0)
        self.block = []
        
    def step(self, action_me, action_em):
        return
    
    def reward(self):
        return