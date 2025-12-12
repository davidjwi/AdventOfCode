def main():
    filepath = 'input'
    
    with open(filepath, 'r') as file:
        lines = file.readlines()
        idx_of_newline = lines.index('\n')
    
    fresh_id_ranges = []
    for idx in range(idx_of_newline):
        id_range = tuple(int(x) for x in lines[idx].split('-'))
        fresh_id_ranges.append(id_range)

    answer = set()
    for idx in range(idx_of_newline+1, len(lines)):
        num_to_check = int(lines[idx])
        for id_range in fresh_id_ranges:
            if id_range[0] <= num_to_check <= id_range[1]:
                answer.add(num_to_check)

    print(len(answer))
    return len(answer)

if __name__ == '__main__':
    main()