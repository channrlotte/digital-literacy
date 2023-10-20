import requests
import json

import time

from collections import deque

API_KEY = '...'


def find_names(ax, ay, bx, by):
    global last_file_name

    skip = 0

    while True:
        url = (f'https://search-maps.yandex.ru/v1/'
               f'?apikey={API_KEY}'
               f'&text=кофейня'
               f'&lang=ru_RU'
               f'&bbox={ax},{ay}~{bx},{by}'
               f'&rspn=1'
               f'&results=50'
               f'&type=biz'
               f'&skip={skip}')

        request = requests.get(url)
        time.sleep(0.1)

        if request.status_code != 200:
            if skip > 1000:
                return -1
        elif len(request.json()['features']) == 0:
            return 0
        else:
            with open(f'data/result_{last_file_name}.json', 'w') as out:
                print(json.dump(request.json(), out, indent=4))

            skip += 50
            last_file_name += 1


def main():
    to_process = deque()

    to_process.append((37.453685, 55.643120, 37.817159, 55.835115))

    while len(to_process) > 0:
        ax, ay, bx, by = to_process[0]
        to_process.popleft()

        if find_names(ax, ay, bx, by) == -1:
            mx = (ax + bx) / 2
            my = (ay + by) / 2

            to_process.append((ax, ay, mx, my))
            to_process.append((mx, ay, bx, my))
            to_process.append((ax, my, mx, by))
            to_process.append((mx, my, bx, by))


if __name__ == '__main__':
    last_file_name = 0
    main()
