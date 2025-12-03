

def main(starting_num):
    answer = 0
    dial_num = starting_num
    with open('input', 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        for line in lines:
            side = line[:1]
            line = line[1:]
            last_2 = line[-2:]
            before_last_2 = line[:-2]
            num = int(last_2)
#            print(f'side {side} line: {line} num: {num} before_last_2: {before_last_2}')
            
            if len(before_last_2) > 0:
                answer += int(before_last_2)

            start_num = dial_num
            if side == 'L':
                dial_num -= num
                if dial_num == 0:
                    answer += 1
#                    print('Dial moved LEFT and on 0. Adding 1')
                elif dial_num < 0:
                    dial_num = 100 + dial_num
                    if start_num != 0:
                        answer += 1
#                        print('Dial moved LEFT and passed 0. Adding 1')
#                print(f'Dial Num is {dial_num}')
            else:
                dial_num += num
                if dial_num == 0:
                    answer += 1
#                    print('Dial moved RIGHR and on 0. Adding 1')
                elif dial_num > 99:
                    dial_num = dial_num - 100
                    if start_num != 100:
                        answer += 1
#                        print('Dial moved RIGHT and passed 0. Adding 1')
#                print(f'Dial Num is {dial_num}')
    
    return answer

if __name__ == "__main__":
    print(main(50))