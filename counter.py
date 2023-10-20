import json
import os


def get_names():
    names = set()

    for file in os.listdir('data'):
        with open(f'data/{file}', 'r') as inp:
            data = json.load(inp)

        for feature in data['features']:
            names.add(feature['properties']['name'])

    return sorted(list(names))


if __name__ == '__main__':
    with open('names.txt', 'wt') as out:
        for name in get_names():
            print(name, file=out)
