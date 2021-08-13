import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    q = deque()
    q.append(v)
    dist = [-1 for _ in range(n+1)]
    dist[v] = 0
    while q:
        curr = q.popleft()
        for node, cost in graph[curr]:
            if dist[node] == -1:
                dist[node] = dist[curr] + cost
                q.append(node)

    return dist

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

rtn = bfs(1)
rtn = bfs(rtn.index(max(rtn)))
print(max(rtn))


