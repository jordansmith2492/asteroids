import pygame  # Import the pygame library
import random # Import the random library for generating random numbers
from constants import *  # Import all constants from the constants module
from circleshape import CircleShape  # Import the CircleShape class from the circleshape module

class Asteroid(CircleShape, pygame.sprite.Sprite):
	def __init__(self, x, y, radius):
		pygame.sprite.Sprite.__init__(self, *self.containers)
		CircleShape.__init__(self, x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, width=2)

	def update(self, dt):
		self.position += self.velocity * dt

	def split(self): 
		if self.radius <= ASTEROID_MIN_RADIUS: 
			self.kill() 
			return
		random_angle = random.uniform(20, 50)

		direction1 = self.velocity.rotate(random_angle) * 1.5
		direction2 = self.velocity.rotate(-random_angle) * 1.5

		new_radius = self.radius - ASTEROID_MIN_RADIUS

		asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
		asteroid1.velocity = direction1
		asteroid1.add(*Asteroid.containers)
		asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
		asteroid2.velocity = direction2
		asteroid2.add(*Asteroid.containers)
		self.kill()
