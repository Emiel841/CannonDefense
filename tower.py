import pygame
import math
from Bullet import Bullet

class Tower(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = pygame.image.load('Assets/Towers/Cannon.png').convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (80, 80))
        self.original_image = pygame.transform.rotate(self.original_image, -90)
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.pos_vector = pygame.math.Vector2(x, y)
        self.range = 4*80
        self.fire_rate = 30
        self.fire_count = 0
        self.bullets = pygame.sprite.Group()



    def update(self, enemies):
        for enemy in enemies:
            target_pos_vec = pygame.math.Vector2(enemy.rect.x, enemy.rect.y+40)
            direction = target_pos_vec - self.pos_vector
            if direction.length() <= self.range:
                break

        direction = target_pos_vec - self.pos_vector

        self.fire_count += 1

        if direction.length() <= self.range:
            angle = math.degrees(math.atan2(-direction.y, direction.x))
            self.image = pygame.transform.rotate(self.original_image, angle)
            self.rect = self.image.get_rect(center=self.pos_vector)
            if self.fire_count >= self.fire_rate:
                self.fire_count = 0
                bullet = Bullet(self.rect.x+40, self.rect.y+40, direction.normalize())
                self.bullets.add(bullet)

        if self.bullets:
            self.bullets.update()

