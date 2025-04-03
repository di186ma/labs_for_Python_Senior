import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Agar.io для детей")

player_size = 20
player_x, player_y = WIDTH//2, HEIGHT//2
player_color = (0, 100, 255)
player_speed = 3

foods = []
for _ in range(50):
    food_x = random.randint(0, WIDTH)
    food_y = random.randint(0, HEIGHT)
    food_color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
    foods.append([food_x, food_y, food_color])

enemies = []
for _ in range(10):
    enemy_size = random.randint(10, 30)
    enemy_x = random.randint(0, WIDTH)
    enemy_y = random.randint(0, HEIGHT)
    enemy_color = (random.randint(100, 255), 0, 0)
    enemies.append([enemy_x, enemy_y, enemy_size, enemy_color])

score = 0
font = pygame.font.SysFont(None, 36)

running = True
clock = pygame.time.Clock()

while running:
    screen.fill((240, 240, 240))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT:
        player_y += player_speed
    
    pygame.draw.circle(screen, player_color, (player_x, player_y), player_size)
    
    for food in foods[:]:
        pygame.draw.circle(screen, food[2], (food[0], food[1]), 5)
        if math.dist((player_x, player_y), (food[0], food[1])) < player_size:
            foods.remove(food)
            player_size += 0.5
            score += 1
            foods.append([random.randint(0, WIDTH), random.randint(0, HEIGHT), 
                         (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))])
    
    for enemy in enemies[:]:
        pygame.draw.circle(screen, enemy[3], (enemy[0], enemy[1]), enemy[2])
        if math.dist((player_x, player_y), (enemy[0], enemy[1])) < player_size + enemy[2]:
            if player_size > enemy[2]:
                enemies.remove(enemy)
                player_size += enemy[2]/4
                score += 5
                enemies.append([random.randint(0, WIDTH), random.randint(0, HEIGHT), 
                              random.randint(10, 30), (random.randint(100, 255), 0, 0)])
            else:
                running = False
    
    score_text = font.render(f"Очки: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
