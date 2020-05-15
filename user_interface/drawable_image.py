from .drawable import Drawable
from engine.fs.serialization import Serializable, serialize_to_file, deserialize_from_file
from pygame.math import Vector2 as Vector
from pygame import Surface
from typing import Tuple, Dict, Any
from .drawable import Drawable
import pygame as py


class DrawableImage(Drawable):
    def __init__(self,x: int, y: int, width: int, height: int, image_path , background_color, is_drawing ):
        super(DrawableImage, self).__init__(x=x, y=y, width=width, height=height, is_drawing=is_drawing)
        self.image_path :Path = image_path
        self.background_color = background_color

    def _render(self):
        img = py.image.load(self.image_path).convert()
        return img

    # def serialize(self):
    #     # Ask Yonatan
    #     return {'x': self.x, 'y': self.y, 'width': self.width, 'height': self.height, 'image_path': self.image_path}
    #
    # def deserialize(file):
    #     # Ask if i need here to create the object or not
    #     x = file['x']
    #     y = file['y']
    #     width = file['width']
    #     height = file['height']
    #     image_path = file['image_path']
    #
    #     return DrawableImage(x, y, width, height, image_path)
    #     # creating a new object
