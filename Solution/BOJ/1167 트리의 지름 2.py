from collections import deque
import sys
input = sys.stdin.readline

def bfs(e):
    q = deque()
    q.append(e)
    dist = [-1 for _ in range(v+1)]
    dist[e] = 0
    while q:
        curr = q.popleft()
        for i in graph[curr]:
            node, cost = i
            if dist[node] == -1:
                dist[node] = dist[curr] + cost
                q.append(node)

    return dist

v = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(v):
    c = list(map(int, input().split()))
    for e in range(1, len(c) - 2, 2):
        graph[c[0]].append((c[e], c[e + 1]))

rtn = bfs(1)
rtn = bfs(rtn.index(max(rtn)))
print(max(rtn))
