
from kivy.uix.image import Image
class lokiChester(Image):
    def moveLeft(self):
        self.pos = (self.pos[0] - 10, self.pos[1])