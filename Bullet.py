import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Assets/Enemies/BasicEnemy.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.x = x
        self.y = y
        self.direction = direction
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 10
        self.lifecount = 0

    def update(self):
        self.lifecount += 1
        if self.lifecount >= 120:
            self.kill()
        self.rect.move_ip(self.direction.x * 10, self.direction.y * 10)