import io

def to_int(pair):
    return (int(pair[0]), int(pair[1]))

def dis(pair):
    return abs(pair[0]-pair[1])

with open("./input.txt", "r") as f:
    lines = f.readlines()
    lines = list(map(str.rstrip, lines))
    lines = list(map(str.split, lines))
    lines = list(map(to_int, list(map(tuple, lines))))
    a, b = zip(*lines)
    a = sorted(a)
    b = sorted(b)
    sm = sum(list(map(dis, zip(a, b))))
    print (sm)
