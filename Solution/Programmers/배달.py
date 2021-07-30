from collections import deque

def bfs(v, graph, dist):
    dist[v] = 0
    q = deque()
    q.append(v)
    while q:
        curr = q.popleft()
        for i in graph[curr]:
            dest, cost = i
            if dist[dest] == -1 or dist[dest] > cost + dist[curr]:
                dist[dest] = cost + dist[curr]
                q.append(dest)

def solution(N, roads, K):
    graph = [[] for _ in range(N+1)]
    
    for road in roads:
        a, b, c = road
        graph[a].append([b, c])
        graph[b].append([a, c])
    
    dist = [-1] * (N+1)
    bfs(1, graph, dist)
    
    ans = 0
    for i in dist:
        if i <= K and i != -1:
            ans += 1
    
    return ans