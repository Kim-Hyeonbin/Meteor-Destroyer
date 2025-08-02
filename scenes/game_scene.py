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

    def on_mouse_button_down(self, button):
        if button == 1:
            self.lasers.append(
                Laser(self.player_ship.rect.centerx, self.player_ship.rect.top)
            )
            self.laser_sound.play()

    def on_update(self, delta_seconds):
        for laser in self.lasers:
            laser.update(delta_seconds)
            if laser.y < 0:
                self.lasers.remove(laser)

    def on_render(self, screen):
        self.player_ship.draw(screen)

        for laser in self.lasers:
            laser.draw(screen)
