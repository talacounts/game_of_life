from .textbox import Textbox
from engine.device import Device
from engine.action import Action
from typing import List
from .clickable import BLUE, RED


class PowerTextbox(Textbox):
    def __init__(self, x: int, y: int, width: int, height: int, power_on: bool, device: Device, possible_devices: List[Device], split: str):

        super(PowerTextbox, self).__init__(x, y, width, height, "Turn on: " if power_on else "Turn off: ")
        self.devices_list = []
        self.power_on: bool = power_on
        self.device: Device = device
        self.possible_devices: List[Device] = possible_devices
        self.split = split

    def on_finish(self):
        if self.split in self.text:
            self.devices_list = self.text.split(self.split)
        else:
            self.devices_list = [self.text]
        print(self.devices_list)
        possibilities = ['true', 'false'] + [device.name for device in self.possible_devices]
        valid = all(device in possibilities for device in self.devices_list)

        if valid:
            self.text_color = BLUE
            self.action = Action(True, self.devices_list, self.power_on)
        else:
            self.text_color = RED
            self.action = Action(False, None, self.power_on)

        self.render()

    def turning_on_all_devices(self, devices_list: list):
        renderd_images = []
        append_drawable = []
        devices_list_checked = []
        for device in devices_list:
            if device.name in self.devices_list:
                devices_list_checked.append(device)
        for device in devices_list_checked:
            device.activating(self.power_on)
            append_drawable.append(device)
        return append_drawable
