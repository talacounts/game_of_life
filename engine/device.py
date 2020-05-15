from typing import Optional
from engine.item import Item
from pygame.math import Vector2 as Vector

class Device(Item):
    def __init__(self, width: int, height: int, image_path, cost: int, _action: bool, on_off :bool, name :str, active_image_path, background_color, x: int, y: int, is_drawing: bool ):
        print(x,y)
        super(Device, self).__init__( width, height, image_path, cost, name, background_color, x, y, is_drawing)
        self.powered: bool = on_off
        self.name = name
        self.action: Optional[Action] = _action
        self.active_image_path = active_image_path
        self.non_active_image_path = image_path

    def activating(self,action: bool):
        print('activating')
        if action == True:
            self.powerd = True
            self.image_path = self.active_image_path
            print(self.image_path)
        else:
            self.powerd = False
            self.image_path = self.non_active_image_path

        self.render()
        print('rendered')




# {MatrialName{'id': id,'pos': pos}}
