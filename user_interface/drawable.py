from abc import ABC, abstractmethod
import pygame as py
from pygame.math import Vector2 as Vector

class Drawable(ABC):
    def __init__(self, x: int, y: int, width: int, height: int, is_drawing: bool):
        self.rendered: Optional[Surface] = None
        self.x = x
        self.y = y
        print(type(self.x).__name__)
        if not type(self.x).__name__ == 'NoneType':
            self.pos = Vector(x,y)
        else:
            self.is_drawing = False
        self.width = width
        self.height = height
        self.is_drawing = is_drawing

    @abstractmethod
    def _render(self) :
        pass

    def render(self):
        self.rendered: Optional[Surface] = self._render()

    def draw(self, window):
        if self.is_drawing:
            if self.rendered is None:
                self.render()
            window.blit(self.rendered, self.pos)
