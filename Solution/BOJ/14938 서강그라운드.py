import heapq
INF = int(1e9)

def dijkstra(start, graph, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, curr = heapq.heappop(q)
        if distance[curr] < dist:
            continue
        for v in graph[curr]:
            cost = dist + v[1]
            if cost < distance[v[0]]:
                distance[v[0]] = cost
                heapq.heappush(q, (cost, v[0]))

n, m, r = list(map(int, input().split()))
items = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

ans = int(-1e9)
for i in range(1, n+1):
    distance = [INF] * (n+1)
    result = 0
    dijkstra(i, graph, distance)
    for j in range(1, n+1):
        if distance[j] <= m:
            result += items[j-1]
            
    ans = max(ans, result)

print(ans)
