import pygame
from scene_manager import SceneManager
from scenes.base_scene import BaseScene


class GameOverScene(BaseScene):
    def on_key_down(self, key):
        if key == pygame.K_RETURN:
            SceneManager.instance.change_scene("title")

    def on_render(self, surface):
        font = pygame.font.Font(None, 50)
        text = font.render("Game over scene to be implemented", True, (255, 0, 0))
        text_rect = text.get_rect(
            center=(surface.get_width() / 2, surface.get_height() / 2)
        )
        surface.blit(text, text_rect)
