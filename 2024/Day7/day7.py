
def solve(answer, numbers):
    if len(numbers) == 1:
        if numbers[0] == answer:
            return True
        else:
            return False
    else:
        result1 = numbers[0] + numbers[1]
        result2 = numbers[0] * numbers[1]
        result3 = int(str(numbers[0]) + str(numbers[1]))
        newList = numbers[2:]
        new_numbers1 = [result1] + newList
        new_numbers2 = [result2] + newList
        new_numbers3 = [result3] + newList

        if solve(answer, new_numbers1):
            return True
        elif solve(answer, new_numbers2):
            return True
        elif solve(answer, new_numbers3):
            return True


def main():
    answer = 0
    FILEPATH = 'day7_input.txt'
    clean_input = []
    with open(FILEPATH, 'r') as file:
        for line in file:
            line = line.strip().split(':')
            test_case = int(line[0])
            test_data = list(map(int, line[1].strip().split(' ')))
            clean_input.append([test_case, test_data])
    # print(clean_input)

    for row in clean_input:
        if solve(row[0], row[1]):
            answer += row[0]
    print(answer)


main()
