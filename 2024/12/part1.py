def to_char_array(s):
    a = []
    for i in s:
        a.append(i)
    return a

N = 0
M = 0
             #  up     right    down    left
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def can_go(i, j, grid, prev, vis):
    return i >= 0 and i < N and j >= 0 and j < M and\
                  not vis[i][j] and grid[i][j] == prev
def should_increase_perimeter(i, j, grid, prev):
    return i < 0 or i >= N or j < 0 or j >= M or grid[i][j] != prev

def dfs(i, j, grid, vis):
    if vis[i][j]:
        return [0, 0]
    vis[i][j] = True
    
    area = 1
    perimeter = 0
    for d in directions:
        ii = d[0]+i
        jj = d[1]+j
        if should_increase_perimeter(ii, jj, grid, grid[i][j]):
            perimeter += 1
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
