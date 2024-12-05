N = 0
M = 0

def in_range(r, c):
    return r >= 0 and r < N and c >= 0 and c < M

def is_x_mas(r, c, grid):
    if grid[r][c] != 'A':
        return False

    if not in_range(r+1, c+1) or not in_range(r+1, c-1) or not in_range(r-1, c+1) or not in_range(r-1, c-1):
        return False
    
    diagonal1 = (grid[r+1][c+1] == 'M' and grid[r-1][c-1] == 'S') or (grid[r+1][c+1] == 'S' and grid[r-1][c-1] == 'M')
    diagonal2 = (grid[r+1][c-1] == 'M' and grid[r-1][c+1] == 'S') or (grid[r+1][c-1] == 'S' and grid[r-1][c+1] == 'M')
    return diagonal1 and diagonal2

def solve(grid):
    count = 0
    for i in range(0, N):
        for j in range(0, M):
            if is_x_mas(i, j, grid):
                count += 1
    return count

with open("input.txt") as file:
    grid = list(map(str.rstrip, file.readlines()))
    N = len(grid)
    M = len(grid[0])
    print(solve(grid))
