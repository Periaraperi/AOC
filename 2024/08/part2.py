import io

def is_antenna(ch):
    return (ch >= '0' and ch <= '9') or\
           (ch >= 'a' and ch <= 'z') or\
           (ch >= 'A' and ch <= 'Z')

def place_antinodes(a1, a2, dr, dc):
    r = [0, 0]
    c = [0, 0]
    if a1[0] < a2[0]:
        r[0] = a1[0] - dr
        r[1] = a2[0] + dr
    else:
        r[0] = a1[0] + dr
        r[1] = a2[0] - dr

    if a1[1] < a2[1]:
        c[0] = a1[1] - dc
        c[1] = a2[1] + dc
    else:
        c[0] = a1[1] + dc
        c[1] = a2[1] - dc

    return [(r[0], c[0]), (r[1], c[1])]

def in_bounds(r, c, n, m):
    return r >= 0 and r < n and c >= 0 and c < m

def solve(grid):
    N = len(grid)
    M = len(grid[0])
    
    arr = [[] for _ in range(0, 123)]
    for i in range(N):
        for j in range(M):
            if is_antenna(grid[i][j]):
                arr[ord(grid[i][j])].append((i, j))
    antinodes = set()
    ant_pos_count = 0
    for i in range(len(arr)):
        if len(arr[i]) > 1:
            ant_pos_count += len(arr[i])
            a = arr[i]
            for j in range(len(a)):
                for k in range(j+1, len(a)):
                    a1 = (a[j][0], a[j][1])
                    a2 = (a[k][0], a[k][1])
                    dr = abs(a1[0] - a2[0])
                    dc = abs(a1[1] - a2[1])
                    ok = True
                    x = 1
                    while ok:
                        ok = False
                        (an1, an2) = place_antinodes(a1, a2, x*dr, x*dc)
                        if in_bounds(an1[0], an1[1], N, M):
                            ok = True
                            if grid[an1[0]][an1[1]] == '.': # we do this not to over count. We include existing antenna positions later
                                antinodes.add(an1)
                        if in_bounds(an2[0], an2[1], N, M):
                            ok = True
                            if grid[an2[0]][an2[1]] == '.': # we do this not to over count. We include existing antenna positions later
                                antinodes.add(an2)
                        x += 1
    return len(antinodes) + ant_pos_count

with open("input.txt") as file:
    grid = list(map(str.rstrip, file.readlines()))
    print (solve(grid))
