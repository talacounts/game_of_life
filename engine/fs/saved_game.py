from .serialization import Serializable
from typing import Dict, Any, List
from .serialization import serialize_to_file,deserialize_from_file

# TODO: Tal, move to folder (engine)
class SavedGame(Serializable):
    def __init__(self, devices :List, file_path :Path):
        self.devices :List = devices
        self.dict_devices :List = {}
        self.deserialize_objects :List = []
        # list of dictionaries

    def serialize_all_game(self) -> Dict[str, Any]:
        for device in self.devices:
            self.dict_devices.append(device.serialize(self))
        writing_jsonfile(self.dict_devices, self.path :Path)
        self.deserialize_objects = []

    def deserialize_all_game(serialized: Dict[str, Any]):
        for device in self.devices:
            self.deserialize_objects.append(device.deserialize(self))

def writing_jsonfile(dictionary :Dict, path :Path):
    with open(path, 'wb') as f:
        f.write(json.dump(dictionary))
