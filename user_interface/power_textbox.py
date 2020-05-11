from .textbox import Textbox
from engine.device import Device
from engine.action import Action
from typing import List
from .clickable import BLUE, RED


class PowerTextbox(Textbox):
    def __init__(self, x: int, y: int, width: int, height: int, power_on: bool, device: Device, possible_devices: List[Device]):
        super(PowerTextbox, self).__init__(x, y, width, height, "Turn on when: " if power_on else "Turn off when: ")
        self.devices_list = []
        self.power_on: bool = power_on
        self.device: Device = device
        self.possible_devices: List[Device] = possible_devices

    def on_finish(self):
        if ',' in self.text:
            self.devices_list = self.text.split(',')
        else:
            self.devices_list = [self.text]
        blue = False
        possibilities = ['true', 'false'] + [device.name for device in self.possible_devices]
        print(possibilities)
        print(self.text)
        print(self.devices_list)
        for i in range(len(self.devices_list)):
            if self.devices_list[i] in possibilities:
                blue = True

            else:
                blue = False
        if blue == True:
            self.text_color = BLUE
            self.action = Action(True, self.devices_list, self.power_on)
        else:
            self.text_color = RED
            self.action = Action(False, None, self.power_on)

        self.render()

    def turning_on_all_devices(self, devices_list: list):
        renderd_images = []
        devices_list_checked = []
        for device in devices_list:
            if device.name in self.devices_list:
                devices_list_checked.append(device)
        print(devices_list_checked)
        for device in devices_list_checked:
            renderd_images.append(device.activating(self.power_on))
        return renderd_images
