from collections import Counter
from collections import defaultdict


def part1(string_arr):
    num_of_twos = 0
    num_of_threes = 0
    for line in string_arr:
        vals = Counter(line).values()
        two_count = 0
        three_count = 0
        for value in vals:
            if value == 2:
                two_count += 1
            if value == 3:
                three_count += 1
        if two_count != 0:
            num_of_twos += 1
        if three_count != 0:
            num_of_threes += 1
        # if 2 in vals
    print(num_of_twos * num_of_threes)


def part2(string_arr):
    previous = defaultdict(list)
    # dict of [index, letter] mapped to words
    length = len(string_arr[0]) - 1
    solution = ""
    # go through words in the param
    for word in string_arr:
        similar = Counter()
        # go through every letter in the word
        for idx, letter in enumerate(word, start=1):
            # go to dict of tuples of (idx, letter) => list of words
            value_of_key = previous[(idx, letter)]
            if len(value_of_key) != 0:
                for close_word in value_of_key:
                    similar[close_word] += 1
                    if similar[close_word] == length:
                        found_word = close_word
                        current_word = word
                        i = 0
                        while i < (length + 1):
                            if found_word[i] == current_word[i]:
                                solution += (found_word[i])
                            i+=1
            previous[(idx, letter)].append(word)
    print(solution)


if __name__ == "__main__":
    with open("./day2_inputs.txt", "r") as f:
        words = [line for line in f]
    part1(words)
    part2(words)
