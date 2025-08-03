from objects.object import Object


class Effect(Object):

    def __init__(self, image_path, image_size, x, y, duration):
        super().__init__(image_path, image_size)
        self.x = x
        self.y = y
        self.duration = duration

    def update(self, delta_seconds):
        super().update(delta_seconds)
        self.duration -= delta_seconds

    def is_finished(self):
        return self.duration <= 0


class Spark(Effect):

    def __init__(self, x, y):
        super().__init__(
            image_path="assets/images/spark.png", image_size=2, x=x, y=y, duration=0.15
        )


class Explosion(Effect):
    def __init__(self, x, y, size):
        super().__init__(
            image_path="assets/images/explosion.png",
            image_size=size,
            x=x,
            y=y,
            duration=0.2,
        )
