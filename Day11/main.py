class Stone:
    def __init__(self, val: int, blinks: int):
        self.val = val
        self.blinks = blinks


num_cache = {}


def process_num(val: int, num_cache: dict) -> list:
    if val not in num_cache:
        if val != 0:
            str_val = str(val)
            len_val = len(str_val)
            if len_val % 2 == 0:
                # floor divide
                midIdx = len_val//2
                left, right = str_val[:midIdx], str_val[midIdx:]
                left, right = int(left), int(right)
                num_cache[val] = [left, right]
            else:
                num_cache[val] = [val * 2024]
        else:
            num_cache[val] = [1]

    return num_cache[val]


stone_cache = {}


def process_stone(stone: Stone, stone_cache: dict, result: int):
    val, blinks = stone.val, stone.blinks
    key = (val, blinks)

    if blinks == 0:
        return result + 1

    if key not in stone_cache:
        new_nums = process_num(val, num_cache)
        if len(new_nums) == 2:
            num1 = Stone(new_nums[0], blinks - 1)
            num2 = Stone(new_nums[1], blinks - 1)
            stone_cache[key] = process_stone(
                num1, stone_cache, result) + process_stone(num2, stone_cache, result)
        elif len(new_nums) == 1:
            num = Stone(new_nums[0], blinks - 1)
            stone_cache[key] = process_stone(num, stone_cache, result)
    return stone_cache[key]


def main():
    blinks = 75

    filepath = 'input.txt'
#    filepath = 'example.txt'

    with open(filepath, 'r') as file:
        data = [Stone(int(x), blinks)
                for x in file.readline().strip().split(' ')]

    result = 0
    for stone in data:
        stones_at_zero_blinks = process_stone(stone, stone_cache, 0)
        result += stones_at_zero_blinks

    print(result)
    return None


if __name__ == '__main__':
    main()
