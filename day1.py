#format sample
#3   4
#4   3
#2   5
#1   3
#3   9
#3   3


list_1 = []
list_2 = []
list_3 = []

with open("day1_input.txt", "r") as input_file:
    for line in input_file:
        formatted_line = line.strip().split("   ")
        list_1.append(int(formatted_line[0]))
        list_2.append(int(formatted_line[1]))


list_1.sort()
list_2.sort()

for x,y in zip(list_1, list_2):
    dist = abs(x - y)
    list_3.append(dist)

total_dist = sum(list_3)

print(total_dist)