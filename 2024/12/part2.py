def to_char_array(s):
    a = []
    for i in s:
        a.append(i)
    return a

N = 0
M = 0
             #  up     right    down    left
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def in_bounds(i, j):
    return i >= 0 and i < N and j >= 0 and j < M

def can_go(i, j, grid, prev, vis):
    return in_bounds(i, j) and not vis[i][j] and grid[i][j] == prev

def is_same(d, i, j, grid):
    ii = i+d[0]
    jj = j+d[1]
    return in_bounds(ii, jj) and grid[i][j] == grid[ii][jj]

def count_corners(i, j, grid):
    count = 0
    for k in range(len(directions)):
        d1 = directions[k]
        d2 = directions[(k+1)%4]
        d3 = (d1[0]+d2[0], d1[1]+d2[1])
        if not is_same(d1, i, j, grid) and not is_same(d2, i, j, grid):
            count += 1
        if is_same(d1, i, j, grid) and is_same(d2, i, j, grid) and not is_same(d3, i, j, grid):
            count += 1
    return count

def dfs(i, j, grid, vis):
    if vis[i][j]:
        return [0, 0]
    vis[i][j] = True
    
    area = 1
    perimeter = count_corners(i, j, grid)
    for d in directions:
        ii = d[0]+i
        jj = d[1]+j
        if can_go(ii, jj, grid, grid[i][j], vis):
            res = dfs(ii, jj, grid, vis)
            area += res[0]
            perimeter += res[1]
        
    return [area, perimeter]

def solve(grid):
    vis = [[False for _ in range(M)] for _ in range(N)]
    answer = 0
    for i in range(N):
        for j in range(M):
            if not vis[i][j]:
                res = dfs(i, j, grid, vis)
                answer += res[0]*res[1]
    return answer

with open("input.txt") as file:
    grid = list(map(to_char_array, list(map(str.rstrip, file.readlines()))))
    N = len(grid)
    M = len(grid[0])
    print(solve(grid))
