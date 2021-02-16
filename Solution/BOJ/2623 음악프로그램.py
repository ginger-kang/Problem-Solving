import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
flag = True
for _ in range(m):
    singer = list(map(int, input().split()))
    for i in range(1, len(singer) - 1):
        a, b = singer[i:i+2]
        graph[a].append(b)
        indegree[b] += 1

result = []
def sol():
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

sol()

if len(result) != n:
    print(0)
else:
    for i in result:
        print(i)
