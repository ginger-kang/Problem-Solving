import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, distance):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, curr = heapq.heappop(q)
        for i in graph[curr]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                ans[i[0] - 1][start - 1] = curr

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

ans = [[0] * n for _ in range(n)]
for i in range(1, n+1):
    distance = [INF] * (n+1)
    dijkstra(i, distance)

for i in range(n):
    for j in range(n):
        if i == j:
            print('-', end=" ")
        else:
            print(ans[i][j], end=" ")
    print()
