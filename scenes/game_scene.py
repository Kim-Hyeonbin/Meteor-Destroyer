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

        self.launch_laser = False
        self.for_burst = 0
        self.num_laser = 0

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
        # 마우스 포인터를 숨김과 동시에 시작 위치로 이동
        pygame.mouse.set_pos((SCREEN_WIDTH / 2, SCREEN_HEIGHT - 200))
        pygame.mouse.set_visible(False)

    def exit_scene(self):
        # Scene이 시작되면 생성된 객체 일괄 삭제
        self.lasers.clear()
        self.small_meteors.clear()
        self.medium_meteors.clear()
        self.big_meteors.clear()

    def on_mouse_button_down(self, button):
        if button == 1:
            self.launch_laser = True
            self.for_burst = pygame.time.get_ticks()
            self.num_laser = 0

    def on_update(self, delta_seconds):
        self.player_ship.update(delta_seconds)

        # 3발 점사를 위한 구문
        now = pygame.time.get_ticks()
        if self.launch_laser:
            if now >= self.for_burst + self.num_laser * 100:  # 100ms 간격
                self.lasers.append(
                    Laser(
                        self.player_ship.x + self.player_ship.image.get_width() / 2,
                        self.player_ship.y,
                    )
                )
                self.laser_sound.play()
                self.num_laser += 1
                if self.num_laser >= 3:
                    self.launch_laser = False

        print(len(self.lasers))
        for laser in self.lasers:
            laser.update(delta_seconds)
            if laser.y < 0:
                self.lasers.remove(laser)

    def on_render(self, screen):
        self.player_ship.draw(screen)

        for laser in self.lasers:
            laser.draw(screen)
