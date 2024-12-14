# we want to simulate robots in the grid and for each step print the grid and check if it has tree, but
# this approach is insanely tedious and not fun. 
# Because a christmas tree will have many cells interconnected, we can do DFS after each simulation
# and see if bunch of cells are interconnected and only then print the grid and check if it draws a christmas tree

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

simulation_step = 0
def print_grid(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 0:
                print(" ", sep="", end="")
                continue
            print(grid[r][c], sep="", end="")
        print('\n')
    print("SimulationStep:", simulation_step)

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def can_go(r, c, grid, vis, prev):
    return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) and grid[r][c] == prev and not vis[r][c]

def dfs(r, c, grid, vis):
    if vis[r][c]:
        return 0
    vis[r][c] = True

    count = 1 # count of interconnected cells
    for d in dirs:
        rr = r+d[0]
        cc = c+d[1]
        if can_go(rr, cc, grid, vis, grid[r][c]):
            count += dfs(rr, cc, grid, vis)

    return count

magical_number = 30 # our heuristic
def check(grid, rows, columns):
    vis = [[False for _ in range(columns)] for _ in range(rows)]
    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == 0:
                continue
            if not vis[r][c]:
                count = dfs(r, c, grid, vis)
                if count >= magical_number:
                    return True
    return False

# simulate until we have many cells interconnected
# check with dfs
def simulate(info, grid, rows, columns):
    global simulation_step

    while True:
        simulation_step += 1
        for i in info:
            r = i[0][1]
            c = i[0][0]
            grid[r][c] -= 1
            vr = i[1][1]
            vc = i[1][0]
            r = (r + vr) % rows
            c = (c + vc) % columns
            grid[r][c] += 1
            i[0][1] = r
            i[0][0] = c
        if check(grid, rows, columns):
            break

def solve(info, dims):
    columns = dims[0]
    rows = dims[1]
    grid = [[0 for _ in range(columns)] for _ in range(rows)]
    for i in info:
        r = i[0][1]
        c = i[0][0]
        grid[r][c] += 1

    simulate(info, grid, rows, columns)
    print_grid(grid)

with open("input.txt") as file:
    lines = list(map(str.rstrip, file.readlines()))
    dimensions = get_dims(lines[0])
    del lines[0]
    info = parse(lines)
    solve(info, dimensions)
