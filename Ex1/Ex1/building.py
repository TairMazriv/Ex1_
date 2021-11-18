import json

class building:

    def __init__(self, _minFloor, _maxFloor, _elevators):
        self._minFloor = _minFloor
        self._maxFloor = _maxFloor
        self._elevators = _elevators
        self._arr = []
        elevators = []
        for e in _elevators:
            elevators.append(e)
        self.elevators = elevators.copy()
        self.elev_num = len(self.elevators)
        self.arr = []
        for i in range(0, self.elev_num):
            self.arr.append(0)

    def __str__(self):
        return f"_minFloor:{self._minFloor} _maxFloor:{self._maxFloor} _elevators:{self._elevators}"

    def __repr__(self):
        return f"_minFloor:{self._minFloor} _maxFloor:{self._maxFloor} _elevators:{self._elevators}"

