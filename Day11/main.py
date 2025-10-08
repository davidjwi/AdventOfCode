from dataclasses import dataclass
from functools import cache


@dataclass(frozen=True)
class Stone:
    val: int
    blinks: int


@cache
def process_num(val: int) -> list:
    if val != 0:
        str_val = str(val)
        len_val = len(str_val)
        if len_val % 2 == 0:
            # floor divide
            midIdx = len_val//2
            left, right = str_val[:midIdx], str_val[midIdx:]
            left, right = int(left), int(right)
            return [left, right]
        else:
            return [val * 2024]
    else:
        return [1]


@cache
def process_stone(stone: Stone) -> int:
    val, blinks = stone.val, stone.blinks

    if blinks == 0:
        return 1

    new_nums = process_num(val)
    if len(new_nums) == 2:
        num1 = Stone(new_nums[0], blinks - 1)
        num2 = Stone(new_nums[1], blinks - 1)
        return process_stone(num1) + process_stone(num2)
    elif len(new_nums) == 1:
        num = Stone(new_nums[0], blinks - 1)
        return process_stone(num)


def main() -> None:
    blinks = 75

    filepath = 'input.txt'
#    filepath = 'example.txt'

    with open(filepath, 'r') as file:
        data = [Stone(int(x), blinks)
                for x in file.readline().strip().split(' ')]

    # generator expression inside sum
    result = sum(process_stone(stone) for stone in data)

    print(result)
    return None


if __name__ == '__main__':
    main()
