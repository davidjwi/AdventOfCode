def create_disk(filepath: str):
    '''Return a list representing the disk from the input file'''
    with open(filepath, 'r') as file:
        line = file.readline().strip()
    disk_map = []
    for i in range(0, len(line), 2):
        #ID of the current block file by dividing the 2-step loop back into 1
        file_id_index = str(i // 2)
        num_repeats = int(line[i])
        disk_map.extend([file_id_index] * num_repeats)
        
        if i + 1 < len(line):
            #Sets the free space '.'s after the file ID
            num_free_space_dots = int(line[i+1])
            disk_map.extend(['.'] * num_free_space_dots)
    return disk_map

def get_next_freespace_size(leftPointer: int, disk_list: list):
    '''Given the left pointer index get the length of the left-direction group of freespace "." characters'''
    freeDiskspace = 0
    disk_len = len(disk_list)
    if disk_list[leftPointer] != '.':
        return freeDiskspace 
    while leftPointer < disk_len and disk_list[leftPointer] == '.':
        freeDiskspace += 1
        leftPointer += 1
    return freeDiskspace 

def check_fileblock_size(rightPointer: int, disk_list: list):
    '''Starting at the right pointer count how long a file block is and return an int'''
    currNum = disk_list[rightPointer]
    # Size starts at 1 since this is only called on numbers and not freespaces '.'
    blockSize = 1
    # Only go to the 0 index otherwise will be out of range
    while rightPointer > -1:
        if currNum == disk_list[rightPointer-1]:
            blockSize += 1
        else:
            return blockSize
        rightPointer -= 1
    return blockSize

def get_next_rightside_fileblock(rightPointer: int, disk_list: list, checkedNums: set):
    '''Starting at the pointer and moving right find the next file block and return the size'''
    # 0 is last item when moving this direction
    blockSize = None
    while rightPointer > -1:
        if disk_list[rightPointer] != '.' and disk_list[rightPointer] not in checkedNums:
            # this is a file block
            # loop back again to see how far it goes
            checkedNums.add(disk_list[rightPointer])
            blockSize = check_fileblock_size(rightPointer, disk_list)
            return blockSize
        rightPointer -= 1
    return blockSize

def swap_block_and_freespace(disk: list, left_pointer: int, right_pointer: int, fileBlockSize: int):
    '''Swap freespaces and blocks and keep count until the number of swaps is up to the length/size of the block'''
    swaps = 0
    while swaps < fileBlockSize:
        disk[left_pointer], disk[right_pointer] = disk[right_pointer], disk[left_pointer]
        left_pointer += 1
        right_pointer -= 1
        swaps += 1
    return disk

def calc_checksum(disk_list: list):
    return sum(i * int(val) for i, val in enumerate(disk_list) if val != '.')


def main():
    disk = create_disk(filepath='Day9/input.txt')

    right_pointer = len(disk) - 1
    left_pointer = 0
    checkedNums = set()

    # Move from right side to the left and find each file block, then check the left side for free space
    while right_pointer > -1:
        if disk[right_pointer] != '.' and disk[right_pointer] not in checkedNums:
            left_pointer = 0
            fileBlockSize = get_next_rightside_fileblock(right_pointer, disk, checkedNums)
            if fileBlockSize is None:
                break
            next_set_of_open_dots = 0
            while left_pointer < len(disk):
                x = disk[left_pointer]
                if left_pointer > right_pointer:
                    break;
                if x == '.':
                    next_set_of_open_dots = get_next_freespace_size(left_pointer, disk)
                if next_set_of_open_dots >= fileBlockSize:
                    break
                left_pointer += 1
            if next_set_of_open_dots == 0:
                break
            if next_set_of_open_dots >= fileBlockSize:
                checkedNums.add(disk[right_pointer])
                disk = swap_block_and_freespace(disk, left_pointer, right_pointer, fileBlockSize)
        right_pointer -= 1

    #print(''.join(x for x in disk))
    answer = calc_checksum(disk)
    print(answer)
    return answer

if __name__ == '__main__':
    main()