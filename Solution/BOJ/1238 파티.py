import sys
import heapq
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

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
party = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dijkstra(x, party)

ans = 0
for i in range(1, n+1):
    if i == x:
        continue
    distance = [INF] * (n+1)
    dijkstra(i, distance)
    ans = max(ans, party[i] + distance[x])

print(ans)
    
