import pygame
from scene_manager import SceneManager
from scenes.base_scene import BaseScene
from constants import *


class TitleScene(BaseScene):

    def enter_scene(self):
        pygame.mixer.music.unpause()

    def on_key_down(self, key):
        if key == pygame.K_RETURN:
            SceneManager.instance.change_scene("game")

    def on_render(self, screen):

        title_text = pygame.image.load("assets/images/title.png")
        screen.blit(
            title_text,
            (
                SCREEN_WIDTH / 2 - title_text.get_width() / 2,
                SCREEN_HEIGHT / 2 - title_text.get_height() / 2,
            ),
        )
