from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
parts = [[0] * (n+1) for _ in range(n+1)]
not_basic = []
for _ in range(m):
    x, y, k = map(int, input().split())
    graph[y].append((x, k))
    not_basic.append(x)
    indegree[x] += 1

q = deque()
for i in range(n):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    for i in graph[now]:
        if not now in not_basic:
            parts[i[0]][now] = i[1]
        else:
            for j in range(1, n+1):
                parts[i[0]][j] += parts[now][j] * i[1]
        indegree[i[0]] -= 1
        if indegree[i[0]] == 0:
            q.append(i[0])

for i, cnt in enumerate(parts[n]):
    if cnt:
        print(i, cnt)
