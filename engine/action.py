from engine.device import Device
class Action:
    def __init__(self, valid: bool, list_devices: Device, power_on: bool):
        self.valid: bool = valid
        self.list_devices: str = list_devices
        self.power_on: bool = power_on
