N = 0
M = 0

directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def in_range(r, c):
    return r >= 0 and r < N and c >= 0 and c < M

def is_xmas(r, c, d, grid):
    for i in range (1, 4):
        if not in_range(r+i*d[0], c+i*d[1]):
            return False
    return grid[r][c] == 'X' and grid[r+d[0]][c+d[1]] == 'M' and grid[r+2*d[0]][c+2*d[1]] == 'A' and grid[r+3*d[0]][c+3*d[1]] == 'S'

def solve(grid):
    count = 0
    for i in range(0, N):
        for j in range(0, M):
            for d in directions:
                if is_xmas(i, j, d, grid):
                    count += 1
    return count

with open("input.txt") as file:
    grid = list(map(str.rstrip, file.readlines()))
    N = len(grid)
    M = len(grid[0])
    print(solve(grid))
