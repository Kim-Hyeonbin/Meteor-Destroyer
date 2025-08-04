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

        # 점수 출력
        font_1 = pygame.font.SysFont("Goudy Stout", 70)
        text_1 = font_1.render(f"Your score : {score.score}", False, (255, 255, 255))
        text_rect_1 = text_1.get_rect(
            center=(screen.get_width() / 2, screen.get_height() / 2 - 70)
        )
        screen.blit(text_1, text_rect_1)

        # 랭킹 출력
        font_2 = pygame.font.SysFont("Goudy Stout", 35)
        text_2 = font_2.render(score.read_ranking(), False, (255, 255, 255))
        text_rect_2 = text_2.get_rect(
            center=(screen.get_width() / 2, screen.get_height() / 2 + 300)
        )
        screen.blit(text_2, text_rect_2)

        # 게임 오버 이미지 출력
        game_over_image = pygame.image.load("assets/images/gameover.png")
        screen.blit(
            game_over_image,
            (
                SCREEN_WIDTH / 2 - game_over_image.get_width() / 2,
                SCREEN_HEIGHT / 2 - game_over_image.get_height() / 2 - 90,
            ),
        )
