# changed
import pygame as py
from user_interface.power_textbox import PowerTextbox
from engine.device import Device
from user_interface.clickable import Clickable
from user_interface.textbox import Textbox
from user_interface.game_textbox import GameTextbox
from user_interface.game_textbox import MONEY
from user_interface.drawable_image import DrawableImage
from engine.item import Item
from engine.player import Player
import numpy as np
from path import Path
from engine.player import Player
import os

py.init()
player = Player(0)
# Path(base_path) / 'textures' / 'brick.png'
devices_list = []
F = 102
base_path = os.getcwd()
background_color = (0,0,0)
this_item = ''
items_list= []
TAB = 9
fridge_path = os.path.dirname(os.path.realpath(__file__)) + '/textures' + '/fridge.png'
print(fridge_path)
door_path = os.path.dirname(os.path.realpath(__file__)) + '/textures' + '/door.png'
active_fridge_path = os.path.dirname(os.path.realpath(__file__)) + '/textures' + '/open_fridge.png'



devices = {
    'fridge': Device(50, 50, fridge_path, 20, True, False, 'fridge', active_fridge_path, background_color ),
    'door': Device(50, 50, door_path, 20, True, False, 'door', door_path, background_color)
}

devices_list = list(devices.values())
items = {
    **devices,
}

for key in devices:
    devices_list.append(devices[key])

BACKGROUND_COLOR = (54, 54, 54)

def create_window(height, width, caption):
    window = py.display.set_mode((height, width))
    py.display.set_caption(caption)
    return window

window = create_window(1350, 800, "Automation")

def create_power_textboxes(y, device):
    return [PowerTextbox(40, y, 200, 50, True, device, devices_list),
            PowerTextbox(40, y + 100, 200, 50, False, device, devices_list)]

def create_clickables(y):
    return [Clickable(40, y, 200, 50),
            Clickable(40, y + 200, 200,50)]

def create_textboxes(titles, y):
    return [Textbox(40, y, 200, 50, titles[0])]

def create_game_textbox(y):
    return GameTextbox(40, y ,200, 50,"random number game")

power_textboxes = [*create_power_textboxes(100,devices['fridge'])]
game_textbox = create_game_textbox(550)
clickables = [
    *power_textboxes,
    game_textbox
]
drawables = [*clickables]

mode  = True
building = False
coding_and_working  = True
run = True
key_able = True

for key in items:
    items_list.append(items[key])


while run:
    #print(mode)
    window.fill(BACKGROUND_COLOR)
    for drawable in drawables:
        drawable.draw(window)

    py.display.update()

    py.time.delay(100)

    for event in py.event.get():
        if mode == False:
            print('mode = building')


            # print(items_list)
            if event.type == py.KEYDOWN:
                if 48 <= event.key <= 59:
                    this_item = items_list[int(chr(event.key)) - 1]
                    print(this_item)


            if event.type  == py.MOUSEBUTTONDOWN:
                mouse_pos = py.mouse.get_pos()

                drawable_item = this_item.buy_instance(player, mouse_pos, window)
                drawable_item.draw(window)
                py.display.update()
                drawables.append(drawable_item)

        if event.type == py.KEYDOWN:
            if event.key == TAB:
                mode = not mode
        if event.type == py.QUIT:
            run = False
        if mode == coding_and_working:
            if event.type == py.MOUSEBUTTONDOWN:
                for clickable in clickables:
                    clickable.handle_click(py.mouse.get_pos())
            if event.type == py.KEYDOWN:
                for clickable in clickables:
                    if clickable.focused:
                        clickable.input_text(event.key)

            if event.type == py.KEYDOWN:
                if event.key == 271:
                    print('f')
                    for power_textbox in power_textboxes:
                        function_output = power_textbox.turning_on_all_devices(devices_list)
                        for i in range(len(function_output)):
                            drawable_item = function_output[i]
                            drawable_item.draw(window)
                            py.display.update()
                            drawables.append(drawable_item)



py.quit()
