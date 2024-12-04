import io

def is_digit(ch):
    return ch >= '0' and ch <= '9'

def get_num(s, i):
    num = 0
    cnt = 0
    if is_digit(s[i]):
        num = num*10 + int(s[i])
        cnt = 1
        if is_digit(s[i+1]): 
            num = num*10 + int(s[i+1])
            cnt = 2
            if is_digit(s[i+2]): 
                num = num*10 + int(s[i+2])
                cnt = 3
    return (num, cnt)

def solve(s):
    res = 0
    j = 0
    old_len = len(s)
    s = s + "??????????????????????" # not to check for index < length
    do = True
    while j < len(s):
        if j >= old_len:
            break
        i = j
        if s[i] == 'm' and s[i+1] == 'u' and s[i+2] == 'l' and s[i+3] == '(' and do:
            i += len("mul(")
            (num1, cnt1) = get_num(s, i)
            if cnt1 == 0:
                j += 1
                continue
            i += cnt1

            if s[i] != ',':
                j += 1
                continue
            i += 1
            (num2, cnt2) = get_num(s, i)
            if cnt2 == 0:
                j += 1
                continue
            i += cnt2
            if s[i] == ')':
                res += num1*num2
        j += 1
    return res

with open("input.txt") as file:
    data = list(map(str.rstrip, file.readlines()))
    print(solve(data[0]))
