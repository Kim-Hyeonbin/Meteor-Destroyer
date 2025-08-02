import pygame


class Object:

    # 오브젝트의 기본 생성자. 이미지 경로, 이미지 크기, x좌표와 y좌표, 충돌 타입을 매개 변수로 받음
    def __init__(self, image_path, image_size):

        # 이미지 생성 로직
        original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(
            original_image,
            (
                original_image.get_width() * image_size,
                original_image.get_height() * image_size,
            ),
        )

        # 좌표 할당 로직
        self.x = 0
        self.y = 0

    # 객체의 각 꼭짓점을 반환
    @property
    def rect(self):
        return pygame.Rect(
            self.x, self.y, self.image.get_width(), self.image.get_height()
        )

    # 매 프레임 마다 호출할 업데이트 메서드. 추후 확장을 위해 선언
    def update(self, delta_seconds):
        self.move(delta_seconds)

    # 오브젝트를 움직이는 함수. 각 서브클래스에서 구현
    def move(self, delta_seconds):
        pass

    # 객체를 화면에 그리는 메서드. 현재 화면을 매개 변수로 받음
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
