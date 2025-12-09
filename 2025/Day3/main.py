def main():
    SEQUENCE_LENGTH = 12 
    answer = 0
    battery_banks = []
    with open('input', 'r') as input_file:
        for line in input_file.readlines():
            battery_banks.append(line.strip())

    for battery_bank in battery_banks:
        battery_sequence = '' # the sequence answer for a given battery_bank
        highest_starting_batteries = find_highest_battery(battery_bank, SEQUENCE_LENGTH)

        starting_battery_str = str(highest_starting_batteries[0])
        battery_sequence += starting_battery_str
        starting_battery_idx = highest_starting_batteries[1]

        new_battery_bank_list = battery_bank[starting_battery_idx+1:]
        battery_sequence_output = generate_sequence_from_start_battery(starting_battery_str, starting_battery_idx, new_battery_bank_list, SEQUENCE_LENGTH)
        battery_output_int = int(battery_sequence_output)

        print(f'For the row the answer to add is {battery_output_int}')
        answer += battery_output_int

    print(answer)
    return answer

def generate_sequence_from_start_battery(battery_sequence: str, battery_idx: int, battery_bank: str, SEQUENCE_LENGTH: int) -> str:

    battery_sequence_length = len(battery_sequence)
    battery_bank_length = len(battery_bank)

    if battery_bank_length == 0 or battery_sequence_length > 11:
        return battery_sequence

    high_battery_int = 0
    battery_idx_list = []

    end_point = battery_bank_length - (SEQUENCE_LENGTH - battery_sequence_length)
    for idx in range(0, end_point+1): 
        battery_int = int(battery_bank[idx])

        if high_battery_int == 0:
            high_battery_int = battery_int
            battery_idx_list.append(idx)

        elif high_battery_int < battery_int:
            high_battery_int = battery_int
            battery_idx_list = [idx]

        elif high_battery_int == battery_int:
            battery_idx_list.append(idx)
        
    battery_sequence += str(high_battery_int)
    for idx in battery_idx_list:
        new_battery_bank_list = battery_bank[idx+1:]
        return generate_sequence_from_start_battery(battery_sequence, idx, new_battery_bank_list, SEQUENCE_LENGTH)


def find_highest_battery(battery_bank: str, battery_bank_stop_offsset: int) -> list:
    battery_bank_len = len(battery_bank)

    battery_bank_len = battery_bank_len - battery_bank_stop_offsset

    temp_high_battery = 0
    battery_idx = 0

    for i in range(0, battery_bank_len):
        battery_int = int(battery_bank[i])

        if temp_high_battery == 0:
            temp_high_battery = battery_int
            battery_idx = i
        elif temp_high_battery < battery_int:
            temp_high_battery = battery_int
            battery_idx = i

    return [temp_high_battery, battery_idx]


if __name__ == '__main__':
    main()