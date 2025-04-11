from circleshape import CircleShape
import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN, SCREEN_HEIGHT, SCREEN_WIDTH
from shot import Shot

class Player(CircleShape):
    
    # Initialize the Player with a position and default rotation.
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0
        
    # Calculate the points for a triangle representing the player's ship.
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        # Compute the right vector to determine the triangle's base.
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius # Front point of the triangle.
        b = self.position - forward * self.radius - right # Rear left point.
        c = self.position - forward * self.radius + right # Rear right point.
        return [a, b, c]
    
    # Render the player's triangle on the given screen.
    def draw(self, screen):
        pygame.draw.polygon(screen, 'yellow', self.triangle(), 2)


    def rotate(self, dt):
        # Update the player's rotation based on their turn speed and the time passed
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        # Modify the player's position.
        # We start with a unit vector pointing straight up from (0, 0) to (0, 1).
        # We rotate that vector by the player's rotation, so it's pointing in the direction the player is facing.
        # We multiply by PLAYER_SPEED * dt. A larger vector means faster movement.
        # Add the vector to our position to move the player.
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shot_cooldown > 0:
            return
        self.shot_cooldown = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
    
    def update(self, dt):
        self.shot_cooldown -= dt
        
        # Get the current state of all keyboard keys
        keys = pygame.key.get_pressed()

        # Check if the 'a' key (left) is pressed
        # Rotate the player counterclockwise by passing negative 'dt'
        if keys[pygame.K_a]: 
            self.rotate(-dt) # -
        
        # Check if the 'd' key (right) is pressed
        # Rotate the player clockwise by passing positive 'dt'
        if keys[pygame.K_d]: 
            self.rotate(dt) # +

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

        # Clamp the player's position to stay within screen bounds
        if self.position.x - self.radius < 0:
            self.position.x = self.radius

        if self.position.x + self.radius > SCREEN_WIDTH:
            self.position.x = SCREEN_WIDTH - self.radius

        if self.position.y - self.radius < 0:
            self.position.y = self.radius

        if self.position.y + self.radius > SCREEN_HEIGHT:
            self.position.y = SCREEN_HEIGHT - self.radius
