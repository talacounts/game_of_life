from user_interface.textbox import Textbox
from engine.player import Player
from typing import Tuple, Dict, Any


class Money_Textbox(Textbox):
    def __init__(self, x: int, y: int, width: int, height: int, player: Player):
        super(Money_Textbox, self).__init__(x, y, width, height, player.name)
        self.player = player
        self.title = self.player.name

    def _render(self):
        self.text = str(self.player.money)
        return super(Money_Textbox, self)._render()

    def draw(self, window):
        self.render()
        super(Textbox, self).draw(window)

    def on_focus(self):
        pass

    def on_unfocus(self):
        pass
