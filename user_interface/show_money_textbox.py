from user_interface.textbox import Textbox
from engine.player import Player
from typing import Tuple, Dict, Any


class Money_Textbox(Textbox):
    def __init__(self, x: int, y: int, width: int, height: int, player: Player):
        super(Money_Textbox, self).__init__(x, y, width, height, player.name)
        self.player = player
        self.title = self.player.name
        self.text = str(player.money)

    def input_text(self, key):
        pass

    def update_text(self):
        self.text = str(self.player.money)
        self.render()
