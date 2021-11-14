import building as b

class elevator:
    def __init__(self, i) -> None:
        self._id = b.get_elevators[i]["_id"]
        self._speed = b.get_elevators[i]["_speed"]
        self._minFloor = b.get_elevators[i]["_minFloor"]
        self._maxFloor = b.get_elevators[i]["_maxFloor"]
        self._closeTime = b.get_elevators[i]["_closeTime"]
        self._openTime = b.get_elevators[i]["_openTime"]
        self._startTime = b.get_elevators[i]["_startTime"]
        self._stopTime = b.get_elevators[i]["_stopTime"]
        self._state = 0;
        self._pos = 0;

    def getMinFloor(self):
        return self._minFloor

    def getMaxFloor(self):
        return self._maxFloor

    def getTimeForOpen(self):
        return self._openTime

    def getTimeForClose(self):
        return self._closeTime

    def getState(self): # up/down/level/error
        return self._state

    def getPos(self):
        return self._pos

    def goTo(self, floor):
        if (floor<self.getPos())
            self._state = -1
        if (floor > self.getPos())
            self._state = 1
        if (floor == self.getPos())
            self._state = 0
        else
            self._state = -2

    def getSpeed(self):
        return self._speed

    def getStartTime(self):
        return self._startTime

    def getStopTime(self):
        return self._stopTime

    def get_id(self):
        return self._id
