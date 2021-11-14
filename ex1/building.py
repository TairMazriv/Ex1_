import json

class building:
    def get_minFloor(self):
        return self._minFloor

    def get_maxFloor(self):
        return self._maxFloor

    def get_elevators(self):
        return self._elevators

    def elev_num(self):
        return (self._elevators).len

    def from_json(self,file_name):
        with open(file_name,"r") as fp:
            di=json.load(fp)
            self._minFloor=di["_minFloor"]
            self._maxFloor=di["_maxFloor"]
            self._elevators=di["_elevators"]