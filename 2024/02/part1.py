import io

def to_num(arr):
    return [int(i) for i in arr]

def is_inc_dec(report):
    l = len(report)
    if l == 1:
        return True

    if report[0] < report[1]:
        for i in range(0, l-1):
            if report[i] > report[i+1]:
                return False
    else:
        for i in range(0, l-1):
            if report[i] < report[i+1]:
                return False

    return True

def is_good_neighbours(report):
    for i in range(0, len(report)-1):
        a = abs(report[i]-report[i+1])
        if a < 1 or a > 3:
            return False
    return True

def solve(reports):
    safe_reports = 0
    for report in reports:
        if is_inc_dec(report) and is_good_neighbours(report):
            safe_reports += 1
    return safe_reports

with open("input.txt") as file:
    reports = list(map(to_num, list(map(str.split, list(map(str.rstrip, file.readlines()))))))
    print(solve(reports))
