import pygame


class ColliderMixin:

    # 기본 생성자. 피격 타입을 정할 매개 변수를 "circle", "mask"의 두 문자열 형식으로 받음
    def __init__(self, collision_type):
        col_type_dic = {"circle": "c", "mask": "m"}
        self.collision_type = col_type_dic.get(collision_type, "m")

    @property
    def mask(self):
        return pygame.mask.from_surface(self.image)

    # 객체의 피격 타입에 따른 피격 메서드를 반환하는 메서드
    def collides_with(self, other):

        # 피격 객체의 피격 타입이 "circle"일 때
        if self.collision_type == "c":
            center = self.rect.center
            radius = self.rect.width / 2

            closest_x = max(other.rect.left, min(center[0], other.rect.right))
            closest_y = max(other.rect.top, min(center[1], other.rect.bottom))

            dx = center[0] - closest_x
            dy = center[1] - closest_y

            return dx**2 + dy**2 <= radius**2

        else:
            offset = (other.rect.left - self.rect.left, other.rect.top - self.rect.top)

            return self.mask.overlap(other.mask, offset) is not None
