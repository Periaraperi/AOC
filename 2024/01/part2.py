import io

def to_int(pair):
    return (int(pair[0]), int(pair[1]))

def count(x, nums):
    return nums.count(x)

with open("./input.txt", "r") as f:
    lines = f.readlines()
    lines = list(map(str.rstrip, lines))
    lines = list(map(str.split, lines))
    lines = list(map(to_int, list(map(tuple, lines))))
    a, b = zip(*lines)
    score = sum([x*count(x, b) for x in a])
    print (score)
