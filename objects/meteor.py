import random
from constants import *
from objects.object import Object
from objects.collider_mixin import ColliderMixin


class Meteor(Object, ColliderMixin):

    def __init__(self, image_path, image_size, speed, resistance, score):
        Object.__init__(self, image_path, image_size)
        ColliderMixin.__init__(self, "circle")

        # 서브클래스들의 속도를 다르게 하기 위한 speed 속성 추가
        self.speed = speed

        # x좌표를 무작위로 설정
        center_x = self.image.get_width() // 2
        center_y = self.image.get_height()
        self.x = random.randint(center_x, SCREEN_WIDTH - center_x)
        self.y = -center_y
        self.resistance = resistance
        self.score = score

    # speed 값에 따라 각기 다른 속도로 하강
    def move(self, delta_seconds):
        self.y += delta_seconds * self.speed


# 서로 다른 크기, 속도, 이미지의 메테오 클래스 세 개
class SmallMeteor(Meteor):

    def __init__(
        self,
        image_path="assets/images/meteor_small.png",
        image_size=3,
        speed=800,
        resistance=4,
        score=50,
    ):
        super().__init__(image_path, image_size, speed, resistance, score)


class MediumMeteor(Meteor):

    def __init__(
        self,
        image_path="assets/images/meteor_medium.png",
        image_size=5,
        speed=500,
        resistance=8,
        score=100,
    ):
        super().__init__(image_path, image_size, speed, resistance, score)


class BigMeteor(Meteor):

    def __init__(
        self,
        image_path="assets/images/meteor_big.png",
        image_size=10,
        speed=400,
        resistance=15,
        score=500,
    ):
        super().__init__(image_path, image_size, speed, resistance, score)


# 메테오 생성용 정적 메서드
class MeteorFactory:

    @staticmethod
    def create_random_meteor():
        rand = random.random()
        if rand < 0.6:
            return MediumMeteor()
        elif rand < 0.9:
            return SmallMeteor()
        else:
            return BigMeteor()
