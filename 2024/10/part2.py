import io
import copy

def to_int_array(s):
    arr = []
    for i in s:
        arr.append(int(i))
    return arr

def can_go(i, j, g, old_value, vis):
    return i >= 0 and i < len(g) and \
           j >= 0 and j < len(g[0]) and \
           not vis[i][j] and g[i][j] - 1 == old_value

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(i, j, g, vis):
    if vis[i][j]:
        return 0
    vis[i][j] = True
    if g[i][j] == 9:
        return 1

    count = 0
    for k in d:
        if can_go(i+k[0], j+k[1], g, g[i][j], vis):
            count += dfs(i+k[0], j+k[1], g, vis)
            vis[i+k[0]][j+k[1]] = False

    vis[i][j] = False
    return count

def solve(grid):
    starting_cells = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                starting_cells.append((i, j))
    
    answer = 0
    for i in range(len(starting_cells)):
        g = copy.deepcopy(grid)
        vis = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        answer += dfs(starting_cells[i][0], starting_cells[i][1], g, vis)
    return answer

with open("input.txt") as file:
    grid = list(map(to_int_array, list(map(str.rstrip, file.readlines()))))
    print(solve(grid))
