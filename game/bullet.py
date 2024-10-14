import pygame
from game.utils import calculate_distance


class Bullet:
    def __init__(self, player_x, player_y):
        self.image = pygame.image.load('assets/bullet.png')
        self.x = player_x + 16
        self.y = player_y + 10
        self.step = 10

    def move(self):
        self.y -= self.step

    def hit(self, enemies, explosion_sound, score):
        for enemy in enemies:
            if calculate_distance(self.x, self.y, enemy.x, enemy.y) < 30:
                print('Hit!!!')
                explosion_sound.play()
                enemy.reset()  # 重置敵人位置
                score += 1  # 更新分數
                print(f'Score:{score}')
                return True,score  # 子彈擊中敵人後，應該刪除子彈
        return False,score

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
