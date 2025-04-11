from circleshape import CircleShape
import pygame
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius) # Initializes position using the parent class constructor
        self.radius = radius
        self.position.x = x
        self.position.y = y

    def draw(self, screen):
        # Draw the asteroid on the game screen as a circle with the given position, radius, and outline width
        pygame.draw.circle(screen, (0, 255, 0), (self.position.x, self.position.y), self.radius, 2)


    def update(self, dt):
        # Apply the velocity to the position based on the time delta
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt

    def split(self):
        # Splits the asteroid into two smaller asteroids when destroyed
        
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        velocity_1 = self.velocity.rotate(random_angle)
        velocity_2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = velocity_1 * 1.2

        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2.velocity = velocity_2 * 1.2

        return asteroid_1, asteroid_2