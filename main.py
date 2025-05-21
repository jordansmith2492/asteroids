# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import * 


def main():
    pygame.init()  # Initialize all imported pygame modules
    clock = pygame.time.Clock()  # Create a clock object to control the frame rate
    dt = 0  # Initialize delta time
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Set the screen size

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.Surface.fill(screen, (0, 0, 0), rect=None)  # Fill the screen with black
        pygame.display.flip()
        clock.tick(60)  # Control the frame rate to 60 FPS
        dt = clock.tick(60) / 1000.0

if __name__ == "__main__":
    main()
