import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, curr = heapq.heappop(q)
        if distance[curr] < dist:
            continue
        for i in graph[curr]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
            
n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

dist_start = [INF] * (n+1)
dijkstra(1, dist_start)
dist_v1 = [INF] * (n+1)
dijkstra(v1, dist_v1)
dist_v2 = [INF] * (n+1)
dijkstra(v2, dist_v2)

ans = INF
ans = min(dist_start[v1] + dist_v1[v2] + dist_v2[n], dist_start[v2] + dist_v2[v1] + dist_v1[n])
if ans < INF:
    print(ans)
else:
    print(-1)

