from constants import *
from objects.object import Object
from objects.collider_mixin import ColliderMixin


class PlayerShip(Object, ColliderMixin):
    def __init__(self):
        Object.__init__(self, "assets/images/ship.png", 4)
        ColliderMixin.__init__(self, "mask")

    # 마우스를 따라 움직임
    def move(self, delta_seconds):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        self.x = mouse_x - self.image.get_width() // 2
        self.y = mouse_y - self.image.get_height() // 2
