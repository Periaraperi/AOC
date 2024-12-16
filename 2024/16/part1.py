import queue

def to_char_array(s):
    arr = []
    for i in s:
        arr.append(i)
    return arr

N = 0
M = 0
INF = 1000000000

def in_bounds(i, j):
    return i >= 0 and i < N and j >= 0 and j < M

def solve(grid):
    sr = 0
    sc = 0
    er = 0
    ec = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'S':
                sr = i
                sc = j
            elif grid[i][j] == 'E':
                er = i
                ec = j
    
    pq = queue.PriorityQueue()
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dis = [[[INF for _ in range(4)] for _ in range(M)] for _ in range(N)]

    current_direction = (0, 1)
    for i in range(4):
        dis[sr][sc][i] = 0
    pq.put((0, (sr, sc, current_direction)))
    while not pq.empty():
        curr = pq.get()
        cost = curr[0]
        r = curr[1][0]
        c = curr[1][1]
        curr_dir = curr[1][2]

        for i in range(len(dirs)):
            d = dirs[i]
            rr = r + d[0]
            cc = c + d[1]
            if in_bounds(rr, cc) and grid[rr][cc] != '#':
                new_cost = INF
                if d == curr_dir:
                    new_cost = cost + 1
                elif d == (-curr_dir[0], -curr_dir[1]):
                    new_cost = cost + 2001
                else:
                    new_cost = cost + 1001

                if new_cost < dis[rr][cc][i]:
                    pq.put((new_cost, (rr, cc, d)))
                    dis[rr][cc][i] = new_cost

    return min(dis[er][ec][0], dis[er][ec][1], dis[er][ec][2], dis[er][ec][3])

with open("input.txt") as file:
    grid = list(map(to_char_array, list(map(str.rstrip, file.readlines()))))
    N = len(grid)
    M = len(grid[0])
    print(solve(grid))
