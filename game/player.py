import pygame


class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load('assets/player.png')
        self.x = x #玩家的X坐标
        self.y = y #玩家的Y坐标
        self.step = 0 #玩家移动的速度

    def move(self):
        self.x += self.step
        if self.x > 736:
            self.x = 736
        if self.x < 0:
            self.x = 0

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
