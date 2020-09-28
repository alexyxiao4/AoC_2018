import re
from collections import Counter, defaultdict
from pprint import pprint


def part1_and_2(coords):
    seen = Counter()
    id_to_coords = defaultdict(list)

    for line in coords:
        id, x, y, length, height = [int(z) for z in re.findall(r'\d+', line)]
        for true_x in range(x, x + length):
            for true_y in range(y, y + height):
                seen.update([(true_x, true_y)])
                id_to_coords[id].append((true_x, true_y))

    repeat(seen)

    singletons = {coord for coord, count in seen.items() if count == 1}

    for claims in id_to_coords:
        if all(x_y in singletons for x_y in id_to_coords[claims]):
            print(claims)


def repeat(counter):
    repeats = 0
    for multiple in counter.values():
        if multiple > 1:
            repeats += 1
    print(repeats)


if __name__ == "__main__":
    with open("./Day_3_inputs.txt", "r") as f:
        coords = [line for line in f]
    part1_and_2(coords)
