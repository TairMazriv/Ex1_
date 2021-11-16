class call:

    def __init__(self, _time, _src, _dest, _elev):
        self._time = _time
        self._src = _src
        self._dest = _dest
        self._elev = _elev

    def __str__(self):
        return f"_time:{self._time} _src:{self._src} _dest:{self._dest} _elev:{self._elev}"

    def __repr__(self):
        return f"_time:{self._time} _src:{self._src} _dest:{self._dest} _elev:{self._elev}"

    def get_time(self):
        return self._time

    def get_src(self):
        return self._src

    def get_dest(self):
        return self._dest

    def get_elev(self):
        return self._elev