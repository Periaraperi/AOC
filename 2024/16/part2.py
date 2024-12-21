import queue

def to_char_array(s):
    arr = []
    for i in s:
        arr.append(i)
    return arr

N = 0
M = 0
INF = 1000000000
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def in_bounds(i, j):
    return i >= 0 and i < N and j >= 0 and j < M

def dijkstra(sr, sc, er, ec, grid):
    lowest_cost = [[[INF for _ in range(4)] for _ in range(M)] for _ in range(N)]
    tiles = set()
    pq = queue.PriorityQueue()
    pq.put((0, (sr, sc, 1, [(sr, sc)])))
    lowest_cost[sr][sc][1] = 0
    best = INF

    while not pq.empty():
        cell = pq.get()
        cost = cell[0]
        r, c, d_index, path = cell[1]

        if r == er and c == ec:
            if cost <= best:
                best = cost
                for rr, cc in path:
                    tiles.add((rr, cc))
            else:
                break

        if lowest_cost[r][c][d_index] < cost:
            continue

        for new_cost, nr, nc, new_d_index in [(cost+1, r+dirs[d_index][0], c+dirs[d_index][1], d_index),\
                                              (cost+1000, r, c, (d_index+1)%4),\
                                              (cost+1000, r, c, (d_index-1)%4),\
                                              (cost+2000, r, c, (d_index+2)%4)]:
            if not in_bounds(nr, nc):
                continue
            if grid[nr][nc] == '#':
                continue
            if lowest_cost[nr][nc][new_d_index] < new_cost:
                continue
            
            if new_cost < lowest_cost[nr][nc][new_d_index]:
                lowest_cost[nr][nc][new_d_index] = new_cost

            pp = list(path)
            if d_index == new_d_index:
                pp.append((nr, nc))
            pq.put((new_cost, (nr, nc, new_d_index, pp)))
    
    return len(tiles)

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
    return dijkstra(sr, sc, er, ec, grid)

with open("input.txt") as file:
    grid = list(map(to_char_array, list(map(str.rstrip, file.readlines()))))
    N = len(grid)
    M = len(grid[0])
    print(solve(grid))
