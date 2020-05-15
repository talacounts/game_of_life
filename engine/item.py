from user_interface.drawable_image import DrawableImage
from pygame import Surface
from engine.player import Player
from typing import Tuple, Dict, Any
from pygame.math import Vector2 as Vector
from engine.fs.serialization import Serializable

class Item(Serializable, DrawableImage):
    def __init__(self, width: int, height: int, image_path: str, cost: int, name: str, background_color, x: int, y: int, is_drawing: bool):
        Serializable.__init__(self, width=width, height=height, image_path=image_path, cost=cost, name=name, background_color=background_color)
        DrawableImage.__init__(self, x, y, width, height, image_path, background_color, is_drawing)
        self.cost: int = cost
        self.name = name
        self.width = width
        self.height = height
        self.image_path = image_path
        self.background_color = background_color

    def buy_instance(self, player, mouse_pos: Vector, window) -> DrawableImage:
        if self in player.avaliabe_items:
            self.updating_pos(mouse_pos)
        else:
            print('you dont have this item')

    def updating_pos(self, mouse_pos: Vector):
        self.x,self.y = mouse_pos
        self.pos = self.x, self.y




    #def serialize(self):
        #return {'x': self.x, 'y': self.y, 'width': self.width, 'height': self.height, 'image_path': self.image_path,'cost': self.cost}

    #def deserialize(file):
        #x = file['x']
        #y = file['y']
        #width = file['width']
        #height = file['height']
        #image_path == file['image_path']
        #cost = file['cost']
        # creating a new object
        #return Item(x, y, width, height, image_path, cost)
