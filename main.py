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
from main_functions import *
import os


py.init()
print('what is your name')
player = Player(0, str(input()))
print(player.name)
# Path(base_path) / 'textures' / 'brick.png'
devices_list = []
E_KEY = 101
ERASE_KEY  = E_KEY
F = 102
base_path = os.getcwd()
background_color = (0,0,0)
this_item = ''
items_list= []
TAB = 9
fridge_path = os.path.dirname(os.path.realpath(__file__)) + '/textures' + '/fridge.jpeg'
print(fridge_path)
door_path = os.path.dirname(os.path.realpath(__file__)) + '/textures' + '/door.png'
active_fridge_path = os.path.dirname(os.path.realpath(__file__)) + '/textures' + '/open_fridge.jpeg'



devices = {
    'fridge': Device(50, 50, fridge_path, 20, True, False, 'fridge', active_fridge_path, background_color, None, None, False ),
    'door': Device(50, 50, door_path, 20, True, False, 'door', door_path, background_color, None, None, False)
}

devices_list = list(devices.values())
items = {
    **devices,
}

for key in devices:
    devices_list.append(devices[key])

BACKGROUND_COLOR = (54, 54, 54)



window = create_window(1350, 800, "game_of_life")




power_textboxes = [*create_power_textboxes(100,devices['fridge'], devices_list)]

show_money_textbox = creat_money_textbox(100, player)

game_textbox = create_game_textbox(550, show_money_textbox, player)

clickables = [
    *power_textboxes,
    game_textbox,
    show_money_textbox
]
drawables = [*clickables]
avaliabe_devices = []


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
                if event.key == ERASE_KEY:
                    this_item.is_drawing = False
                    this_item.draw(window)
                    py.display.update()

            if event.type  == py.MOUSEBUTTONDOWN:
                this_item.is_drawing = True
                mouse_pos = py.mouse.get_pos()
                this_item.buy_instance(player, mouse_pos, window)
                py.display.update()
                drawables.append(this_item)
                avaliabe_devices.append(this_item)

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
                    print('turning all devices')
                    for power_textbox in power_textboxes:
                        new_drawables = power_textbox.turning_on_all_devices(avaliabe_devices)
                        for device in new_drawables:
                            drawables.append(device)
                            device.draw(window)

py.quit()
