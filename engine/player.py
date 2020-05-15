from engine.fs.serialization import Serializable

class Player(Serializable):
    def __init__(self, money: int, name: str, avaliabe_devices: list):
        super(Player,self).__init__(money=money)
        self.money :int = money
        self.name = name
        self.avaliabe_items  = avaliabe_devices
