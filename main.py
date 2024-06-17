import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
hits = 0
miss = 0
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
score_font = pygame.font.Font(None, 36)  # Загрузка шрифта
#score_surface = score_font.render(str(score), True, (255, 255, 255))  # Создание поверхности для текста

#score = 0

pygame.display.set_caption('Игра Тир')
icon = pygame.image.load("img/tir.jpg")
pygame.display.set_icon(icon)

target_imj = pygame.image.load("img/mish.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                hits += 1
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
            else:
                miss += 1
    delta_x = 2 * (random.randint(0, 2) - 1)
    delta_y = 2 * (random.randint(0, 2) - 1)
    if ((target_x + delta_x) > (SCREEN_WIDTH - target_width)) or ((target_x + delta_x) < 0):
        target_x -= delta_x
    else:
        target_x += delta_x
    if ((target_y + delta_y) > (SCREEN_HEIGHT - target_height)) or ((target_y + delta_y) < 0):
        target_y -= delta_y
    else:
        target_y += delta_y


    screen.blit(target_imj, (target_x, target_y))
    score = "Попал : " + str(hits) + "  Промазал : " + str(miss)
    score_surface = score_font.render(str(score), True, (255, 255, 255))  # Создание поверхности для текста
    screen.blit(score_surface, (10, 10))  # Отображение текста score на экране
    pygame.display.update()




pygame.quit()
