import sys

from elevator import elevator
from building import building
from call import call
import json
import csv
import math as m

def from_json(build_file):
        try:
            with open(build_file, "r") as fp:
                di = json.load(fp)
                b = building(di["_minFloor"], di["_maxFloor"], di["_elevators"])
                return b
        except IOError as er:
            print(er)

def csv_to_calls(calls_file):
        calls = []
        with open(calls_file) as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                c = call(_str = row[0], _time=row[1], _src=int(row[2]), _dest=int(row[3]), _status = row[4],
                                _elev=int(row[5]))
                calls.append(c)
        return calls

build = from_json(sys.argv[1])

elev_stops = []
for i in range(build.elev_num):
    elev_stops.append([])

def time(build, e ,curr, src):
    elev = build._elevators[e]
    speed = elev["_speed"]
    stops = len(elev_stops[e])
    return abs(curr-src)/speed + stops * (elev["_closeTime"] + elev["_openTime"] + elev["_startTime"] + elev["_stopTime"])

def algo(build_file, calls_file):
    calls = csv_to_calls(calls_file)
    build = from_json(build_file)
    out = calls
    for c in range(len(calls)):
        if (build.elev_num==1):
            out[c]._elev = 0
        else:
            ans = 0
            for e in range(build.elev_num):
                if (calls[c]._dest > calls[c]._src):
                    if (calls[c]._src >= build.arr[e]):
                        if (time(build, e , build.arr[e], calls[c]._src) < time(build, ans, build.arr[ans], calls[c]._src)):
                            ans = e
                    else:
                        ans = (c) % build.elev_num
                else:
                    if (calls[c]._src <= build.arr[e]):
                        if (time(build, e , build.arr[e], calls[c]._src) < time(build, ans, build.arr[ans], calls[c]._src)):
                            ans = e
                    else:
                        ans = (c*e) % build.elev_num
                elev_stops[ans].append(calls[c]._src)
                elev_stops[ans].append(calls[c]._dest)
                build.arr[ans] = calls[c]._dest
                out[c]._elev = ans
    return out

out = algo(sys.argv[1],sys.argv[2])
new_out = []
for call in out:
    new_out.append(call.__dict__.values())
with open('out.csv', 'w', newline="") as file:
    write = csv.writer(file)
    write.writerows(new_out)