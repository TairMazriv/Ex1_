import json

class building:

    def __init__(self, _minFloor, _maxFloor, _elevators):
        self._minFloor = _minFloor
        self._maxFloor = _maxFloor
        self._elevators = _elevators.copy()
        self._arr = []
        self.elev_num = len(self._elevators)
        # Array of the current locations of each elevator (initially all locations will be defined as 0th floor):
        self.arr = []
        for i in range(0, self.elev_num):
            self.arr.append(0)

    def __str__(self):
        return f"_minFloor:{self._minFloor} _maxFloor:{self._maxFloor} _elevators:{self._elevators}"

    def __repr__(self):
        return f"_minFloor:{self._minFloor} _maxFloor:{self._maxFloor} _elevators:{self._elevators}"

