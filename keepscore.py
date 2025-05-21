import os  # Import the os module for file operations
import pygame # Import the pygame library
from constants import *  # Import all constants from the constants module

class KeepScore():
    def __init__(self):
        self.score = 0
        self.highscore = self.load_highscore()
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        highscore_text = self.font.render(f"Highscore: {self.highscore}", True, (255, 255, 255))
        score_text_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, 20))
        highscore_text_rect = highscore_text.get_rect(center=(SCREEN_WIDTH // 2, 50))
        screen.blit(score_text, score_text_rect)
        screen.blit(highscore_text, highscore_text_rect)

    def add_score(self, points):
        self.score += points
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highscore()

    def save_highscore(self):
        with open("highscore.txt", "w") as f:
            f.write(str(self.highscore))

    def load_highscore(self):
        if os.path.exists("highscore.txt"):
            with open("highscore.txt", "r") as f:
                return int(f.read().strip())
        return 0