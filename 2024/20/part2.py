import queue  

INF = 100000000
N = 0
M = 0
si = 0
sj = 0
ei = 0
ej = 0
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def to_char_array(s):
    arr = []
    for i in s:
        arr.append(i)
    return arr

def in_bounds(i, j):
    return i<N and i>=0 and j<M and j>=0 

def bfs(grid, si, sj, dis):
    q = queue.Queue()
    q.put((si, sj, 0))
    dis[si][sj] = 0
    
    while not q.empty():
        i, j, d = q.get()
        
        if d > dis[i][j]:
            continue

        for di, dj in directions:
            ii = i+di
            jj = j+dj
            if in_bounds(ii, jj) and grid[ii][jj] == '.':
                if dis[ii][jj] > d+1:
                    dis[ii][jj] = d+1
                    q.put((ii, jj, d+1))

def solve(grid):
    global si
    global sj
    global ei
    global ej
    for i in range(N):
        for j in range(M):
            if grid[i][j]=='S':
                si = i
                sj = j
                grid[i][j] = '.'
            if grid[i][j]=='E':
                ei = i
                ej = j
                grid[i][j] = '.'

    dis1 = [[INF for _ in range(M)] for _ in range(N)]
    dis2 = [[INF for _ in range(M)] for _ in range(N)]
    bfs(grid, si, sj, dis1)
    bfs(grid, ei, ej, dis2)
    best_without_cheat = dis1[ei][ej]

    target = 100
    mx = 20
    ans = 0

    # don't care about grid border
    for i in range(1, N-1):
        for j in range(1, M-1):
            if grid[i][j] == '#':
                continue
            for r in range(1, N-1):
                for c in range(1, M-1):
                    if grid[r][c] == '#':
                        continue
                    # cheat starts at (i,j) and ends at (r, c)
                    x = abs(i-r)+abs(j-c)
                    if x > mx:
                        continue
                    d = dis1[i][j]+dis2[r][c]+x
                    if best_without_cheat-d >= target:
                        ans += 1
    return ans

with open("input.txt") as file:
    grid = list(map(to_char_array, list(map(str.rstrip, file.readlines()))))
    N = len(grid)
    M = len(grid[0])
    print(solve(grid))
