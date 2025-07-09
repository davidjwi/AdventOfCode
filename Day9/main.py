def get_input_line(filepath):
    with open(filepath, 'r') as file:
        return file.readline().strip()
    
def create_disk_map(line: str):
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

def swap_dots_to_end(disk_list: list):
    right_pointer = len(disk_list) - 1

    for left_i in range(len(disk_list)):
        if left_i >= right_pointer:
            break

        if disk_list[left_i] == '.':
            while disk_list[right_pointer] == '.' and left_i < right_pointer:
                right_pointer -= 1

            disk_list[left_i], disk_list[right_pointer] = disk_list[right_pointer], disk_list[left_i]

            right_pointer -= 1
    return disk_list 
        

def calc_checksum(disk_list: list):
    return sum(i * int(val) for i, val in enumerate(disk_list) if val != '.')

        
def main(filepath: str):
    input_line = get_input_line(filepath)
    disk_map_visual = create_disk_map(input_line)
    updated_list = swap_dots_to_end(disk_map_visual) 
    answer = calc_checksum(updated_list)
    return answer
    


if __name__ == '__main__':
    filepath = 'Day9/input.txt'
    print (main(filepath))