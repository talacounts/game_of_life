from user_interface.textbox import Textbox
from typing import Tuple, Dict, Any
from engine.player import Player
from user_interface.clickable import BLUE, RED

class Shop_textbox(Textbox):
    def __init__(self, x: int, y: int, width: int, height: int, player: Player, items_list: list):
        super(Shop_textbox, self).__init__( x, y, width, height, 'shop')
        self.player = player
        self.all_items_list = items_list

    def on_finish(self):
        items_list_names = []
        for item in self.all_items_list:
            items_list_names.append(item.name)
        if self.text in items_list_names:
            self.text_color = BLUE
            self.player.avaliabe_items.append(self.all_items_list[items_list_names.index(self.text)])
        else:
            self.text_color = RED
            print('not a valid item')
