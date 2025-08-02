from objects.object import Object


class Laser(Object):
    def __init__(self, x, y):
        super().__init__(image_path="assets/images/laser.png", image_size=2)
        self.x = x - self.image.get_width() / 2
        self.y = y
        self.speed = 600

    def move(self, delta_seconds):
        self.y -= 600 * delta_seconds
