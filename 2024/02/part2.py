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
    l = len(report)
    for i in range(0, l-1):
        a = abs(report[i]-report[i+1])
        if a < 1 or a > 3:
            return False
    return True

def can_fix(report):
    if len(report) <= 2:
        return True

    # prefix and suffix structures for inc/dec
    pref_inc = [False for i in report]
    pref_inc[0] = True
    pref_dec = [False for i in report]
    pref_dec[0] = True
    suff_inc = [False for i in report]
    suff_inc[len(report)-1] = True
    suff_dec = [False for i in report]
    suff_dec[len(report)-1] = True
    for i in range(1, len(report)):
        if report[i-1] < report[i]:
            pref_inc[i] = True
        else:
            break
    for i in range(1, len(report)):
        if report[i-1] > report[i]:
            pref_dec[i] = True
        else:
            break
    for i in range(len(report)-2, -1, -1):
        if report[i] > report[i+1]:
            suff_inc[i] = True
        else:
            break
    for i in range(len(report)-2, -1, -1):
        if report[i] < report[i+1]:
            suff_dec[i] = True
        else:
            break

    bad_neighbours = []
    for i in range(0, len(report)-1):
        a = abs(report[i]-report[i+1])
        if a < 1 or a > 3:
            bad_neighbours.append(i)

    if len(bad_neighbours) > 2:
        return False
    elif len(bad_neighbours) == 1:
        l = bad_neighbours[0]
        r = l+1
        if (l == 0 and (suff_dec[l+1] or suff_inc[l+1])) or (r == len(report)-1 and (pref_inc[r-1] or pref_dec[r-1])):
            return True
        else:
            if l-1 >= 0:
                a = abs(report[l-1]-report[r]) # try removing left
                if a >= 1 and a <= 3 and ((pref_inc[l-1] and suff_dec[r] and report[l-1] < report[r]) or (pref_dec[l-1] and suff_inc[r] and report[l-1] > report[r])):
                    return True
            if r+1 < len(report):
                b = abs(report[l]-report[r+1]) # try removing right
                if b >= 1 and b <= 3 and ((pref_inc[l] and suff_dec[r+1] and report[l] < report[r+1]) or (pref_dec[l] and suff_inc[r+1] and report[l] > report[r+1])):
                    return True
        return False
    elif len(bad_neighbours) == 2:
        l1 = bad_neighbours[0]
        r1 = l1+1
        l2 = bad_neighbours[1]
        r2 = l2+1
        if l2 != r1:
            return False
        a = abs(report[l1]-report[r2])
        if a >= 1 and a <= 3 and ((pref_inc[l1] and suff_dec[r2] and report[l1] < report[r2]) or (pref_dec[l1] and suff_inc[r2] and report[l1] > report[r2])):
            return True
        return False
    print(report)

    # if we are here that means neighbours don't need fix, but inc/dec does
    for i in range(0, len(report)):
        # try removing i
        if i == 0 and (suff_dec[i+1] or suff_inc[i+1]):
            return True
        if i == len(report)-1 and (pref_inc[i-1] or pref_dec[i-1]):
            return True
        if i > 0 and i < len(report)-1:
            a = abs(report[i-1]-report[i+1])
            if a >= 1 and a <= 3 and ((pref_inc[i-1] and suff_dec[i+1] and report[i-1] < report[i+1]) or (pref_dec[i-1] and suff_inc[i+1] and report[i-1] > report[i+1])):
                return True
    return False

def solve(reports):
    safe_reports = 0
    for report in reports:
        cf = can_fix(report)
        if (is_inc_dec(report) and is_good_neighbours(report)) or cf:
            safe_reports += 1
    return safe_reports

with open("input.txt") as file:
    reports = list(map(to_num, list(map(str.split, list(map(str.rstrip, file.readlines()))))))
    print(solve(reports))
