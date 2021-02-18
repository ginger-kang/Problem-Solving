import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, distance):
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, curr = heapq.heappop(q)
        for n, c in graph[curr]:
            next_cost = dist + c
            if len(distance[n]) < k:
                heapq.heappush(distance[n], -next_cost)
                heapq.heappush(q, (next_cost, n))
            elif (-1 * distance[n][0]) > next_cost:
                heapq.heappop(distance[n])
                heapq.heappush(distance[n], -next_cost)
                heapq.heappush(q, (next_cost, n))

n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
distance = []
for i in range(n+1):
    q = []
    heapq.heapify(q)
    distance.append(q)

heapq.heappush(distance[1], 0)
dijkstra(1, distance)
for i in range(1, n+1):
    if len(distance[i]) < k:
        print(-1)
    else:
        print(-distance[i][0])
