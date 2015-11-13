import json


def parseFile(filename):
    if filename is None or filename == "":
        raise Exception("Filename has to have a value")
    json_data = open(filename, "r")
    data = json.load(json_data)
    if data is None:
        raise Exception("Could not parse " + filename)
    return data
