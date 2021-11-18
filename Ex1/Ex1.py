import sys

from elevator import elevator
from building import building
from call import call
import json
import csv
import math as m

# Function of Reading a json file of a building:
def from_json(build_file):
        try:
            with open(build_file, "r") as fp:
                di = json.load(fp)
                b = building(di["_minFloor"], di["_maxFloor"], di["_elevators"])
                return b
        except IOError as er:
            print(er)

# Function of reading a csv file of calls:
def csv_to_calls(calls_file):
        calls = []
        with open(calls_file) as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                c = call(_str = row[0], _time=row[1], _src=int(row[2]), _dest=int(row[3]), _status = row[4], _elev=int(row[5]))
                calls.append(c)
        return calls

# Definition of the building:
build = from_json(sys.argv[1])

# An array that accepts the floors where each elevator stops:
elev_stops = []
for i in range(build.elev_num):
    elev_stops.append([])

# A function that calculates the time it will take for an elevator to get
# from the floor it is currently on to the call source floor:
def time(build, e ,curr, src):
    elev = build._elevators[e]
    speed = elev["_speed"]
    stops = len(elev_stops[e])
    return abs(curr-src)/speed + stops * (elev["_closeTime"] + elev["_openTime"] + elev["_startTime"] + elev["_stopTime"])

# An algorithm that returns an output file with the fastest embedding of an elevator per call:
def algo(build_file, calls_file):
    calls = csv_to_calls(calls_file)
    build = from_json(build_file)
    out = calls.copy()
    for c in range(len(calls)):
        if (build.elev_num==1): # if there is one elevator in the building
            out[c]._elev = 0
        else:
            ans = 0
            for e in range(build.elev_num):
                if (calls[c]._dest > calls[c]._src):  # up call
                    if (calls[c]._src >= build.arr[e]):
                        if (time(build, e , build.arr[e], calls[c]._src) < time(build, ans, build.arr[ans], calls[c]._src)):
                            ans = e
                    else:
                        ans = (c) % build.elev_num
                else:                                # down call
                    if (calls[c]._src <= build.arr[e]):
                        if (time(build, e , build.arr[e], calls[c]._src) < time(build, ans, build.arr[ans], calls[c]._src)):
                            ans = e
                    else:
                        ans = (c*e) % build.elev_num
                # Add the source and destination floor of the call to the selected elevator stops:
                elev_stops[ans].append(calls[c]._src)
                elev_stops[ans].append(calls[c]._dest)
                # Defines the current location of the elevator as the destination floor of the call:
                build.arr[ans] = calls[c]._dest
                # Add the fast elevator to the output file:
                out[c]._elev = ans
    return out

# Creates an output file of an inlay for elevators by building and a calls file:
out = algo(sys.argv[1],sys.argv[2])
new_out = []
for call in out:
    new_out.append(call.__dict__.values())
# Create a csv file of the calls:
with open('out.csv', 'w', newline="") as file:
    write = csv.writer(file)
    write.writerows(new_out)