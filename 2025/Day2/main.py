def main():
    answer = 0 
    with open('input', 'r') as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]
    lines = [line.split(',') for line in lines]

    for line in lines:
        for num_range in line:
            if num_range != '':
                idx = num_range.find('-')
                num1 = num_range[:idx]
                num2 = num_range[idx+1:]
                for num in range(int(num1),int(num2)+1):
                    str_num = str(num)
                    if str_num in cache:
                        is_sequence = cache[str_num]
                    else:
                        is_sequence = check_sequence(str_num)
                    if is_sequence:
                        answer += int(num)
    return answer

cache = {}
def check_sequence(num: str):
    if num in cache:
        return cache[num]
    midIdx  = len(num)//2
    num1 = num[:midIdx]
    num2 = num[midIdx:] 
    if num1 == num2:
        cache[num] = True
        return True
    else:
        cache[num] = False
        return False

        

if __name__ == '__main__':
    print(main())