import random
import sys
from time import sleep

import pygame
from game.bullet import Bullet
from game.enemy import Enemy
from game.player import Player

# 初始化遊戲
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('天降怪獸：終極防線')


# 加載資產
def load_assets():
    global bg_image, icon, explosion_sound
    bg_num = random.randint(1, 4)
    bg_image = pygame.image.load(f'assets/bg{bg_num}.png')
    icon = pygame.image.load('assets/ufo.png')
    pygame.display.set_icon(icon)

    pygame.mixer.music.load('assets/bg.wav')
    pygame.mixer.music.play(-1)  # 單曲循環
    explosion_sound = pygame.mixer.Sound('assets/exp.wav')  # 創建射中音效

# 初始化遊戲狀態
def reset_game():
    global player, enemies, bullets, score, is_over, start_time, game_duration, game_over
    player = Player(400, 500)
    enemies = [Enemy() for _ in range(random.randint(6, 10))]  # 隨機生成敵人
    bullets = []
    score = 0
    is_over = False
    game_over = False
    start_time = pygame.time.get_ticks()  # 記錄遊戲開始時間
    game_duration = 15 * 1000  # 60 秒遊戲時間

# 顯示分數
font = pygame.font.Font('freesansbold.ttf', 32)
def show_score(score):
    score_text = f"Score: {score}"
    score_render = font.render(score_text, True, (0, 255, 0))
    screen.blit(score_render, (10, 10))

# 遊戲結束檢查
over_font = pygame.font.Font('freesansbold.ttf', 64)
def check_is_over(is_over,game_over):
    if is_over:
        show_game_over_screen()
        sleep(10)
        game_over = True
    return game_over
        # over_render = over_font.render(over_text, True, (255, 0, 0))
        # screen.blit(over_render, (200, 250))

# 顯示遊戲結束畫面
def show_game_over_screen():
    game_over_bg = pygame.image.load("assets/end.png")  # 載入遊戲結束背景圖片
    screen.blit(game_over_bg, (0, 0))  # 顯示背景
    font = pygame.font.SysFont(None, 55)  # 設定字體
    game_over_text = font.render("Game Over", True, (255, 255, 255))  # 顯示文字
    score_text = font.render(f"Your Score: {score}", True, (255, 255, 255))

    # 顯示文字在螢幕上
    screen.blit(game_over_text, (screen.get_width() // 2 - game_over_text.get_width() // 2, screen.get_height() // 2 + 50))
    screen.blit(score_text, (screen.get_width() // 2 - score_text.get_width() // 2, screen.get_height() // 3 + 60))
    pygame.display.update()

# 遊戲主迴圈
load_assets()
reset_game()
running = True
game_over = False  # 標記遊戲是否結束
delay = 10000  # 10 秒延遲
restart_delay = None  # 用於記錄遊戲結束後的時間點

while running:
    if not game_over:
        screen.blit(bg_image, (0, 0))
        show_score(score)

        elapsed_time = pygame.time.get_ticks() - start_time

        if elapsed_time >= game_duration:
            game_over = True
            restart_delay = pygame.time.get_ticks()  # 記錄結束時間

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.step = 5
                elif event.key == pygame.K_LEFT:
                    player.step = -5
                elif event.key == pygame.K_SPACE and not game_over:
                    bullets.append(Bullet(player.x, player.y))
            if event.type == pygame.KEYUP:
                player.step = 0

        player.move()
        player.draw(screen)

        for enemy in enemies:
            enemy.move()
            enemy.draw(screen)
            if enemy.y > 450:
                is_over = True
                enemies.clear()

        for bullet in bullets[:]:
            bullet.move()
            is_hit, score = bullet.hit(enemies, explosion_sound, score)
            if is_hit:
                bullets.remove(bullet)
            bullet.draw(screen)

        game_over = check_is_over(is_over,game_over)
        pygame.display.update()

    else:
        show_game_over_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a: # 按 'a'  鍵重新開始
                    reset_game()

        # 10 秒自動重啟
        if restart_delay and (pygame.time.get_ticks() - restart_delay >= delay):
            reset_game()
            game_over = False

pygame.quit()
sys.exit()