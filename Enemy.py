from math import trunc

import pygame

class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y, speed, hp):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Assets/Enemies/BasicEnemy.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80))


        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.path_counter = 0
        self.count = 0
        self.hp = hp

    def lose_hp(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.kill()
            return True

    def update(self, path):
        self.count += 1

        if self.count >= 80/self.speed:
            self.count = 0
            self.path_counter += 1
        if path[self.path_counter] == "L":
            self.rect = self.rect.move(-self.speed, 0)
        elif path[self.path_counter] == "U":
            self.rect = self.rect.move(0, -self.speed)
        elif path[self.path_counter] == "D":
            self.rect = self.rect.move(0, self.speed)
        elif path[self.path_counter] == "R":
            self.rect = self.rect.move(self.speed, 0)
        elif path[self.path_counter] == "K":
            self.kill()

