import pygame
import math

# Initialize Pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Load sprite images
source_image = pygame.image.load("Assets/Towers/Cannon.png").convert_alpha()
target_image = pygame.image.load("Assets/Enemies/BasicEnemy.png").convert_alpha()
source_image = pygame.transform.scale(source_image, (100, 100))
target_image = pygame.transform.scale(target_image, (100, 100))

# Scale images (optional)
source_image = pygame.transform.scale(source_image, (50, 50))
target_image = pygame.transform.scale(target_image, (50, 50))

# Sprite positions
source_pos = pygame.Vector2(400, 300)  # Center of the screen
target_pos = pygame.Vector2(600, 400)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((30, 30, 30))

    # Calculate angle between sprites
    direction = target_pos - source_pos
    angle = math.degrees(math.atan2(-direction.y, direction.x))  # Negative y because Pygame's y-axis is inverted

    # Rotate the source image
    rotated_image = pygame.transform.rotate(source_image, angle-90)
    rotated_rect = rotated_image.get_rect(center=source_pos)

    target_pos.x -= 5
    target_pos.y -= 1

    # Draw sprites
    screen.blit(rotated_image, rotated_rect.topleft)
    screen.blit(target_image, target_pos - (25, 25))  # Center the target image

    # Update the display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
