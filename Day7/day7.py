
def main():
    FILEPATH = 'day7_input.txt'
    clean_input = []
    with open(FILEPATH, 'r') as file:
        for line in file:
            line = line.strip().split(':')
            test_case = int(line[0])
            test_data = list(map(int, line[1].strip().split(' ')))
            clean_input.append([test_case, test_data])
    #print(clean_input)

    operation_slot_combinations = {}
    sum = 0
    for row in clean_input:
        number_of_slots = len(row[1])-1
        answer = row[0]
        numbers_list = row[1]
        try:
            opertations_list = operation_slot_combinations[number_of_slots]
            if test_list(answer, numbers_list, opertations_list):
                sum += answer
        except KeyError:
            seed_list =  [ ['+' for i in  range(0, number_of_slots)] ]
            new_operations_list = create_new_lists(seed_list)
            operation_slot_combinations[number_of_slots] = new_operations_list
            if test_list(answer, numbers_list, new_operations_list):
                sum += answer
#    print(operation_slot_combinations)
    print(sum)
    return sum

def create_new_lists(seed_lists_within_list):
    for seed_list in seed_lists_within_list:
        for i in range(0, len(seed_list)):
            new_seed_list = seed_list.copy()
            if new_seed_list[i] == '+':
                new_seed_list[i] = '*'
            elif new_seed_list[i] == '*':
                new_seed_list[i] = '+'
            else:
                break
            if new_seed_list not in seed_lists_within_list:
                seed_lists_within_list.append(new_seed_list)
    return seed_lists_within_list
    
def test_list(answer, numbers_list, operations_list):
    for x in operations_list:
        clean_list = []
        for i in range(0, len(numbers_list)):
            clean_list.append(numbers_list[i])
            if i < len(x):
                clean_list.append(x[i])
        result = clean_list[0]                        
        for i in range(0, len(clean_list)):           
            if clean_list[i] == '+':
                result += clean_list[i+1]
            elif clean_list[i] == '*':
                result *= clean_list[i+1]
        if result == answer:
            return True
    return False

if __name__ == "__main__":
    main()