import pygame
import random

pygame.init()

# Screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Shooter Game")

# Colors
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

# Player
player = pygame.Rect(375, 500, 50, 50)
player_speed = 5

# Bullets
bullets = []

# Enemies
enemies = []
for i in range(5):
    enemy = pygame.Rect(random.randint(0,750), random.randint(0,200), 50, 50)
    enemies.append(enemy)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Shoot
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet = pygame.Rect(player.x+20, player.y, 10, 20)
            bullets.append(bullet)

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.x -= player_speed
    if keys[pygame.K_d]:
        player.x += player_speed
    if keys[pygame.K_w]:
        player.y -= player_speed
    if keys[pygame.K_s]:
        player.y += player_speed

    # Draw player
    pygame.draw.rect(screen, GREEN, player)

    # Bullets
    for bullet in bullets:
        bullet.y -= 10
        pygame.draw.rect(screen, WHITE, bullet)

    # Enemies
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    # Collision
    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                enemies.remove(enemy)
                if bullet in bullets:
                    bullets.remove(bullet)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
