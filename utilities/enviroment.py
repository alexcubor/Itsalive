import os
from pprint import pprint
import json
import sys

def get_all():
    # Get All Environments
    env = os.environ
    dict = {}
    for e in env:
        dict.update({e: env[e].split(';')})
    return dict


def write(path):
    print("Write to " + path)
    with open(path, "w") as write_file:
        json.dump(get_all(), write_file, indent=4, sort_keys=True)


if __name__ == "__main__":
    path = "C:/env.json"
    if sys.argv:
        if ".json" in sys.argv[-1]:
            path = sys.argv[-1]
    write(path)
