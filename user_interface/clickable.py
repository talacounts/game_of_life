from pygame.math import Vector2 as Vector
from pygame import Surface
from typing import Tuple
from .drawable import Drawable


BLUE: Tuple[int] = (56, 8, 246)
RED: Tuple[int] = (246, 8, 16)
LIGHT_GRAY: Tuple[int] = (124, 124, 124)
WHITE: Tuple[int] = (255, 255, 255)


class Clickable(Drawable):
    def __init__(self, x: int, y: int, width: int, height: int):
        super(Clickable,self).__init__(x, y, width, height)
        self.x: int = x
        self.y: int = y
        self.width: int = width
        self.height: int = height
        self.pos: Vector = Vector(x, y)
        self.focused: bool = False

    def handle_click(self, mouse_pos: Vector):
        if self.x <= mouse_pos[0] < self.x + self.width and self.y <= mouse_pos[1] < self.y + self.height:
            self.on_focus()
        elif self.focused:
            self.on_unfocus()

    def on_focus(self):
        self.focused = True

    def on_unfocus(self):
        self.focused = False
