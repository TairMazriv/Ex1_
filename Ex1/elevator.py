import building as b

class elevator:
    def __init__(self, _id, _speed, _minFloor, _maxFloor, _closeTime, _openTime, _startTime, _stopTime, _state, _pos, _time) -> None:
        self._id = _id
        self._speed = _speed
        self._minFloor = _minFloor
        self._maxFloor = _maxFloor
        self._closeTime = _closeTime
        self._openTime = _openTime
        self._startTime = _startTime
        self._stopTime = _stopTime
        self._state = _state
        self._pos = _pos
        self._time = _time

    def __str__(self):
        return f"_id:{self._id} _speed:{self._speed} _minFloor:{self._minFloor} _maxFloor:{self._maxFloor} _closeTime:{self._closeTime} _openTime:{self._openTime} _startTime:{self._startTime} _stopTime:{self._stopTime} _state:{self._state} _pos:{self._pos}"

    def __repr__(self):
        return f"_id:{self._id} _speed:{self._speed} _minFloor:{self._minFloor} _maxFloor:{self._maxFloor} _closeTime:{self._closeTime} _openTime:{self._openTime} _startTime:{self._startTime} _stopTime:{self._stopTime} _state:{self._state} _pos:{self._pos}"

