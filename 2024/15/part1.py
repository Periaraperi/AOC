def to_char_array(s):
    arr = []
    for i in s:
        arr.append(i)
    return arr

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def parse(lines):
    i = 0
    grid = []
    while i < len(lines) and lines[i] != '':
        grid.append(to_char_array(lines[i]))
        i += 1
    i += 1
    p = []
    dd = {
        "^" : dirs[0],
        ">" : dirs[1],
        "v" : dirs[2],
        "<" : dirs[3]
    }
    while i < len(lines):
        for j in lines[i]:
            p.append(dd.get(j))
        i += 1
    return [grid, p]

def in_bounds(i, j, N, M):
    return i >= 0 and j >= 0 and i < N and j < M

def solve(grid, robot_path):
    N = len(grid)
    M = len(grid[0])
    sr = 0
    sc = 0
    for r in range(N):
        found = False
        for c in range(M):
            if grid[r][c] == '@':
                sr = r
                sc = c
                found = True
                break
        if found:
            break

    for d in robot_path:
        rr = sr + d[0]
        cc = sc + d[1]
        if in_bounds(rr, cc, N, M):
            if grid[rr][cc] == '.':
                grid[sr][sc], grid[rr][cc] = grid[rr][cc], grid[sr][sc]
                sr = rr
                sc = cc
            elif grid[rr][cc] == 'O':
                i = rr
                j = cc
                while in_bounds(i, j, N, M) and grid[i][j] == 'O':
                    i += d[0]
                    j += d[1]
                if grid[i][j] == '.':
                    grid[i][j], grid[rr][cc] = grid[rr][cc], grid[i][j]
                    grid[sr][sc], grid[rr][cc] = grid[rr][cc], grid[sr][sc]
                    sr = rr
                    sc = cc
    
    answer = 0
    for r in range(N):
        for c in range(M):
            if grid[r][c] == 'O':
                answer += (100*r + c)
    return answer

with open("input.txt") as file:
    lines = list(map(str.rstrip, file.readlines()))
    info = parse(lines)
    print(solve(info[0], info[1]))
