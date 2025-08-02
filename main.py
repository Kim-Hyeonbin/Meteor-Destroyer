import pygame
from constants import *
from scene_manager import SceneManager
from scenes.title_scene import TitleScene
from scenes.game_scene import GameScene
from scenes.game_over_scene import GameOverScene

print("Game start")
pygame.init()
pygame.key.set_repeat(500, 300)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()

original_background_image = pygame.image.load("assets/images/background.png")
background_image = pygame.transform.scale(
    original_background_image, (SCREEN_WIDTH, SCREEN_HEIGHT)
)

SceneManager.instance.add_scene("title", TitleScene())
SceneManager.instance.add_scene("game", GameScene())
SceneManager.instance.add_scene("game_over", GameOverScene())

run = True
while run:

    for event in pygame.event.get():

        if (event.type == pygame.QUIT) or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        ):
            print("Shutdown")
            pygame.quit()
            run = False
            break

        if event.type == pygame.KEYDOWN:
            SceneManager.instance.scene.on_key_down(event.key)

        if event.type == pygame.KEYUP:
            SceneManager.instance.scene.on_key_up(event.key)

    delta_seconds = clock.tick(FPS) / 1000
    SceneManager.instance.scene.on_update(delta_seconds)

    screen.blit(background_image, (0, 0))
    SceneManager.instance.scene.on_render(screen)

    pygame.display.update()
