def main():
    filepath = '../input'
    grid_of_paper_rolls = []
    with open(filepath, 'r') as file:
        for line in file.readlines():
            grid_of_paper_rolls.append([x for x in line.strip()])


    num_rows = len(grid_of_paper_rolls)
    num_cols = len(grid_of_paper_rolls[0])

    answer = 0
    has_changed = True

    while has_changed != False:
        has_changed = False
        for row in range(0, num_rows):
            for col in range(0, num_cols):
                curr_idx = (row, col)
                if grid_of_paper_rolls[row][col] == '@':
                    total_neighbors = count_neighbor_rolls(curr_idx, grid_of_paper_rolls, num_rows, num_cols)
                    if total_neighbors < 4:
                        answer += 1
                        grid_of_paper_rolls[row][col] = '.'
                        has_changed = True


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
        if 0 <= new_col < col_length and 0 <= new_row < row_length:
            if grid_of_paper_rolls[new_row][new_col] == '@':
                local_neighbors_count += 1
        if local_neighbors_count > 3:
            break
    return local_neighbors_count


if __name__ == '__main__':
    main()