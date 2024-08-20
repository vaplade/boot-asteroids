import pygame
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        position = pygame.Vector2(self.x, self.y)
        rotation = 0
        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]