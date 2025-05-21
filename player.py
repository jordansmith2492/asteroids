import pygame # Import the pygame library
from constants import * # Import all constants from the constants module
from circleshape import CircleShape # Import the CircleShape class from the circleshape module
from shot import Shot # Import the Shot class from the shot module

class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.shot_timer = 0

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

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt

	def update(self, dt):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(-dt)

		if keys[pygame.K_a]:
			self.rotate(dt)
		if keys[pygame.K_d]:
			self.rotate(-dt)

		if keys[pygame.K_SPACE]:
			Player.shoot(self)

		if self.shot_timer > 0:
			self.shot_timer -= dt
			if self.shot_timer < 0:
				self.shot_timer = 0

	def shoot(self):
		if self.shot_timer > 0:
			return
		shot = Shot(self.position.x, self.position.y)
		shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
		self.shot_timer = PLAYER_SHOOT_COOLDOWN
		return shot