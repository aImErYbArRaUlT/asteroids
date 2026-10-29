import pygame 

import random

from logger import log_event

from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from circleshape import CircleShape 



class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)


    def draw(self, screen: pygame.Surface) -> None:  
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> str | None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return "this was a small asteroid and now we're done"
        log_event("asteroid_split")

        first_velocity = self.velocity.rotate(random.uniform(20, 50))
        second_velocity = self.velocity.rotate(random.uniform(-20, -50))
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid_one.velocity = first_velocity * 1.2
        asteroid_two.velocity = second_velocity * 1.2
