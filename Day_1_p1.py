file1 = open('day1_inputs.txt', 'r')
x = 0
for i in file1.readlines():
    x+= int(i)
print(x)
file1.close()

#better version:
#x = 0
#with open('day1_inputs.txt', 'r') as f:
#   for line in f:
#       x += int(line)
#print(x)