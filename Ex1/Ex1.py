import sys

from elevator import elevator
from building import building
from call import call
import json

def from_json(build_file):
        try:
            with open(build_file, "r") as fp:
                di = json.load(fp)
                b = building(di["_minFloor"], di["_maxFloor"], di["_elevators"])
                return b
        except IOError as er:
            print(er)

def from_json_elev(build_file):
        try:
            with open(build_file, "r") as fp:
                elev = []
                di = json.load(fp)
                di_elev = di["_elevators"]
                for i in di_elev:
                    e = elevator( di_elev["_id"], di_elev["_speed"], di_elev["_minFloor"], di_elev["_maxFloor"], di_elev["_closeTime"], di_elev["_openTime"], di_elev["_startTime"], di_elev["_stopTime"], 0, 0)
                    elev.append(e)
                return elev
        except IOError as er:
            print(er)

if __name__ == '__main__':
    # b1 = from_json(sys.argv[1])
    # print(b1)
