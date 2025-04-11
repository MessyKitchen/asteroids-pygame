import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

# Create a group to manage all game objects that require updating each frame.
updatable = pygame.sprite.Group()
# Create a group to manage all game objects that need to be drawn to the screen.
drawable = pygame.sprite.Group() 
# Assign the Player class's containers attribute to the updatable and drawable groups.
# This ensures all Player instances are automatically added to both groups upon creation.
asteroids = pygame.sprite.Group()
# Create a group specifically for managing all Asteroid objects.
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)
Shot.containers = (shots, updatable, drawable)

def main():
    # Initialize all imported Pygame modules
    pygame.init()
    
    # Instantiate the Player object at the center of the screen 
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # Instantiate an instance of AsteroidField to handle all asteroid spawning and updates
    asteroid_field = AsteroidField()
    
    # Set up the drawing window with predefined dimensions
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Diagnostic output
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initiating score-board and score-board font
    score = 0
    font = pygame.font.SysFont("OCR A Extended", 28)


    # Intialise timing variables for framerate control
    # dt (delta time)
    dt = 0
    # Create a clock object to manage consistent game speed
    clock = pygame.time.Clock()

    # Main game loop
    while True:
        # Event Handeling - check for window close events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return # Exit the main loop to close the game
        
        # Fill the screen with black to clear the previous frame
        screen.fill((0, 0, 0))

        for object in updatable: # Iterate over all objects in the 'updatable' group and update their states based on the delta time (dt).
            object.update(dt)
        
        # Logic for Player / Asteroid collisions
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                print(f"Score:{score}")
                sys.exit()

        # Logic for SHOOT / Asteroid collisions
        for shot in shots:
            for asteroid in asteroids:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()
                    score += 75

        for sprite in drawable: # Iterate over all sprites in the 'drawable' group and draw them onto the screen.
            sprite.draw(screen)

        # Render and display the score
        score_text = font.render(f"Score: {score}", True, (0, 255, 0))  # white color
        screen.blit(score_text, (10, 10))  # top-left corner

        # Update the entire display
        pygame.display.update()
        
        # Limit frame rate to 60 and get the time since the last frame
        # Convert from milliseconds to seconds for easier physics calculation
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

# Added 'score-board', new colour scheme, player stays within screen and score print to console.