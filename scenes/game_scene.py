import pygame
from constants import *
from scene_manager import SceneManager
from scenes.base_scene import BaseScene
from objects.player_ship import PlayerShip
from objects.laser import Laser
from objects.meteor import Meteor, SmallMeteor, MediumMeteor, BigMeteor


class GameScene(BaseScene):

    def __init__(self):
        self.player_ship = None
        self.lasers = []
        self.small_meteors = []
        self.medium_meteors = []
        self.big_meteors = []

        self.laser_sound = pygame.mixer.Sound("assets/sounds/launch_laser.wav")
        self.meteor_explosion_sound = pygame.mixer.Sound(
            "assets/sounds/meteor_explosion.wav"
        )
        self.ship_explosion_sound = pygame.mixer.Sound(
            "assets/sounds/ship_explosion.wav"
        )

        self.laser_sound.set_volume(0.1)
        self.meteor_explosion_sound.set_volume(0.1)
        self.ship_explosion_sound.set_volume(0.1)

    def enter_scene(self):
        # Scene이 시작되면 PlayerShip 객체 생성
        self.player_ship = PlayerShip()

    def exit_scene(self):
        # Scene이 시작되면 생성된 객체 일괄 삭제
        self.lasers.clear()
        self.small_meteors.clear()
        self.medium_meteors.clear()
        self.big_meteors.clear()

    def on_key_down(self, key):
        if key == pygame.K_RETURN:
            SceneManager.instance.change_scene("game_over")

    def on_render(self, surface):
        font = pygame.font.Font(None, 50)
        text = font.render("Game scene to be implemented", True, (255, 0, 0))
        text_rect = text.get_rect(
            center=(surface.get_width() / 2, surface.get_height() / 2)
        )
        surface.blit(text, text_rect)
