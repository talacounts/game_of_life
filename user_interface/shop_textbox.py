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
        item = next((item for item in self.all_items_list if item.name == self.text), None)
        if item:
            if self.player.money < item.cost:
                self.text_color = RED
                self.text += "; Not enough money! Lets do some mini games!"
            else:
                self.player.money -= item.cost
                self.text_color = BLUE
                self.text += "; Bought item!!! now we can build!!"
                self.player.avaliabe_items.append(item)
        else:
            self.text_color = RED
            print('not a valid item')

        self.render()
