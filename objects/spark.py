from objects.object import Object


class Spark(Object):

    def __init__(self, x, y):
        super().__init__(image_path="assets/images/spark.png", image_size=2)
        self.x = x - self.image.get_width() / 2
        self.y = y - self.image.get_height() / 2
        self.duration = 0.15

    def update(self, delta_seconds):
        super().update(delta_seconds)
        self.duration -= delta_seconds

    def is_finished(self):
        return self.duration <= 0
