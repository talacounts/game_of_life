from .textbox import Textbox
from engine.device import Device
from engine.action import Action
from typing import List
from .clickable import BLUE, RED
from numpy.random import randn as random

BACKSPACE: int = 8
ENTER: int = 13
MONEY: int = 0

class GameTextbox(Textbox):
    def __init__(self, x: int, y: int, width: int, height: int, title: str):
        super(GameTextbox, self).__init__(x, y, width, height, title)
        self.random_number = int(random() * 10)

    def on_finish(self):
        selection = int(self.text)
        if selection < self.random_number:
            self.text += "; The number is higher"
        elif selection > self.random_number:
            self.text += "; The number is lower"
        else:
            self.text += "; Good job"

        self.render()
        self.text = ""
