import random

import pygame
from game.bullet import Bullet
from game.enemy import Enemy
from game.player import Player

# 初始化遊戲
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('飛機大戰')

# 加載資產
bg_num = random.randint(1, 4)
bg_image = pygame.image.load(f'assets/bg{bg_num}.png')
icon = pygame.image.load('assets/ufo.png')
pygame.display.set_icon(icon)

# 添加背景音效
pygame.mixer.music.load('assets/bg.wav')
pygame.mixer.music.play(-1)  # 單曲循環
explosion_sound = pygame.mixer.Sound('assets/exp.wav') #創建射中音效

# 初始化玩家
player = Player(400, 500)

# 初始化敵人
#保存所有的敵人
enemies = [Enemy() for _ in range(random.randint(6, 10))]

# 初始化子彈
bullets = []

# 分數
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

def show_score(score):
    score_text = f"Score: {score}"
    score_render = font.render(score_text, True, (0, 255, 0))
    screen.blit(score_render, (10, 10))

# 遊戲結束檢查
is_over = False
over_font = pygame.font.Font('freesansbold.ttf', 64)

def check_is_over():
    if is_over:
        over_text = "Game Over"
        over_render = over_font.render(over_text, True, (255, 0, 0))
        screen.blit(over_render, (200, 250))

# 遊戲主迴圈
running = True
while running:
    screen.blit(bg_image, (0, 0))
    show_score(score)

    # 事件監控
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.step = 5
            elif event.key == pygame.K_LEFT:
                player.step = -5
            elif event.key == pygame.K_SPACE:
                bullets.append(Bullet(player.x, player.y))
        if event.type == pygame.KEYUP:
            player.step = 0

    # 更新玩家狀態
    player.move()
    player.draw(screen)

    # 更新敵人狀態
    for enemy in enemies:
        enemy.move()
        enemy.draw(screen)
        if enemy.y > 450:
            is_over = True
            enemies.clear()

    # 更新子彈狀態
    for bullet in bullets[:]:
        bullet.move()
        is_hit,score = bullet.hit(enemies, explosion_sound, score)
        if is_hit:
            bullets.remove(bullet)
        bullet.draw(screen)

    check_is_over()
    pygame.display.update()
