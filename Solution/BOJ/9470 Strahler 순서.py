from collections import deque

T = int(input())
for t in range(1, T + 1):
    k, m, p = map(int, input().split())
    graph = [[] for _ in range(m + 1)]
    indegree = [0] * (m + 1)
    strahler = [0] * (m + 1)
    nodes = [[] for _ in range(m + 1)]
    for _ in range(p):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    q = deque()
    for i in range(1, m + 1):
        if indegree[i] == 0:
            strahler[i] = 1
            q.append(i)

    while q:
        curr = q.popleft()
        for i in graph[curr]:
            nodes[i].append(strahler[curr])
            indegree[i] -= 1
            if indegree[i] == 0:
                max_val = max(nodes[i])
                if nodes[i].count(max_val) >= 2:
                    strahler[i] = max_val + 1
                else:
                    strahler[i] = max_val
                q.append(i)

    print(t, strahler[m])
