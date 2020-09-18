import itertools
x = 0
y = set()
file1 = open('day1_inputs.txt', 'r')
for line in itertools.cycle(file1.readlines()):
    x+= int(line)
    if x in y:
        print(x)
        break
    y.add(x)

file1.close()