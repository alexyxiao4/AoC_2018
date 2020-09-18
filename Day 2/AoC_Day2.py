from collections import Counter
if __name__ == "__main__":
    lines = open("./day2_inputs.txt", "r")
    array_of_strings = lines.readlines()
    num_of_twos = 0
    num_of_threes = 0
    for line in array_of_strings:
        vals = Counter(line).values()
        two_count = 0
        three_count = 0
        for value in vals:
            if(value == 2):
                two_count += 1
            if(value == 3):
                three_count += 1
        if (two_count != 0):
            num_of_twos += 1
        if (three_count != 0):
            three_count += 1
    print([num_of_twos, num_of_threes])
