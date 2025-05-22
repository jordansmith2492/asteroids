import pygame
import random
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

class TitleScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font_large = pygame.font.Font(None, 100)
        self.font_small = pygame.font.Font(None, 36)
    
        self.bg_asteroids = pygame.sprite.Group()
        self.updatable = pygame.sprite.Group()
        AsteroidField.containers = (self.bg_asteroids, self.updatable)
        Asteroid.containers = (self.bg_asteroids, self.updatable)
        self.asteroid_field = AsteroidField()

    def run(self):
        clock = pygame.time.Clock()

        while True:
            dt = clock.tick(60) / 1000.0
            self.updatable.update(dt)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    # Clear title groups
                    self.bg_asteroids.empty()
                    self.updatable.empty()
                
                    # Reset screen (fill black once before leaving)
                    self.screen.fill((0,0,0))
                    pygame.display.flip()
                    return
                
            self.screen.fill((0, 0, 0))

            self.asteroid_field.update(dt)
            self.bg_asteroids.update(dt)

            for asteroid in self.bg_asteroids:
                if isinstance(asteroid, Asteroid):
                    asteroid.draw(self.screen)

            title = self.font_large.render("Asteroids", True, (255, 255, 255))
            prompt = self.font_small.render("Press Enter to Start", True, (255, 255, 255))
            self.screen.blit(title, ((SCREEN_WIDTH - title.get_width()) // 2, SCREEN_HEIGHT // 3))
            self.screen.blit(prompt, ((SCREEN_WIDTH - prompt.get_width()) // 2, SCREEN_HEIGHT // 2))

            pygame.display.flip()