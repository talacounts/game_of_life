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
import scipy
import os
from user_interface.show_money_textbox import Money_Textbox

from scipy.spatial.distance import cdist

POINTS = []
def create_power_textboxes(y: int, device: Device, devices_list: list):
    return [PowerTextbox(40, y, 200, 50, True, device, devices_list),
            PowerTextbox(40, y + 100, 200, 50, False, device, devices_list)]

def creat_money_textbox(y: int, player: Player):
    return Money_Textbox(260, y, 200, 50, player)


def create_clickables(y):
    return [Clickable(40, y, 200, 50),
            Clickable(40, y + 200, 200,50)]

def create_textboxes(titles, y):
    return [Textbox(40, y, 200, 50, titles[0])]

def create_game_textbox(y, textbox, player: Player):
    return GameTextbox(40, y ,200, 50,"random number game", textbox, player)

def create_window(height, width, caption):
    window = py.display.set_mode((height, width))
    py.display.set_caption(caption)
    return window


def creating_points(width: int, height: int, height_mulitple: int):
    def calculating_one_row(height: int):
        for i in range(3):
            POINTS.append([(width / 3) * (i + 1), start_height])

    calculate_height = height / 3

    for i in range(3):
        calculating_one_row(calculate_height * (i + 1))
    return points

def find_closest(place: tuple):
    distances = POINTS - place
    return points[cdist([place], points).argmin()]
