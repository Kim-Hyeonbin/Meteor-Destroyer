import pygame
import score
from scene_manager import SceneManager
from scenes.base_scene import BaseScene
from constants import *


class GameOverScene(BaseScene):

    def enter_scene(self):
        pygame.mixer.music.pause()

    def exit_scene(self):
        score.score = 0

    def on_key_down(self, key):
        if key == pygame.K_RETURN:
            SceneManager.instance.change_scene("title")

    def on_render(self, screen):

        font = pygame.font.SysFont("Goudy Stout", 70)
        text = font.render(f"Your score : {score.score}", False, (255, 255, 255))
        text_rect = text.get_rect(
            center=(screen.get_width() / 2, screen.get_height() / 2 + 30)
        )
        screen.blit(text, text_rect)

        game_over_text = pygame.image.load("assets/images/gameover.png")
        screen.blit(
            game_over_text,
            (
                SCREEN_WIDTH / 2 - game_over_text.get_width() / 2,
                SCREEN_HEIGHT / 2 - game_over_text.get_height() / 2 + 10,
            ),
        )
