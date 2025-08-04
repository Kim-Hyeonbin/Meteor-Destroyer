import pygame
from constants import *
import score
from scene_manager import SceneManager
from scenes.base_scene import BaseScene
from objects.player_ship import PlayerShip
from objects.laser import Laser
from objects.meteor import MeteorFactory, BigMeteor, MediumMeteor, SmallMeteor
from objects.effect import Spark, Explosion


class GameScene(BaseScene):

    def __init__(self):
        # 플레이어, 레이저, 메테오 객체 리스트 초기화
        self.player_ship = None
        self.lasers = []
        self.meteors = []
        self.sparks = []
        self.explosions = []

        # 점사 레이저 발사 상태 제어용 변수
        self.launch_laser = False  # 점사 시작 여부
        self.for_burst = 0  # 점사 시작 시각 (ms 단위)
        self.num_laser = 0  # 현재까지 발사한 레이저 수 (최대 3)

        # 메테오 생성 제어용 변수
        self.meteor_spawn_interval = 0.1
        self.meteor_timer = 0

        # 추가 점수 제어용 변수
        self.score_timer = 0

        # 사운드 로드 및 볼륨 설정
        self.laser_sound = pygame.mixer.Sound("assets/sounds/launch_laser.wav")
        self.meteor_explosion_sound = pygame.mixer.Sound(
            "assets/sounds/meteor_explosion.wav"
        )
        self.ship_explosion_sound = pygame.mixer.Sound(
            "assets/sounds/ship_explosion.wav"
        )
        self.meteor_hit_sound = pygame.mixer.Sound("assets/sounds/meteor_hit.wav")

        self.laser_sound.set_volume(0.2)
        self.meteor_explosion_sound.set_volume(2)
        self.ship_explosion_sound.set_volume(0.2)
        self.meteor_hit_sound.set_volume(0.8)

    def enter_scene(self):
        # 게임 씬 진입 시 플레이어 생성 및 마우스 초기 설정
        self.player_ship = PlayerShip()

        # 마우스 포인터 숨김 + 지정 위치로 이동
        pygame.mouse.set_pos((SCREEN_WIDTH / 2, SCREEN_HEIGHT - 200))
        pygame.mouse.set_visible(False)

    def exit_scene(self):
        # 씬 종료 시 객체 리스트 초기화
        self.lasers.clear()
        self.meteors.clear()
        self.sparks.clear()
        self.explosions.clear()

    def on_mouse_button_down(self, button):
        # 마우스 좌클릭 시 점사 레이저 발사 시작
        if button == 1:
            self.launch_laser = True
            self.for_burst = pygame.time.get_ticks()
            self.num_laser = 0

    def on_update(self, delta_seconds):

        # 플레이어 위치 갱신
        self.player_ship.update(delta_seconds)

        # 3발 점사 레이저 발사 처리
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

        # 0.1초 마다 메테오 객체 생성
        self.meteor_timer += delta_seconds
        while self.meteor_timer >= self.meteor_spawn_interval:
            meteor = MeteorFactory.create_random_meteor()
            if not isinstance(meteor, BigMeteor):
                meteor.image = pygame.transform.rotate(meteor.image, meteor.angel)
            self.meteors.append(meteor)
            self.meteor_timer -= self.meteor_spawn_interval

        # 추가 점수 시스템 (초당 +5점)
        self.score_timer += delta_seconds
        while self.score_timer >= 1.0:
            score.score += 5
            self.score_timer -= 1.0

        # 메테오와 레이저 충돌 검사
        for meteor in self.meteors[:]:
            for laser in self.lasers[:]:
                if meteor.collides_with(laser):
                    self.sparks.append(Spark(laser.x, laser.y))
                    self.lasers.remove(laser)
                    meteor.resistance -= 1
                    if meteor.resistance <= 0:  # 메테오의 내구도가 0이 되면 객체 삭제
                        score.score += meteor.score
                        self.meteor_explosion_sound.play()
                        # 메테오 크기에 따라 폭발 사이즈 설정
                        if isinstance(meteor, SmallMeteor):
                            self.explosions.append(
                                Explosion(
                                    meteor.x + meteor.image.get_width() / 2 - 24,
                                    meteor.y + meteor.image.get_height() / 2 - 24,
                                    3,
                                )
                            )
                        elif isinstance(meteor, MediumMeteor):
                            self.explosions.append(
                                Explosion(
                                    meteor.x + meteor.image.get_width() / 2 - 32,
                                    meteor.y + meteor.image.get_height() / 2 - 32,
                                    4,
                                )
                            )
                        elif isinstance(meteor, BigMeteor):
                            self.explosions.append(
                                Explosion(
                                    meteor.x + meteor.image.get_width() / 2 - 48,
                                    meteor.y + meteor.image.get_height() / 2 - 48,
                                    6,
                                )
                            )
                        self.meteors.remove(meteor)
                    self.meteor_hit_sound.play()
                    break

        # 플레이어와 메테오의 충돌 검사
        for meteor in self.meteors:
            if self.player_ship.collides_with(meteor):
                self.ship_explosion_sound.play()
                pygame.time.delay(10)
                SceneManager.instance.change_scene("game_over")
                break

        # 객체 업데이트 밑 화면 밖 객체 제거
        for laser in self.lasers[:]:  # 리스트 복사로 반복 중 삭제 대응
            laser.update(delta_seconds)
            if laser.y < 0:
                self.lasers.remove(laser)
        for meteor in self.meteors[:]:
            meteor.update(delta_seconds)
            if meteor.y > SCREEN_HEIGHT:
                self.meteors.remove(meteor)

        for spark in self.sparks:
            spark.update(delta_seconds)
            if spark.is_finished():
                self.sparks.remove(spark)

        for explosion in self.explosions:
            explosion.update(delta_seconds)
            if explosion.is_finished():
                self.explosions.remove(explosion)

    def on_render(self, screen):

        self.player_ship.draw(screen)

        for laser in self.lasers:
            laser.draw(screen)

        for meteor in self.meteors:
            meteor.draw(screen)

        for spark in self.sparks:
            spark.draw(screen)

        for explosion in self.explosions:
            explosion.draw(screen)

        # 화면 왼쪽 상단 스코어 출력
        font = pygame.font.SysFont("Goudy Stout", 40)
        text = font.render(f"SCORE : {score.score}", True, (255, 255, 255))
        screen.blit(text, (20, 20))
