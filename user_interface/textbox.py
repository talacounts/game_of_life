import pygame
import string
from pygame.math import Vector2 as Vector
from pygame import Surface
from pygame.font import SysFont as SystemFont
from typing import Tuple
from .clickable import Clickable, BLUE, RED, LIGHT_GRAY, WHITE

BACKSPACE: int = 8
ENTER: int = 13

class Textbox(Clickable):
    def __init__(self, x, y, width, height, title):
        super(Textbox, self).__init__(x, y, width, height)
        self.background_color: Tuple[int] = LIGHT_GRAY
        self.font: SystemFont = SystemFont("Calibiri", 18)
        self.title: str = title
        self.title_color: Tuple[int] = (0,0,0)
        self.text: str = ""
        self.text_color: Tuple[int] = (56, 8, 246)

    def input_text(self, key_code: int):
        key: chr = chr(key_code)
        if key_code == ENTER:
            # Handle enter, input ended
            self.on_unfocus()
            self.on_finish()

        elif key_code == BACKSPACE and len(self.text) > 0:
            # Handle backspace, delete last character
            self.text = self.text[:-1]
            self.render()
        if key in string.printable:
            # Handle regular character, append to text
            self.text += key
            self.render()

    def _render(self):
        image: Surface = Surface((self.width, self.height))
        image.fill(self.background_color)

        title_render = self.font.render(self.title, False, self.title_color)
        text_render = self.font.render(self.text, False, self.text_color)
        image.blit(title_render, (10, 20) if self.focused else (0, 0))
        image.blit(text_render, (10, 30))

        return image

    def on_focus(self):
        super(Textbox, self).on_focus()
        self.background_color = WHITE
        self.render()

    def on_unfocus(self):
        super(Textbox, self).on_unfocus()
        self.background_color = LIGHT_GRAY
        self.render()

    def on_finish(self):
        pass
