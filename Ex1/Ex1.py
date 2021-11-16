import sys

from elevator import elevator
from building import building
from call import call
import json
import csv

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

#if __name__ == '__main__':
    # b1 = from_json(sys.argv[1])
    # print(b1)
def csv_to_calls(calls_file):
  #  if __name__ == '__main__':
        calls = []
        with open(calls_file) as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                c = call( _time=row[1], _src=int(row[2]), _dest=int(row[3]),
                                _elev=int(row[5]))
                calls.append(c)
        print (calls)