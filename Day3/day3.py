import re

def parse_row(row): 
    muls = []
    split_on_dont = row.split('don\'t()')
    #first string is the initial 'do' part
    muls.append(split_on_dont[0])
    # get rid of it before looping thru the remaining 
    split_on_dont.pop(0)
    for x in split_on_dont:
        if 'do()' in x:
            position_of_do = x.find('do()')
            # +4 to position_of_do to get the end of the do() string
            # Take anything after the first do() because there shouldn't
            # be any don't() pieces in this section
            after_do = x[position_of_do+4:]
            muls.append(after_do)
    return muls

def find_multiplications(lines):
    mul_match_list = []
    # regex for mul(123,4) where the numbers are 1-3 digits
    pattern = r'mul\((\d{1,3}\,\d{1,3})\)'
    for row in lines:
        row_matches = re.findall(pattern, row)
        # should be a bunch of strings like '1,2' in row_matches
        for match in row_matches:
            mul_match_list.append(match)
    return mul_match_list

def main():
    filepath = 'day3_input.txt'
    with open(filepath, 'r') as file:
        # remove newline characters from saved input.txt file
        # needed to prevent the \n from changing the logic order of do() and dont()
        combined = ''.join(line.strip('\n') for line in file)

    muls = parse_row(combined)
    multiplication_pairs = find_multiplications(muls) 

    total = 0
    for x in multiplication_pairs:
        p1 = int(x.split(',')[0])
        p2 = int(x.split(',')[1])
        total += p1 * p2 

    print(total)

if __name__ == '__main__':
    main()