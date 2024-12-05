import io

# part 2 of this problem is convertible to topological ordering of graph nodes problem
# we assume all incorrect updates are fixable and fix is unique (i.e topological ordering is unique)

def convert_rules(s):
    s = s.split('|')
    return [int(n) for n in s]

def convert_pages(s):
    s = s.split(',')
    return [int(n) for n in s]

def dfs(v, graph, vis, t_sorted):
    if vis[v]:
        return
    vis[v] = True
    for u in graph[v]:
        if not vis[u]:
            dfs(u, graph, vis, t_sorted)
    t_sorted.append(v)

def top_sort(graph, should_take, mx):
    vis = []
    for i in range(0, mx+1):
        vis.append(True)
    for i in range(0, len(should_take)):
        if should_take[i]:
            vis[i] = False

    t_sorted = []
    for i in range(0, mx+1):
        if not vis[i]:
            dfs(i, graph, vis, t_sorted)

    for i in range(0, len(t_sorted) // 2):
        t_sorted[i], t_sorted[len(t_sorted)-i-1] = t_sorted[len(t_sorted)-i-1], t_sorted[i]
    return t_sorted

def solve(rules, pages):
    mx = 0 # max number that appears in rules/updates
    for r in rules:
        mx = max(max(r[0], r[1]), mx)

    g = [] # rule graph
    for i in range(0, mx+1):
        g.append([])
    for r in rules:
        g[r[0]].append(r[1])

    incorrects = []
    for p in pages: # each update page array is small so we can brute force
        ok = True
        for i in range(0, len(p)):
            for j in range(i+1, len(p)):
                if not (p[j] in g[p[i]]):
                    ok = False
                    incorrects.append(p)
                    break
            if not ok:
                break

    # setup graph with only those values that are in each incorrect update
    graphs = []
    should_takes = []
    for i in range(0, len(incorrects)):
        graph = []
        for j in range(0, mx+1):
            graph.append([])

        should_take = []
        for j in range(0, mx+1):
            should_take.append(False)

        for j in incorrects[i]:
            should_take[j] = True
        should_takes.append(should_take)

        for j in incorrects[i]:
            for k in g[j]:
                if should_take[k]:
                    graph[j].append(k)
        graphs.append(graph)

    answer = 0
    for i in range(0, len(graphs)):
        t_sorted = top_sort(graphs[i], should_takes[i], mx)
        answer += t_sorted[len(t_sorted) // 2]

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
