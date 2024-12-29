def parse_lines(lines):
    towels = set()
    
    ts = lines[0].split(", ")
    for i in ts:
        towels.add(i)
    
    targets = []
    for i in range(2, len(lines)):
        targets.append(lines[i])

    return (towels, targets)

def can_construct(i, target, towels, dp):
    if i == len(target):
        return 1
    if i > len(target):
        return 0
    if dp[i] > 0:
        return dp[i]
    character = target[i]

    ways = 0
    for towel in towels[ord(character)]:
        if towel == target[i:i+len(towel)]:
            ways += can_construct(i + len(towel), target, towels, dp)
    dp[i] = ways
    return ways

def solve(info):
    (towels, targets) = info
    ans = 0

    arr = [[] for _ in range(130)]
    for towel in towels:
        arr[ord(towel[0])].append(towel)
    
    for t in targets:
        dp = [0 for _ in range(len(t))]
        ways = can_construct(0, t, arr, dp)
        ans += ways
    return ans

with open("dp.txt") as file:
    lines = list(map(str.rstrip, file.readlines()))
    print(solve(parse_lines(lines)))
