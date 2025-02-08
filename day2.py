# 7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9


lines = []
with open("day2_input.txt", 'r') as input_file:
    for line in input_file:
        lines.append(line.strip().split(" "))

print(lines)

safe_reports = []

for report in lines:
    report = list(map(int, report))
    print(report)
    if (report == sorted(report) or report == sorted(report, reverse=True)):
        isSafe = True
        for i, x in enumerate(report):
            try:
                a = abs(x - report[i+1])
                print(a)
                if not (a >= 1 and a <= 3):
                    print('Adjacent level NOT between 1 and 3: {}'.format(a))
                    safe_reports.append(False)
                    print('breaking')
                    isSafe = False
                    break
                print('here1')
            except:
                IndexError
            print('here2')
        print('here3')
        if isSafe:
            safe_reports.append(True)
    print('Done')
    print(safe_reports)


print(safe_reports)
print(safe_reports.count(True))
