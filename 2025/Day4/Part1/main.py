def main():
    filepath = '../input'
    answer = 0
    grid_of_paper_rolls = []
    with open(filepath, 'r') as file:
        for line in file.readlines():
            grid_of_paper_rolls.append([x for x in line.strip()])
    
    col_length = len(grid_of_paper_rolls)
    row_length = len(grid_of_paper_rolls[0])
    
    for row in range(0, row_length):
        for col in range(0, col_length):
            if grid_of_paper_rolls[row][col] == '@':
                key = (row, col)
                total_neighbors = count_neighbor_rolls(key, grid_of_paper_rolls, col_length, row_length)
                if total_neighbors < 4:
                    answer += 1
    print(answer)
    return answer


#(row, col)
directions = {
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
    for direction in directions:
        row_offset, col_offset = directions[direction]
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