from collections import Counter
from collections import defaultdict


# find occurences of 2x a letter and 3x a letter in list of strings
def part1(string_arr):
    num_of_twos = 0
    num_of_threes = 0
    for line in string_arr:
        vals = Counter(line).values()
        if 2 in vals:
            num_of_twos += 1
        if 3 in vals:
            num_of_threes += 1
        # if 2 in vals
    print(num_of_twos * num_of_threes)


# find 2 strings that are different by exactly 1 letter
def part2(string_arr):
    # Key:(index, letter) => value: list of strings that correspond
    previous = defaultdict(list)
    length = len(string_arr[0]) - 1

    for word in string_arr:
        shared = Counter()
        for idx, letter in enumerate(word, start=1):
            shared.update(previous[(idx, letter)])
        almost_match = similar_word(shared, length)
        if almost_match:
            same_characters(word, almost_match, length)
            return
        previous[(idx, letter)].append(word)


# return string if same chars except 1
def similar_word(counter, length):
    for key, value in counter.most_common(1):
        if value == length:
            return key


# print a string with all common chars across 2 words
def same_characters(word, close_word, length):
    i = 0
    solution = ""
    while i < (length + 1):
        if word[i] == close_word[i]:
            solution += (word[i])
        i += 1
    print(solution)


if __name__ == "__main__":
    with open("./day2_inputs.txt", "r") as f:
        words = [line for line in f]
    part1(words)
    part2(words)
