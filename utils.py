import json


def writeDataToFile(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def readDataFromFile(filepath):
    with open(filepath) as data_file:
        return json.load(data_file)