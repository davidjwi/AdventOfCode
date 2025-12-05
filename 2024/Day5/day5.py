# 40|78
# 11|90
#
# 40,78,90,10

filepath = 'day5_input.txt'
with open(filepath, 'r') as file:
    file_data = file.read()
    input_data = file_data.split('\n')

for i, x in enumerate(input_data):
    if x == '':
        rule_strings = input_data[:i]
        updates = [list(map(int, x.split(',')))
                   for x in input_data[i:] if x != '']
        break

RULES = [
    tuple(map(int, x.split('|'))) for x in rule_strings
]

UPDATES_TO_CHECK = []

for update_row in updates:
    updates_dict = {}
    for order_value, number_as_key in enumerate(update_row):
        updates_dict[number_as_key] = order_value
    UPDATES_TO_CHECK.append(updates_dict)

bad_updates = []


def check_update(update, RULES):
    for rule in RULES:
        x = rule[0]
        y = rule[1]
        order_of_x = False
        order_of_y = False
        try:
            order_of_x = update[x]
            order_of_y = update[y]
            if order_of_x > order_of_y:
                bad_updates.append(update)
                break
        except KeyError:
            pass


def fix_update(update, RULES):
    for rule in RULES:
        bad_rule_count = 0
        x = rule[0]
        y = rule[1]
        order_of_x = False
        order_of_y = False
        try:
            order_of_x = update[x]
            order_of_y = update[y]
            if order_of_x > order_of_y:
                #                print('The rule is bad... {}\nFor update... {}'.format(rule, update))
                update[x] = order_of_y
                update[y] = order_of_x
                bad_rule_count += 1
        except KeyError:
            pass
        if bad_rule_count > 0:
            fix_update(update, RULES)

    if bad_rule_count == 0:
        return update


for update in UPDATES_TO_CHECK:
    check_update(update, RULES)
# print('Bad Updates: {}'.format(bad_updates))

for update in bad_updates:
    fix_update(update, RULES)
# print('Fixed Updates: {}'.format(bad_updates))
total = 0
for update in bad_updates:
    dict_len = len(update)
    middle_number = int((dict_len-1)/2)
    number_to_sum = [key for key,
                     value in update.items() if value == middle_number]
    total += number_to_sum[0]
print('Answer: {}'.format(total))
