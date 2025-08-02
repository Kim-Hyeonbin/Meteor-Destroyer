class SceneManager:

    instance = None

    def __init__(self):
        self.scenes = {}
        self.scene = None

    def add_scene(self, name, scene):
        self.scenes[name] = scene
        if self.scene is None:
            self.scene = scene
            self.scene.enter_scene()

    def change_scene(self, name):
        self.scene.exit_scene()
        self.scene = self.scenes[name]
        self.scene.enter_scene()


SceneManager.instance = SceneManager()
