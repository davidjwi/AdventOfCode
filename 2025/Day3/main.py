def main():
    SEQUENCE_LENGTH = 12
    answer = 0
    battery_banks = []
    with open('input', 'r') as input_file:
        for line in input_file.readlines():
            battery_banks.append(line.strip())

 
    for battery_bank in battery_banks:
        battery_sequence_output = generate_sequence_from_start_battery('', battery_bank, 12)
        battery_output_int = int(battery_sequence_output)
        answer += battery_output_int

    print(f'Answer is {answer}')
    return answer

 
def generate_sequence_from_start_battery(battery_sequence: str, battery_bank: str, SEQUENCE_LENGTH: int) -> str:
    
    battery_sequence_length = len(battery_sequence)
    battery_bank_length = len(battery_bank)
    

    if battery_bank_length == 0 or battery_sequence_length > 11:
        return battery_sequence

    high_battery_int = 0
    battery_idx = -1

    end_point = battery_bank_length - (SEQUENCE_LENGTH - battery_sequence_length)

    for idx in range(0, end_point+1):
        battery_int = int(battery_bank[idx])

        if high_battery_int < battery_int:
            high_battery_int = battery_int
            battery_idx = idx

    battery_sequence += str(high_battery_int)
    new_battery_bank_list = battery_bank[battery_idx+1:]

    return generate_sequence_from_start_battery(battery_sequence, new_battery_bank_list, SEQUENCE_LENGTH)

 
if __name__ == '__main__':
    main()
