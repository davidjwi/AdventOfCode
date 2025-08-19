from time import perf_counter


def main() -> int:
    filepath = 'input.txt'

    with open(filepath, 'r') as file:
        input = [int(x) for x in file.readline().strip().split(' ')]
    
    number_of_blinks =  25

    for i in range(0, number_of_blinks):
        j = 0
#        tStart = perf_counter()
        while j < len(input):
            working_stone = input[j]
            if len(str(working_stone)) % 2 == 0 and working_stone != 0:
                strStone = str(working_stone)
                middleIndex = len(str(working_stone))//2
                newLeftStone = int(strStone[:middleIndex])
                newRightStone = int(strStone[middleIndex:])
                input[j] = newLeftStone
                input.insert(j+1, newRightStone)
                j += 1
            elif working_stone != 0:
                input[j] = input[j] * 2024
            else:
                input[j] = 1
            
            j += 1
#        tStop = perf_counter()
#        print(f'Blink {i}: Len: {len(input)} Elapsed Time: {tStop-tStart}')
    
    print(len(input))
    return len(input) 


if __name__ == "__main__":
    main()