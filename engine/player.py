from engine.fs.serialization import Serializable

class Player(Serializable):
    def __init__(self, money: int):
        super(Player,self).__init__(money=money)
        self.money :int = money
