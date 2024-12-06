import io
import sys

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

def dfs_stack(r, c, grid):
    counter = 1
    d = (-1, 0)
    stk = [(r, c)]
    while stk:
        cell = stk.pop()
        if grid[cell[0]][cell[1]] == '.':
            counter += 1
        grid[cell[0]][cell[1]] = '-'

        if going_outside(cell[0]+d[0], cell[1]+d[1], grid):
            break

        if can_move(cell[0]+d[0], cell[1]+d[1], grid):
            stk.append((cell[0]+d[0], cell[1]+d[1]))
            continue

        d = change_dir(d[0], d[1])
        stk.append(cell) # revert pop since we are still on same cell if we changed direction

    return counter

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
    
    return dfs_stack(sr, sc, grid)

with open("input.txt") as file:
    grid = list(map(get_as_char_array, list(map(str.rstrip, file.readlines()))))
    print(solve(grid))
