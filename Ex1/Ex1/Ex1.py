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

# def from_json_elev(build_file):
#         try:
#             with open(build_file, "r") as fp:
#                 elev = []
#                 di = json.load(fp)
#                 di_elev = di["_elevators"]
#                 for i in di_elev:
#                     e = elevator(i["_id"], i["_speed"], i["_minFloor"], i["_maxFloor"], i["_closeTime"], i["_openTime"], i["_startTime"], i["_stopTime"], 0, 0, 0)
#                     elev.append(e)
#                 return elev
#         except IOError as er:
#             print(er)

def csv_to_calls(calls_file):
        calls = []
        with open(calls_file) as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                c = call( _time=row[1], _src=int(row[2]), _dest=int(row[3]),
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


if __name__ == '__main__':
    # b2 = from_json(sys.argv[1])
    print(algo(sys.argv[1],sys.argv[2]))
    # c = csv_to_calls("Calls_a.csv")
    # print(b1)
    # print(algo(sys.argv[1], "Calls_a.csv"))
    # print(time(b1[0], c[0].get_src(), c[0].get_dest()))
