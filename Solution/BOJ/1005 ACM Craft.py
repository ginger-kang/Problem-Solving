from collections import deque
import sys
input = sys.stdin.readline

def sol():
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        for i in graph[now]:
            next_dist = distance[now] + d[i-1]
            distance[i] = max(distance[i], next_dist)
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
                
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    indegree = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    distance = [0]
    for i in d:
        distance.append(i)
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1
    w = int(input())
    sol()
    print(distance[w])
        
