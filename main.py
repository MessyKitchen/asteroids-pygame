import pygame
from constants import *
from player import Player


def main():
    # Initialize all imported Pygame modules
    pygame.init()
    
    # Instantiate the Player object at the center of the screen 
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # Set up the drawing window with predefined dimensions
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Diagnostic output
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    

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

        # Render the player onto the screen in its current state
        player.draw(screen)

        # Update the entire display
        pygame.display.update()
        
        # Limit frame rate to 60 and get the time since the last frame
        # Convert from milliseconds to seconds for easier physics calculation
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()