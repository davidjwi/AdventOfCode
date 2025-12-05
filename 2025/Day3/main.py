def main():
    answer = 0
    battery_banks = []
    with open('input', 'r') as input_file:
        for line in input_file.readlines():
            battery_banks.append(line.strip())

    for battery_bank in battery_banks:
        firstBattery = find_highest_battery(battery_bank, True)
        firstBatteryIdx = firstBattery[1]
        
        remaining_battery_bank = battery_bank[firstBatteryIdx+1:]
        secondBattery = find_highest_battery(remaining_battery_bank, False)
        
        highest_pair_str = str(firstBattery[0]) + str(secondBattery[0])

        answer += int(highest_pair_str)
        
    print (answer)
    return answer

def find_highest_battery(battery_bank: str, is_first_battery: bool):
    highest_battery = None
    highest_battery_idx = None
    battery_bank_len = len(battery_bank)

    if is_first_battery:
        battery_bank_len = battery_bank_len - 1

    for i in range(0, battery_bank_len):
        battery_int = int(battery_bank[i])

        if highest_battery is None:
            highest_battery = battery_int
            highest_battery_idx = i
        elif highest_battery < battery_int:
            highest_battery = battery_int
            highest_battery_idx = i

        if highest_battery == 9:
            break

    return [highest_battery, highest_battery_idx]


if __name__ == '__main__':
    main()