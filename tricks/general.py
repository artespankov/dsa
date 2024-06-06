from typing import Dict, List


def sort_by_value(d: Dict):
    return sorted(d.items(), key=lambda x: x[1])


def checker():
    x, y, z = 0, 1, 0
    if x == 1 or y == 1 or z == 1:
        print('Passed #1.1')
    if 1 in (x, y, z):
        print('Passed #1.2')
    if x or y or z:
        print('Passed #2.1')
    if any((x, y, z)):
        print('Passed #2.2')


if __name__ == '__main__':
    ud = {'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1, 'f': 0}
    print(sort_by_value(ud))
    checker()
    d1 = {"a": 12, "b": 17}
    d2 = {"a": 172, "c": 0}
    d3 = {**d1, **d2}
    print(d3)


