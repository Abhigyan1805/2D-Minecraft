import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 32
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Minecraft-like Game")

# Initialize the player's position
player_x, player_y = GRID_WIDTH // 2, GRID_HEIGHT // 2

# Create a simple grid-based world
def generate_world():
    return [[random.choice([0, 1]) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

world = generate_world()

# Initialize the time variables
last_update_time = time.time()
move_delay = 0.1

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate time since the last update
    current_time = time.time()
    time_elapsed = current_time - last_update_time

    if time_elapsed >= move_delay:
        # Handle player input (e.g., movement)
        keys = pygame.key.get_pressed()

        dx, dy = 0, 0

        if keys[pygame.K_LEFT]:
            dx = -1
        if keys[pygame.K_RIGHT]:
            dx = 1
        if keys[pygame.K_UP]:
            dy = -1
        if keys[pygame.K_DOWN]:
            dy = 1

        # Update the player's position only if it's within the bounds
        new_x = player_x + dx
        new_y = player_y + dy

        if 0 <= new_x < GRID_WIDTH and 0 <= new_y < GRID_HEIGHT:
            player_x = new_x
            player_y = new_y

            # Check if the player is at the border and regenerate the world
            if player_x == 0:
                for row in world:
                    row.insert(0, random.choice([0, 1]))
                    row.pop()
            elif player_x == GRID_WIDTH - 1:
                for row in world:
                    row.append(random.choice([0, 1]))
                    row.pop(0)

            if player_y == 0:
                new_row = [random.choice([0, 1]) for _ in range(GRID_WIDTH)]
                world.insert(0, new_row)
                world.pop()
            elif player_y == GRID_HEIGHT - 1:
                new_row = [random.choice([0, 1]) for _ in range(GRID_WIDTH)]
                world.append(new_row)
                world.pop(0)

        # Update the last update time
        last_update_time = current_time

    # Clear the screen
    screen.fill((0, 0, 0))

    # Render the world
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if world[y][x] == 0:
                pygame.draw.rect(screen, GREEN, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
            else:
                pygame.draw.rect(screen, WHITE, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Render the player as a 1x1 red pixel
    pygame.draw.rect(screen, RED, (player_x * GRID_SIZE, player_y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    pygame.display.update()

pygame.quit()
