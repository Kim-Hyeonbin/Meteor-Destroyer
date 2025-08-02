from constants import *
from objects.object import Object
from objects.collider_mixin import ColliderMixin


class PlayerShip(Object, ColliderMixin):
    def __init__(self):
        Object.__init__(self, "assets/images/sheep.png", 10)
        ColliderMixin.__init__("mask")

        # 생성 시 화면 중앙의 하단에 위치 설정
        self.x = SCREEN_WIDTH - self.image.get_width() / 2
        self.y = SCREEN_HEIGHT - self.image.get_height() / 2

    # 마우스를 따라 움직임
    def move(self):
        self.x, self.y = pygame.mouse.get_pos()
