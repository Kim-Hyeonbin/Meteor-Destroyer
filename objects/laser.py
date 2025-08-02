from objects.object import Object


class Laser(Object):
    def __init__(self, x, y):
        super().__init__("assets/images/laser.png")
        self.x = x
        self.y = y
        self.speed = 600

    def move(self, delta_seconds):
        self.y -= 600 * delta_seconds
