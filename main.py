import sys
import pygame
from constants import *
from scene_manager import SceneManager
from scenes.title_scene import TitleScene
from scenes.game_scene import GameScene
from scenes.game_over_scene import GameOverScene

# 게임 시작 메시지 출력
print("Game start")

# Pygame 초기화
pygame.init()

# bgm 설정

pygame.mixer.init()
pygame.mixer.music.load("assets/sounds/bgm.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.4)

# 키보드 입력 반복 설정 (0.5초 뒤부터 0.3초 간격)
pygame.key.set_repeat(500, 300)

# 전체화면 디스플레이 설정
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# 프레임 제한용 시계 객체 생성
clock = pygame.time.Clock()

# 배경 이미지 로드 및 화면 크기에 맞게 리사이즈
original_background_image = pygame.image.load("assets/images/background.png")
background_image = pygame.transform.scale(
    original_background_image, (SCREEN_WIDTH, SCREEN_HEIGHT)
)

# 씬 매니저에 씬 등록
SceneManager.instance.add_scene("title", TitleScene())
SceneManager.instance.add_scene("game", GameScene())
SceneManager.instance.add_scene("game_over", GameOverScene())

# 메인 게임 루프

while True:

    # 이벤트 처리 루프
    for event in pygame.event.get():

        # 종료 조건: 윈도우 종료 버튼 or ESC 키
        if (event.type == pygame.QUIT) or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        ):
            print("Shutdown")
            pygame.quit()
            sys.exit()
            break

        # 키 입력 처리 (씬에 전달)
        if event.type == pygame.KEYDOWN:
            SceneManager.instance.scene.on_key_down(event.key)

        if event.type == pygame.MOUSEBUTTONDOWN:
            SceneManager.instance.scene.on_mouse_button_down(event.button)

    # 프레임 간 시간 계산 (초 단위)
    delta_seconds = clock.tick(FPS) / 1000

    # 현재 씬 업데이트
    SceneManager.instance.scene.on_update(delta_seconds)

    # 배경 그리기
    screen.blit(background_image, (0, 0))

    # 현재 씬 렌더링
    SceneManager.instance.scene.on_render(screen)

    # 화면 갱신
    pygame.display.update()
