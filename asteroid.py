import pygame
import constants as CONST
from circleshape import CircleShape
import random
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        log_event("asteroid_split")
        self.kill()
        if self.radius <= CONST.ASTEROID_MIN_RADIUS:
            return

        splitAngle = random.uniform(*CONST.ROCK_SPLIT_RANGE)
        newRadius = self.radius - CONST.ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, newRadius)
        asteroid2 = Asteroid(self.position.x, self.position.y, newRadius)
        asteroid1.velocity = self.velocity.rotate(splitAngle) * CONST.ROCK_SPLIT_SPEED
        asteroid2.velocity = self.velocity.rotate(-splitAngle)
