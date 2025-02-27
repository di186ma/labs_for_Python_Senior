import pygame
import time

pygame.init()
screen = pygame.display.set_mode((850, 150))
screen.fill((0, 0, 0))

pygame.display.set_caption("WARNING!")

font = pygame.font.SysFont("Lucida Console", 20)
label = font.render("YOU DOWNLOADED VIRUS", True, (12, 140, 0))

screen.blit(label, (50, 50))
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(label, (50, 50))
    pygame.display.update()

    time.sleep(0.10)

pygame.quit()
