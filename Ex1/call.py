class call:

    def __init__(self, _str, _time, _src, _dest, _status, _elev):
        self._str = _str
        self._time = _time
        self._src = _src
        self._dest = _dest
        self._status = _status
        self._elev = _elev

    def __str__(self):
        return f"_time:{self._time} _src:{self._src} _dest:{self._dest} _elev:{self._elev}"

    def __repr__(self):
        return f"_time:{self._time} _src:{self._src} _dest:{self._dest} _elev:{self._elev}"