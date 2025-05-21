import pygame # Import the pygame library
from constants import *  # Import all constants from the constants module

class KeepScore():
    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        score_text_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, 20))
        screen.blit(score_text, score_text_rect)

    def add_score(self, points):
        self.score += points