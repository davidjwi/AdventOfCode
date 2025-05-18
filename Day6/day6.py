# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...
import copy

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
    for char in row:
        if char in MOVES:
            # Starting point
            move_direction = MOVES.index(char)
            curr_position = [row_num, row.index(char), move_direction]

LAB_SIZE = row_num
# print(LAB_SIZE)

starting_pos = curr_position.copy()


def move_to_next_space(curr_pos, lab_map):
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
        lab_map[curr_pos[0]][curr_pos[1]] = OPEN_ON
        return False

    next_pos = (x, y, curr_pos[2])
    value_of_position = lab_map[x][y]
    if next_pos in unique_moves:
        return None

    if value_of_position == CLOSED:
        if curr_pos[2] == 3:
            next_move_direction = 0
        else:
            next_move_direction = curr_pos[2] + 1
        new_curr_position = (curr_pos[0], curr_pos[1], next_move_direction)
        return new_curr_position

    elif value_of_position == OPEN_OFF:
        lab_map[curr_pos[0]][curr_pos[1]] = OPEN_ON
        new_curr_position = (x, y, curr_pos[2])
        return new_curr_position

    elif value_of_position == OPEN_ON:
        lab_map[curr_pos[0]][curr_pos[1]] = OPEN_ON
        new_curr_position = (x, y, curr_pos[2])
        return new_curr_position


good_obstructions = 0
# +1 lab size
for x in range(LAB_SIZE+1):
    for y in range(LAB_SIZE+1):
        curr_position = starting_pos
        unique_moves = {}
        a = LAB_MAP[x][y]
        if a == '.':
            test_map = copy.deepcopy(LAB_MAP)
            test_map[x][y] = '#'
            while curr_position:
                new_curr_position = move_to_next_space(curr_position, test_map)
                if unique_moves.get(new_curr_position, 0) == 0:
                    unique_moves[new_curr_position] = 1
                if new_curr_position is None:
                    good_obstructions += 1
                    print(good_obstructions)
                curr_position = new_curr_position

print(good_obstructions)
