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

        position_match_count = get_position_matches(
            curr_point,
            word_search,
            WORD_MATCH,
            WORD_LEN,
            WORD_SEARCH_ROW_LENGTH)

        WORD_MATCH_count += position_match_count

    print(WORD_MATCH_count)


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


main()
