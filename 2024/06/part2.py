import io
import sys
import copy

# NOTE: This solution is extremely slow in python but if we wait for some time, we get answer.
# We are using brute force approach. Basically for every empty cell we try to place an obstacle, and simulate our path.
# If we go outside that means no loop, if we visit cell that we visited before in the same state (i.e. direction is same), then we have a loop

def get_as_char_array(s):
    arr = []
    for i in s:
        arr.append(i)
    return arr

def can_move(r, c, grid):
    return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) and (grid[r][c] == '.' or grid[r][c] == '-')

def going_outside(r, c, grid):
    return not (r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]))

def change_dir(r, c):
    return (c, -r)

def simulate(r, c, grid):
    counter = 0
    d = (-1, 0)
    stk = [(r, c)]

    N = len(grid)
    M = len(grid[0])
    
    vis = [[ [] for _ in range(M)] for _ in range(N)]

    while stk:
        cell = stk.pop()

        grid[cell[0]][cell[1]] = '-'

        if going_outside(cell[0]+d[0], cell[1]+d[1], grid):
            return False

        r = cell[0]+d[0]
        c = cell[1]+d[1]
        if can_move(r, c, grid):
            if d in vis[r][c]:
                return True
            stk.append((r, c))
            vis[r][c].append(d)
            continue

        d = change_dir(d[0], d[1])
        stk.append(cell) # revert pop since we are still on same cell if we changed direction

    return True

def solve(grid):
    sr = 0
    sc = 0
    for r in range(0, len(grid)):
        found = False
        for c in range(0, len(grid[r])):
            if grid[r][c] == '^':
                sr = r
                sc = c
                grid[r][c] = '-'
                found = True
                break
        if found:
            break

    can_loop = 0
    for r in range(0, len(grid)):
        for c in range(0, len(grid[r])):
            tmp_grid = copy.deepcopy(grid)
            if tmp_grid[r][c] == '.':
                tmp_grid[r][c] = '#'
            if simulate(sr, sc, tmp_grid):
                can_loop += 1
            #print(can_loop) disable this to see that new loops are actually found
    
    return can_loop

with open("input.txt") as file:
    grid = list(map(get_as_char_array, list(map(str.rstrip, file.readlines()))))
    print(solve(grid))
