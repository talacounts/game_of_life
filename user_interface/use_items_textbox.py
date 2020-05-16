from user_interface.textbox import Textbox
from engine.player import Player
from typing import Tuple, Dict, Any

class Use_Textbox(Textbox):
    def __init__(self, x: int, y: int, width: int, height: int, player: Player):
        super(Use_Textbox, self).__init__(x, y, width, height, 'choose your item number')
        self.player = player

    def on_finish(self):
        if len(self.text):
            number = int(self.text)
            if number <= len(self.player.avaliabe_items):
                self.player.this_item = self.player.avaliabe_items[number - 1]
