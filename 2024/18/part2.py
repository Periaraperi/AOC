import queue

def get_input(s):
    x = s.split(",")
    return (int(x[0]), int(x[1]))

#N = 7
N = 71
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def in_bounds(r, c):
    return r >= 0 and r < N and c >= 0 and c < N

def pg(grid):
    for i in range(N):
        for j in range(N):
            print(grid[i][j], sep='', end='')
        print()
    print()

def bfs(x):
    grid = [['.' for _ in range(N)] for _ in range(N)]
    for i in range(x):
        (r, c) = points[i]
        grid[r][c] = '#'
    q = queue.SimpleQueue()
    q.put((0, 0, 0)) # r, c, breadth-level

    while not q.empty():
        (r, c, level) = q.get()
        
        if (r == N-1 and c == N-1):
            return level

        for d in dirs:
            rr = r+d[0]
            cc = c+d[1]
            if in_bounds(rr, cc) and grid[rr][cc] == '.':
                grid[rr][cc] = 'O'
                q.put((rr, cc, level+1))
    
    return -1

def solve(points):
    for i in range(len(points)):
        if bfs(i+1) == -1:
            return points[i]
    return []

with open("input.txt") as file:
    points = list(map(get_input, list(map(str.rstrip, file.readlines()))))
    print(solve(points))


