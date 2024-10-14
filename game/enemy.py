import random

import pygame


class Enemy:
    def __init__(self):
        enemy_kind = random.randint(1, 4)
        self.image = pygame.image.load(f'assets/enemy{enemy_kind}.png')
        self.x = random.randint(200, 600)
        self.y = random.randint(50, 250)
        self.step = random.randint(2, 6)  #敵人移動的速度

    #當被射中時，重置位置
    def reset(self):
        self.x = random.randint(200, 600)
        self.y = random.randint(50, 200)

    def move(self):
        self.x += self.step
        if self.x > 736 or self.x < 0:
            self.step *= -1
            self.y += 40

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
