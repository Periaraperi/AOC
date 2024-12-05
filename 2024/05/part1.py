import io

# guaranteed that input page array has odd length
# guaranteed that input page array only contains <= values that are in rules

def convert_rules(s):
    s = s.split('|')
    return [int(n) for n in s]

def convert_pages(s):
    s = s.split(',')
    return [int(n) for n in s]

def solve(rules, pages):
    mx = 0
    for r in rules:
        mx = max(max(r[0], r[1]), mx)

    g = []
    for i in range(0, mx+1):
        g.append([])
    for r in rules:
        g[r[0]].append(r[1])

    answer = 0
    for p in pages: # each update page array is small so we can brute force
        ok = True
        for i in range(0, len(p)):
            for j in range(i+1, len(p)):
                if not (p[j] in g[p[i]]):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            answer += p[len(p) // 2]

    return answer

with open("input.txt") as file:
    lines = list(map(str.rstrip, file.readlines()))
    rules = []
    pages = []
    change = False
    for l in lines:
        if l == '':
            change = True
            continue
        if change:
            pages.append(l)
        else:
            rules.append(l)
    rules = list(map(convert_rules, rules))
    pages = list(map(convert_pages, pages))
    print(solve(rules, pages))
