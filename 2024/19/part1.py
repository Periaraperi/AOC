def parse_lines(lines):
    towels = set()
    
    ts = lines[0].split(", ")
    for i in ts:
        towels.add(i)
    
    targets = []
    for i in range(2, len(lines)):
        targets.append(lines[i])

    return (towels, targets)

def can_construct(i, target, towels):
    if i == len(target):
        return True
    if i > len(target):
        return False
    character = target[i]

    can = False
    for towel in towels[ord(character)]:
        if towel == target[i:i+len(towel)]:
            can = can or can_construct(i + len(towel), target, towels)
            if can:
                return True
    return can

def solve(info):
    (towels, targets) = info
    ans = 0

    arr = [[] for _ in range(130)]
    for towel in towels:
        arr[ord(towel[0])].append(towel)
    
    for t in targets:
        if can_construct(0, t, arr):
            ans += 1
    return ans

with open("input.txt") as file:
    lines = list(map(str.rstrip, file.readlines()))
    print(solve(parse_lines(lines)))
