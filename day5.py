

filepath = 'day5_input.txt'
with open(filepath, 'r') as file:
    file_data = file.read()
    input_data = file_data.split('\n')

for i, x in enumerate(input_data):
    if x == '':
        rule_strings = input_data[:i]
        updates = [x for x in input_data[i:] if x != '']
        break

# print(updates)

rules = [list(map(int, x.split('|'))) for x in rule_strings]

updates_to_check = []

for update_row in updates:
    updates_dict = {}
    int_row = list(map(int, update_row.split(',')))
    for i, number in enumerate(int_row):
        updates_dict[number] = i
    updates_to_check.append(updates_dict)

# print(updates_to_check)
#
# print(rules)

good_updates = []


def check_update(update, rules):
    for rule in rules:
        x = rule[0]
        y = rule[1]
        order_of_x = False
        order_of_y = False
        bad_rule_count = 0
        try:
            order_of_x = update[x]
#            print('x: {} has order: {}'.format(x, order_of_x))
        except KeyError:
            #            print('Key error for x: {}'.format(x))
            pass
        try:
            order_of_y = update[y]
#            print('y: {} has order: {}'.format(y, order_of_y))
        except KeyError:
            #            print('Key error for y: {}'.format(y))
            pass
        if order_of_x is not False and order_of_y is not False:
            # print('Comparing x {} and y {} the orders are {} and {}'.format(x, y, order_of_x, order_of_y))
            if order_of_x < order_of_y:
                print('this rule is good {}'.format(rule))
            else:
                print('the rule is bad... {}'.format(rule))
                bad_rule_count = 1
                break

    if bad_rule_count == 0:
        good_updates.append(update)


for update in updates_to_check:
    #    print(update)
    check_update(update, rules)

# print(good_updates)
total = 0
for update in good_updates:
    dict_len = len(update)
    middle_number = int((dict_len-1)/2)
    number_to_sum = [key for key,
                     value in update.items() if value == middle_number]
#    print(number_to_sum[0])
    total += number_to_sum[0]

print('Answer: {}'.format(total))
