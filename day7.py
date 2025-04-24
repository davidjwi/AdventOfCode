import math
import copy

FILEPATH = 'day7_sample_input.txt'
clean_input = []
with open(FILEPATH, 'r') as file:
    for line in file:
        line = line.strip().split(':')
        test_case = int(line[0])
        test_data = list(map(int, line[1].strip().split(' ')))
        clean_input.append([test_case, test_data])

print(clean_input)


def left_to_right(num1, num2, symbol):
    if symbol == '+':
        return num1 + num2
    elif symbol == '*':
        return num1 * num2
    else:
        return None

operators =  ['*', '+']

for test_line in clean_input:
    data = test_line[1]
    # -1 because there is 1 less in between spaces then the length
    operator_slots = len(data)-1
    total_combinations = math.factorial(operator_slots)
    
    print(total_combinations)


def create_start_list(total_slots):
    start_list = []
    for i in range(0, total_slots):
        start_list.append('+')
    print(start_list)
    return start_list 


def create_lists(op_lists, total_combinations):
    work_list = op_lists.copy()
    print(type(op_lists))
    for operator_list in op_lists:
        for i in range(0, total_combinations):
            if type(operator_list) is not list:
                return
            work_list = operator_list.copy()
            work_list[i] = '*'
            print(work_list)
            if work_list not in list_of_operator_combinations:
                list_of_operator_combinations.append(work_list)
            work_list = operator_list.copy()
    create_lists(work_list, total_combinations)


list_of_operator_combinations = []
test = create_start_list(3)
list_of_operator_combinations.append(test)
create_lists(list_of_operator_combinations, 3)

print('Unique combinations\n{}'.format(list_of_operator_combinations))

#print(clean_input)
#def test_row(row):
#    list_of_operator_combinations = []
#    test_case_answer = row[0]
#    numbers = row[1]
#    operator_slots = len(numbers)-1
#    create_lists(create_start_list(operator_slots), operator_slots)

    



