import random
from constants import *
from objects.object import Object


class Meteor(Object):

    def __init__(self, image_path, image_size):
        super().__init__(image_path, image_size)

        # 서브클래스들의 속도를 다르게 하기 위한 speed 속성 추가
        self.speed = 0

        # x좌표를 무작위로 설정
        center_x = self.image.get_width() // 2
        center_y = self.image.get_height()
        self.x = random.randint(center_x, SCREEN_WIDTH - center_x)
        self.y = -center_y

    # speed 값에 따라 각기 다른 속도로 하강
    def move(self, delta_seconds, speed):
        self.y += delta_seconds * speed
