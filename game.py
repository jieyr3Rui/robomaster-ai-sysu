# init game.py
import pygame
from elements.robot import robot
from elements.ground import ground
class game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("robomaster-ai")
        self.screen = pygame.display.set_mode((830, 530))
        self.clock = pygame.time.Clock()
        self.running = True
        self.done = False
        self.ground = ground('elements/resource/ground.png')
        self.robot1 = robot('elements/resource/robot1.png', 'robot1', 200, 200, 0)

        self.ground_group = pygame.sprite.Group()
        self.robot1_group = pygame.sprite.Group()
        self.ground_group.add(self.ground)
        self.robot1_group.add(self.robot1)



    def run(self):
        while self.running:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    print(pygame.mouse.get_pos()) 
            
            self.step()

            self.ground_group.draw(self.screen)
            self.robot1_group.draw(self.screen)
            pygame.display.update()

    def step(self):

        return
    
    def reset(self):
        return

if __name__ == '__main__':
    rm_ai = game()
    rm_ai.run()

    
        