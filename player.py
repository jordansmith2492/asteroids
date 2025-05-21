import pygame # Import the pygame library
from constants import * # Import all constants from the constants module
from circleshape import CircleShape # Import the CircleShape class from the circleshape module

class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0

	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]

	def draw(self, screen):
		self.screen = screen
		pygame.draw.polygon(self.screen, (255, 255, 255), self.triangle(), width=2)

	def rotate(self, dt):
		self.rotation += dt * PLAYER_TURN_SPEED

	def update(self, dt):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a]:
			self.rotate(dt)
		if keys[pygame.K_d]:
			self.rotate(-dt)