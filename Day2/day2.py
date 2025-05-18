# 7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9
def check_difference(report):
    for (num, next_num) in zip(report, report[1:]):
        difference = abs(num - next_num)
        if difference < 1 or difference > 3:
            return False
    return True


def check_sorted(report):
    if (report == sorted(report) or report == sorted(report, reverse=True)):
        return True
    else:
        return False


with open("day2_input.txt", 'r') as input_file:
    reports = []
    for line in input_file:
        line = line.strip().split(" ")
        line = list(map(int, line))
        reports.append(line)

safe_reports = []
not_safe_reports = []

for report in reports:
    if check_difference(report) and check_sorted(report):
        safe_reports.append(report)
    else:
        not_safe_reports.append(report)

for report in not_safe_reports:
    for index, num in enumerate(report):
        test_report = report.copy()
        test_report.pop(index)
        if (check_difference(test_report) and check_sorted(test_report)):
            safe_reports.append(report)
            break

print(len(safe_reports))
