def remove_empty(s):
    return s != ""

def parse(lines):
    info = []
    add = 10000000000000 
    for i in range(0, len(lines), 3):
        button_a = lines[i]
        button_b = lines[i+1]
        prize    = lines[i+2]
        x = button_a.find('+', 0)
        x += 1
        button_a_units = [0, 0]
        while x < len(button_a) and button_a[x] >= '0' and button_a[x] <= '9':
            button_a_units[0] = button_a_units[0]*10 + int(button_a[x])
            x += 1
        x = button_a.find('+', x+1)
        x += 1
        while x < len(button_a) and button_a[x] >= '0' and button_a[x] <= '9':
            button_a_units[1] = button_a_units[1]*10 + int(button_a[x])
            x += 1

        x = button_b.find('+', 0)
        x += 1
        button_b_units = [0, 0]
        while x < len(button_b) and button_b[x] >= '0' and button_b[x] <= '9':
            button_b_units[0] = button_b_units[0]*10 + int(button_b[x])
            x += 1
        x = button_b.find('+', x+1)
        x += 1
        while x < len(button_b) and button_b[x] >= '0' and button_b[x] <= '9':
            button_b_units[1] = button_b_units[1]*10 + int(button_b[x])
            x += 1

        x = prize.find('=', 0)
        x += 1
        prize_pos = [0, 0]
        while x < len(prize) and prize[x] >= '0' and prize[x] <= '9':
            prize_pos[0] = prize_pos[0]*10 + int(prize[x])
            x += 1
        x = prize.find('=', x+1)
        x += 1
        while x < len(prize) and prize[x] >= '0' and prize[x] <= '9':
            prize_pos[1] = prize_pos[1]*10 + int(prize[x])
            x += 1
        
        prize_pos[0] += add
        prize_pos[1] += add
        info.append((button_a_units, button_b_units, prize_pos))

    return info

def is_int(x):
    return x == round(x)

def solve(info):
    answer = 0
    for i in info:
        button_a = i[0]
        button_b = i[1]
        prize = i[2]

        x1 = button_a[0]
        x2 = button_b[0]
        y1 = button_a[1]
        y2 = button_b[1]
        a = prize[0]
        b = prize[1]

        m = (b*x1 - a*y1) / (x1*y2 - x2*y1)
        n = (a - m*x2) / x1
        if is_int(m) and is_int(n):
            answer += (3*int(n) + int(m))
    return answer

with open("input.txt") as file:
    lines = list(filter(remove_empty, list(map(str.rstrip, file.readlines()))))
    info = parse(lines)
    print(solve(info))
