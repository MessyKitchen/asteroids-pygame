from circleshape import CircleShape
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius) # Initializes position using the parent class constructor
        self.radius = radius
        self.x = x
        self.y = y

    def draw(self, screen):
        # Draw the asteroid on the game screen as a circle with the given position, radius, and outline width
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius, 2)

    def update(self, dt):
        # Apply the velocity to the position based on the time delta
        self.x += self.velocity.x * dt
        self.y += self.velocity.y * dt
