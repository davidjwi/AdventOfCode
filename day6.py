# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# .........
# .#..^.....
# ........#.
# .........
# ......#...

FILEPATH = 'day6_input.txt'
with open(FILEPATH, 'r') as file:
    LAB_MAP = [[char for char in line if char != '\n'] for line in file]

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
MOVES = ('^', '>', 'v', '<')
OPEN_OFF = '.'
OPEN_ON = 'X'
CLOSED = '#'

for row_num, row in enumerate(LAB_MAP):
    # print(row)
    for char in row:
        if char in MOVES:
            # Starting point
            move_direction = MOVES.index(char)
            curr_position = [row_num, row.index(char), move_direction]

LAB_SIZE = row_num


def move_to_next_space(curr_pos):
    x = curr_pos[0]
    y = curr_pos[1]
    if curr_pos[2] == 0:
        x += UP[0]
        y += UP[1]
    elif curr_pos[2] == 1:
        x += RIGHT[0]
        y += RIGHT[1]
    elif curr_pos[2] == 2:
        x += DOWN[0]
        y += DOWN[1]
    elif curr_pos[2] == 3:
        x += LEFT[0]
        y += LEFT[1]

    if x < 0 or y < 0 or x > LAB_SIZE or y > LAB_SIZE:
        # The next move is out of bounds so stop
        LAB_MAP[curr_pos[0]][curr_pos[1]] = OPEN_ON
        return False

    value_of_position = LAB_MAP[x][y]

    if value_of_position == CLOSED:
        if curr_pos[2] == 3:
            next_move_direction = 0
        else:
            next_move_direction = curr_pos[2] + 1 
        new_curr_position = (curr_pos[0], curr_pos[1], next_move_direction)
        return new_curr_position

    elif value_of_position == OPEN_OFF:
        LAB_MAP[curr_pos[0]][curr_pos[1]] = OPEN_ON
        new_curr_position = (x, y, curr_pos[2])
        return new_curr_position

    elif value_of_position == OPEN_ON:
        LAB_MAP[curr_pos[0]][curr_pos[1]] = OPEN_ON
        new_curr_position = (x, y, curr_pos[2])
        return new_curr_position
    else:
        return False


while curr_position:
    new_curr_position = move_to_next_space(curr_position)
    curr_position = new_curr_position

sum = 0
for row in LAB_MAP:
    # print(row)
    sum += row.count('X')
print(sum)
