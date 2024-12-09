import io

def solve(line):
    N = len(line)
    arr = []
    k = 0
    for i in range(N):
        for j in range(int(line[i])):
            if i % 2 == 0:
                arr.append(str(k))
            else:
                arr.append(".")
        if i % 2 == 0:
            k += 1

    M = len(arr)
    l = 0
    r = M - 1
    while (l<r):
        while arr[l] != "." and l < r:
            l += 1
        while arr[r] == "." and r > l:
            r -= 1
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    
    total = 0
    for i in range(M):
        if arr[i] == ".":
            break
        total += int(arr[i])*i
    return total

with open("input.txt") as file:
    line = str.rstrip(file.readline())
    print(solve(line))
