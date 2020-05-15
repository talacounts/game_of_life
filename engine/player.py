from engine.fs.serialization import Serializable

class Player(Serializable):
    def __init__(self, money: int, name: str):
        super(Player,self).__init__(money=money)
        self.money :int = money
        self.name = name
        # self.avaliabe_devices  = avaliabe_devices
