import io

def solve(line):
    N = len(line)
    arr = []
    count_free_dots = []
    len_of_blocks = []
    k = 0
    index_accum = 0
    for i in range(N):
        for j in range(int(line[i])):
            if i % 2 == 0:
                arr.append(str(k))
            else:
                arr.append(".")
        if i % 2 == 0:
            len_of_blocks.append([int(line[i]), index_accum, k])
            k += 1
        else:
            count_free_dots.append([int(line[i]), index_accum])
        index_accum += int(line[i])

    r = len(len_of_blocks) - 1
    while r >= 0:
        for i in range(len(count_free_dots)):
            if count_free_dots[i][1] < len_of_blocks[r][1] and count_free_dots[i][0] >= len_of_blocks[r][0]:
                for j in range(count_free_dots[i][1], count_free_dots[i][1]+len_of_blocks[r][0]):
                    arr[j] = str(len_of_blocks[r][2])
                count_free_dots[i][0] -= len_of_blocks[r][0]
                count_free_dots[i][1] += len_of_blocks[r][0]
                for j in range(len_of_blocks[r][1], len_of_blocks[r][1]+len_of_blocks[r][0]):
                    arr[j] = "."
                break
        r -= 1
    
    M = len(arr)
    total = 0
    for i in range(M):
        if arr[i] == ".":
            continue
        total += int(arr[i])*i
    return total

with open("input.txt") as file:
    line = str.rstrip(file.readline())
    print(solve(line))
