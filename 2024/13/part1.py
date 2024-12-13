def remove_empty(s):
    return s != ""

def parse(lines):
    info = []
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
        
        info.append((button_a_units, button_b_units, prize_pos))

    return info

def solve(info):
    max_button_presses = 100
    infinity = max_button_presses*max_button_presses
    answer = 0
    for i in info:
        button_a = i[0]
        button_b = i[1]
        prize = i[2]

        tokens = infinity
        for n in range(max_button_presses+1):
            for m in range(max_button_presses+1):
                if button_a[0]*n + button_b[0]*m == prize[0] and\
                   button_a[1]*n + button_b[1]*m == prize[1]:
                    tokens = min(tokens, (3*n + m))

        if tokens != infinity:
            answer += tokens
    return answer

with open("input.txt") as file:
    lines = list(filter(remove_empty, list(map(str.rstrip, file.readlines()))))
    info = parse(lines)
    print(solve(info))
