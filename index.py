import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Blocks")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_COLOR = (0, 128, 255)
BLOCK_COLOR = (255, 0, 0)

# Player settings
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - player_size - 10
player_speed = 7

# Block settings
block_size = 50
block_speed = 5
blocks = []

# Clock
clock = pygame.time.Clock()

# Score
score = 0
font = pygame.font.SysFont("Arial", 30)

def draw_player(x, y):
    pygame.draw.rect(screen, PLAYER_COLOR, (x, y, player_size, player_size))

def draw_block(x, y):
    pygame.draw.rect(screen, BLOCK_COLOR, (x, y, block_size, block_size))

def show_score(score):
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

def game_over():
    text = font.render("Game Over!", True, WHITE)
    screen.blit(text, (WIDTH // 2 - 80, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

# Game loop
running = True
while running:
    clock.tick(60)
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Spawn blocks
    if random.randint(1, 30) == 1:
        blocks.append([random.randint(0, WIDTH - block_size), -block_size])

    # Move blocks
    new_blocks = []
    for block in blocks:
        block[1] += block_speed
        if block[1] < HEIGHT:
            new_blocks.append(block)

        # Collision detection
        if (player_x < block[0] + block_size and
            player_x + player_size > block[0] and
            player_y < block[1] + block_size and
            player_y + player_size > block[1]):
            game_over()

    blocks = new_blocks

    # Draw player and blocks
    draw_player(player_x, player_y)
    for block in blocks:
        draw_block(block[0], block[1])

    # Update score
    score += 1
    show_score(score)

    # Increase difficulty
    if score % 500 == 0:
        block_speed += 1

    pygame.display.flip()

pygame.quit()
