from collections import deque
import sys
input = sys.stdin.readline

case = int(input())
for _ in range(case):
    n = int(input())
    indegree = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    
    last = list(map(int, input().split()))
    for i in range(n-1):
        for j in range(i+1, n):
            graph[last[i]].append(last[j])
            indegree[last[j]] += 1

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if b in graph[a]:
            graph[b].append(a)
            graph[a].remove(b)
            indegree[b] -= 1
            indegree[a] += 1
        else:
            graph[a].append(b)
            graph[b].remove(a)
            indegree[a] -= 1
            indegree[b] += 1

    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    result = []
    while q:
        curr = q.popleft()
        result.append(curr)
        for i in graph[curr]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
        
    if len(result) == n:
        print(*result)
    else:
        print('IMPOSSIBLE')
