def get_dims(s):
    d = s.split()
    return [int(d[0]), int(d[1])]

def get_num(i, l, n):
    num = 0
    is_neg = False
    if l[i] == '-':
        is_neg = True
        i += 1
    
    while i < n and l[i] >= '0' and l[i] <= '9':
        num = num*10 + int(l[i])
        i += 1
    if is_neg:
        num *= (-1)
    return num

def parse(lines):
    info = []

    for l in lines:
        p = []
        v = []
        i = l.find('=') + 1
        p.append(get_num(i, l, len(l)))
        i = l.find(',') + 1
        p.append(get_num(i, l, len(l)))

        i = l.rfind('=') + 1
        v.append(get_num(i, l, len(l)))
        i = l.rfind(',') + 1
        v.append(get_num(i, l, len(l)))

        info.append([p, v])
    return info

def solve(info, dims):
    columns = dims[0]
    rows = dims[1]
    sec = 100
    grid = [[0 for _ in range(columns)] for _ in range(rows)]
    for i in info:
        r = i[0][1]
        c = i[0][0]
        vr = i[1][1]
        vc = i[1][0]
        rr = (r + vr*sec) % rows
        cc = (c + vc*sec) % columns
        grid[rr][cc] += 1

    counts = [0, 0, 0, 0]
    for r in range(rows // 2):
        for c in range(columns // 2):
            counts[0] += grid[r][c]
    for r in range(rows // 2):
        for c in range(columns // 2 + 1, columns):
            counts[1] += grid[r][c]
    for r in range(rows // 2 + 1, rows):
        for c in range(columns // 2):
            counts[2] += grid[r][c]
    for r in range(rows // 2 + 1, rows):
        for c in range(columns // 2 + 1, columns):
            counts[3] += grid[r][c]

    return counts[0]*counts[1]*counts[2]*counts[3]

with open("input.txt") as file:
    lines = list(map(str.rstrip, file.readlines()))
    dimensions = get_dims(lines[0])
    del lines[0]
    info = parse(lines)
    print(solve(info, dimensions))
