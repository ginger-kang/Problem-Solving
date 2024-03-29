from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    
def sol():
    result = [0] * (n+1)
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append((i, 1))
    while q:
        now, degree = q.popleft()
        result[now] = degree
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append((i, degree + 1))
    for i in range(1, n+1):
        print(result[i], end=' ')
    
sol()
