from .textbox import Textbox
from engine.device import Device
from engine.action import Action
from typing import List
from .clickable import BLUE, RED
from numpy.random import randn as random
from engine.player import Player
from user_interface.show_money_textbox import Money_Textbox
BACKSPACE: int = 8
ENTER: int = 13
MONEY: int = 0

class GameTextbox(Textbox):
    def __init__(self, x: int, y: int, width: int, height: int, title: str, Money_Textbox: Money_Textbox, player: Player):
        super(GameTextbox, self).__init__(x, y, width, height, title)
        self.random_number = int(random() * 10)
        self.tries  = 0
        self.Money_Textbox = Money_Textbox
        self.player = player
    def on_finish(self):
        print(self.random_number)
        if self.tries <= 3:
            selection = int(self.text)
            if selection < self.random_number:
                self.text += "; The number is higher"
            elif selection > self.random_number:
                self.text += "; The number is lower"
            else:
                self.text += "; Good job"
                self.player.money += 100
                self.tries = 5
        else:
            self.text = 'game over'
            self.random_number = int(random() * 10)
            self.Money_Textbox.update_text()
            self.tries = 0
        self.render()
        # self.tries += 1
