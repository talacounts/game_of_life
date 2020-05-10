from user_interface.drawable_image import DrawableImage
from pygame import Surface
from engine.player import Player
from typing import Tuple, Dict, Any
from pygame.math import Vector2 as Vector
from engine.fs.serialization import Serializable

class Item(Serializable):
    def __init__(self, width: int, height: int, image_path: str, cost: int, name: str, background_color ):
        super(Item, self).__init__(width=width, height=height, image_path=image_path, cost=cost, name=name, background_color=background_color)
        self.cost: int = cost
        self.name = name
        self.width = width
        self.height = height
        self.image_path = image_path
        self.background_color = background_color
        self.pos = (0,0)

    def buy_instance(self, player, mouse_pos: Vector, window) -> DrawableImage:
        self.pos = mouse_pos
        print("buying")
        player.money -= self.cost
        return self.rendering(mouse_pos)

    def rendering(self, mouse_pos: Vector):
        return DrawableImage(self.pos[0], self.pos[1], self.width, self.height, self.image_path, self.background_color)

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
