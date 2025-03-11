# XMASMMX
# MASXMAM
# (x,y)
# x=0,0 m=1,0, a=2,0 s=3,0
# m=0,1 a=1,1, s=2,1

def main():

    WORD_MATCH = 'XMAS'
    WORD_LEN = len(WORD_MATCH)
    WORD_MATCH_count = 0
    word_search = {}
    x_count = 0

    filepath = 'day4_input.txt'
    with open(filepath, 'r') as file:
        lines = []
        for line in file:
            lines.append(line.strip())

    y_coord = 0
    for row in lines:
        x_coord = 0
        for char in row:
            word_search[(x_coord, y_coord)] = char
            x_coord += 1
        y_coord += 1
    # word_search = {(0,0):'M'}

    WORD_SEARCH_ROW_LENGTH = x_coord

    for curr_point, value in word_search.items():
        # curr_point is a tuple (x,y) position
        # reuse x_coord to know the length of the last row
        # assume all rows in the word search are the same length
        (x, y) = curr_point

        x_match = get_x_pattern(curr_point, word_search)
        x_count += x_match

        position_match_count = get_position_matches(
            curr_point,
            word_search,
            WORD_MATCH,
            WORD_LEN,
            WORD_SEARCH_ROW_LENGTH)

        WORD_MATCH_count += position_match_count

    print('Part 2 answer: {}'.format(x_count))
    print('Part 1 answer: {}'.format(WORD_MATCH_count))


def get_position_matches(curr_position, word_search_dict, WORD_MATCH, WORD_LEN, WORD_SEARCH_ROW_LENGTH):
    x = curr_position[0]
    y = curr_position[1]
    back = ''
    up_left = ''
    up = ''
    up_right = ''
    right = ''
    down_right = ''
    down = ''
    down_left = ''
    count_of_position_matches = 0
    # Allowed (true/false) searches for this position
    search_back = (x >= WORD_LEN-1)
    search_up_left = (x >= (WORD_LEN-1) and y >= (WORD_LEN-1))
    search_up = (y >= WORD_LEN-1)
    search_up_right = (
        x <= (WORD_SEARCH_ROW_LENGTH-(WORD_LEN)) and
        y >= (WORD_LEN-1)
    )
    search_right = (x <= (WORD_SEARCH_ROW_LENGTH-(WORD_LEN)))
    search_down_right = (
        x <= (WORD_SEARCH_ROW_LENGTH-(WORD_LEN)) and
        y <= (WORD_SEARCH_ROW_LENGTH-(WORD_LEN))
    )
    search_down = (y <= (WORD_SEARCH_ROW_LENGTH-(WORD_LEN)))
    search_down_left = (
        x >= (WORD_LEN-1) and
        y <= (WORD_SEARCH_ROW_LENGTH-(WORD_LEN))
    )

    for n in range(4):
        if search_back:
            back += ''.join(word_search_dict[(x-n, y)])
            if back == WORD_MATCH:
                count_of_position_matches += 1

        if search_up_left:
            up_left += ''.join(word_search_dict[x-n, y-n])
            if up_left == WORD_MATCH:
                count_of_position_matches += 1

        if search_up:
            up += ''.join(word_search_dict[x, y-n])
            if up == WORD_MATCH:
                count_of_position_matches += 1

        if search_up_right:
            up_right += ''.join(word_search_dict[x+n, y-n])
            if up_right == WORD_MATCH:
                count_of_position_matches += 1

        if search_right:
            right += ''.join(word_search_dict[x+n, y])
            if right == WORD_MATCH:
                count_of_position_matches += 1

        if search_down_right:
            down_right += ''.join(word_search_dict[x+n, y+n])
            if down_right == WORD_MATCH:
                count_of_position_matches += 1

        if search_down:
            down += ''.join(word_search_dict[x, y+n])
            if down == WORD_MATCH:
                count_of_position_matches += 1

        if search_down_left:
            down_left += ''.join(word_search_dict[x-n, y+n])
            if down_left == WORD_MATCH:
                count_of_position_matches += 1

    return count_of_position_matches

def get_x_pattern(curr_position, word_search_dict):
    # curr_pos = x,y
    x = curr_position[0]
    y = curr_position[1]
    count_of_matches = 0

#    first_slash = [(x-1, y-1), (x, y), (x+1, y+1)]
    a1 = (x-1, y-1)
    a2 = (x, y)
    a3 = (x+1, y+1)
#    second_slash = [(x-1, y+1), (x, y), (x+1, y-1)]
    b1 = (x-1, y+1)
    b2 = (x, y)
    b3 = (x+1, y-1)
    try:
        first_slash = word_search_dict[a1[0], a1[1]] + word_search_dict[a2[0], a2[1]] + word_search_dict[a3[0], a3[1]]
        second_slash = word_search_dict[b1[0], b1[1]] + word_search_dict[b2[0], b2[1]] + word_search_dict[b3[0], b3[1]]
        print('{} x {}'.format(first_slash, second_slash))
        if (first_slash == 'MAS' or first_slash == 'SAM') and (second_slash == 'MAS' or second_slash == 'SAM'):
            count_of_matches += 1
    except KeyError:
        print('There was a key error')

    return count_of_matches


main()







