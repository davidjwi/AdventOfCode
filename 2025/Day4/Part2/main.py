def main():
    filepath = '../input'
    grid_of_paper_rolls = []
    with open(filepath, 'r') as file:
        for line in file.readlines():
            grid_of_paper_rolls.append([x for x in line.strip()])



    col_length = len(grid_of_paper_rolls)
    row_length = len(grid_of_paper_rolls[0])

    curr_idx = (0, 0)

    answer = 0
    loop_starting_answer = answer
    loop_end_answer = -1

    checked = set()
    while loop_starting_answer != loop_end_answer:
        loop_starting_answer = answer
        for row in range(0, row_length):
            for col in range(0, col_length):
                curr_idx = (row, col)
                if curr_idx not in checked: 
                    if grid_of_paper_rolls[row][col] == '@':
                        total_neighbors = count_neighbor_rolls(curr_idx, grid_of_paper_rolls, col_length, row_length)
                        if total_neighbors < 4:
                            answer += 1
                            grid_of_paper_rolls[row][col] = '.'
                            checked.add((row, col))
                            break
        loop_end_answer = answer


    print(answer)
    return answer


#(row, col)
DIRECTIONS = {
    'north_west' : (-1, -1),
    'north'      : (-1, 0),
    'north_east' : (-1, 1),
    'east'       : (0, 1),
    'south_east' : (1, 1),
    'south'      : (1, 0),
    'south_west' : (1, -1),
    'west'       : (0, -1)
}


def count_neighbor_rolls(roll_idx: tuple, grid_of_paper_rolls: list, col_length, row_length) -> int:
    local_neighbors_count = 0
    curr_row, curr_col = roll_idx
    for direction in DIRECTIONS:
        row_offset, col_offset = DIRECTIONS[direction]
        new_row = row_offset + curr_row
        new_col = col_offset + curr_col
        if new_col >= 0 and new_col < col_length and new_row >= 0 and new_row < row_length:
            neighbor = grid_of_paper_rolls[new_row][new_col]
            if neighbor == '@':
                local_neighbors_count += 1
        if local_neighbors_count > 3:
            break
    return local_neighbors_count


if __name__ == '__main__':
    main()