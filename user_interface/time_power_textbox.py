from user_interface.power_textbox import PowerTextbox
from typing import List
from engine.device import Device
from user_interface.textbox import Textbox

class TimePowerTextbox(PowerTextbox):
    def __init__(self, x: int, y: int, width: int, height: int, power_on: bool, device: Device, possible_devices: List[Device], split: str):
        super(TimePowerTextbox, self).__init__( x, y, width, height, power_on, device, possible_devices, split)


    def turning_on_all_devices(self, devices_list: list):
        for device in devices_list:
            if device.name in self.devices_list:
                devices_list_checked.append(device)
        return [int(self.devices_list[0]), int(self.devices_list[1])]
