import queue

def to_char_array(s):
    arr = []
    for i in s:
        arr.append(i)
    return arr

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def parse(lines):
    i = 0
    grid = []
    while i < len(lines) and lines[i] != '':
        row = to_char_array(lines[i])
        grid.append([])
        for j in row:
            if j == '#' or j == '.':
                grid[i].append(j)
                grid[i].append(j)
            elif j == '@':
                grid[i].append('@')
                grid[i].append('.')
            elif j == 'O':
                grid[i].append('[')
                grid[i].append(']')
        i += 1
    i += 1
    p = []
    dd = {
        "^" : dirs[0],
        ">" : dirs[1],
        "v" : dirs[2],
        "<" : dirs[3]
    }
    while i < len(lines):
        for j in lines[i]:
            p.append(dd.get(j))
        i += 1
    return [grid, p]

def in_bounds(i, j, N, M):
    return i >= 0 and j >= 0 and i < N and j < M

def solve(grid, robot_path):
    N = len(grid)
    M = len(grid[0])
    sr = 0
    sc = 0
    for r in range(N):
        found = False
        for c in range(M):
            if grid[r][c] == '@':
                sr = r
                sc = c
                found = True
                break
        if found:
            break

    for d in robot_path:
        rr = sr + d[0]
        cc = sc + d[1]
        if in_bounds(rr, cc, N, M):
            if grid[rr][cc] == '.':
                grid[sr][sc], grid[rr][cc] = grid[rr][cc], grid[sr][sc]
                sr = rr
                sc = cc
            elif grid[rr][cc] == '[' or grid[rr][cc] == ']':
                if d == (0, 1) or d == (0, -1): # left right case
                    i = rr
                    j = cc
                    while in_bounds(i, j, N, M) and grid[i][j] == ']' or grid[i][j] == '[':
                        i += d[0]
                        j += d[1]
                    if grid[i][j] == '.':
                        while i != sr or j != sc:
                            grid[i][j], grid[i-d[0]][j-d[1]] = grid[i-d[0]][j-d[1]], grid[i][j] 
                            i -= d[0]
                            j -= d[1]
                        sr = rr
                        sc = cc
                else: # up down case
                    can_move_every_box = True
                    q = queue.SimpleQueue() # will hold coordinates of left and right half of box
                    if grid[rr][cc] == '[':
                        q.put([(rr, cc), (rr, cc+1)])
                    elif grid[rr][cc] == ']':
                        q.put([(rr, cc-1), (rr, cc)])

                    boxes = []

                    while not q.empty():
                        current_box = q.get()
                        if current_box not in boxes:
                            boxes.append(current_box)

                        left_half = current_box[0]
                        li = left_half[0] + d[0]
                        lj = left_half[1] + d[1]

                        right_half = current_box[1]
                        ri = right_half[0] + d[0]
                        rj = right_half[1] + d[1]

                        if in_bounds(li, lj, N, M):
                            if grid[li][lj] == grid[left_half[0]][left_half[1]]:
                                q.put([(li, lj), (li, lj+1)])
                                continue
                            if in_bounds(ri, rj, N, M) and grid[ri][rj] == grid[right_half[0]][right_half[1]]:
                                q.put([(ri, rj-1), (ri, rj)])
                                continue

                            if grid[li][lj] == '#' or (in_bounds(ri, rj, N, M) and grid[ri][rj] == '#'):
                                can_move_every_box = False
                                break

                            potential_box1 = []
                            potential_box2 = []
                            if grid[li][lj] == grid[right_half[0]][right_half[1]]:
                                potential_box1.append((li, lj-1))
                                potential_box1.append((li, lj))
                            if in_bounds(ri, rj, N, M) and grid[ri][rj] == grid[left_half[0]][left_half[1]]:
                                potential_box2.append((ri, rj))
                                potential_box2.append((ri, rj+1))
                            if len(potential_box1) != 0:
                                q.put(potential_box1)
                            if len(potential_box2) != 0:
                                q.put(potential_box2)
                    if can_move_every_box and len(boxes) != 0:
                        for i in range(len(boxes)-1, -1, -1):
                            left_half = boxes[i][0]
                            li = left_half[0] + d[0]
                            lj = left_half[1] + d[1]

                            right_half = boxes[i][1]
                            ri = right_half[0] + d[0]
                            rj = right_half[1] + d[1]

                            grid[left_half[0]][left_half[1]], grid[li][lj] = grid[li][lj], grid[left_half[0]][left_half[1]]
                            grid[right_half[0]][right_half[1]], grid[ri][rj] = grid[ri][rj], grid[right_half[0]][right_half[1]]

                        grid[sr][sc], grid[rr][cc] = grid[rr][cc], grid[sr][sc]
                        sr = rr
                        sc = cc
    answer = 0
    for r in range(N):
        for c in range(M):
            if grid[r][c] == '[':
                answer += (100*r + c)
    return answer

with open("input.txt") as file:
    lines = list(map(str.rstrip, file.readlines()))
    info = parse(lines)
    print(solve(info[0], info[1]))
