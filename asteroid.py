import pygame  # Import the pygame library
from circleshape import CircleShape  # Import the CircleShape class from the circleshape module

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, width=2)

	def update(self, dt):
		self.position += self.velocity * dt