import pygame # Import the pygame library
from constants import * # Import all constants from the constants module
from circleshape import CircleShape  # Import the CircleShape class from the circleshape module
from player import Player  # Import the Player class from the player module
from asteroid import Asteroid  # Import the Asteroid class from the asteroid module
from asteroidfield import AsteroidField  # Import the AsteroidField class from the asteroidfield module
from shot import Shot  # Import the Shot class from the shot module
from keepscore import KeepScore  # Import the KeepScore class from the keepscore module

def main():
    pygame.init()  # Initialize all imported pygame modules
    clock = pygame.time.Clock()  # Create a clock object to control the frame rate
    dt = 0  # Initialize delta time
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Set the screen size

    updatable_group = pygame.sprite.Group() # Create a group for updatable objects
    drawable_group = pygame.sprite.Group() # Create a group for drawable objects
    asteroid_group = pygame.sprite.Group() # Create a group for asteroids
    shot_group = pygame.sprite.Group() # Create a group for shots
    
    Player.containers = (updatable_group, drawable_group) # Assign the groups to the Player class
    Asteroid.containers = (asteroid_group, updatable_group, drawable_group) # Assign the groups to the Asteroid class
    AsteroidField.containers = (updatable_group) # Assign the groups to the AsteroidField class
    Shot.containers = (shot_group, updatable_group, drawable_group) # Assign the groups to the Shot class

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2) # Create a player object at the center of the screen
    asteroid_field = AsteroidField() # Create an asteroid field object
    score = KeepScore() # Create a score object


    while True: # Main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Check for quit event
                return
        
        screen.fill((0, 0, 0)) # Fill the screen with black
        updatable_group.update(dt) # Update all updatable objects
        for drawable in drawable_group: # Draw all drawable objects
            drawable.draw(screen)
            score.draw(screen) # Draw the score
        for asteroid in asteroid_group:
            for shot in shot_group:
                if shot.detect_collision(asteroid): # Check for collision between shots and asteroids
                    asteroid.split() # Remove the asteroid if it is hit
                    asteroid.kill() # Remove the asteroid from the group
                    shot.kill()
                    score.add_score(1)
            if player.detect_collision(asteroid):
                print("Game over!") # Check for collision between player and asteroids
                pygame.quit()
                return
        pygame.display.flip() # Update the display
        clock.tick(60) # Control the frame rate to 60 FPS
        dt = clock.tick(60) / 1000.0 # Calculate delta time

if __name__ == "__main__":
    main()
