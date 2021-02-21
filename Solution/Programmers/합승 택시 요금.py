import heapq
INF = int(1e9)

def dijkstra(distance, start, graph):
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

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n+1)]
    for fare in fares:
        x, y, z = fare
        graph[x].append((y, z))
        graph[y].append((x, z))
    
    distance = [INF] * (n+1)
    dijkstra(distance, s, graph)
    ans = INF
    for i in range(1, n+1):
        result = 0
        distance_tmp = [INF] * (n+1)
        dijkstra(distance_tmp, i, graph)
        result = distance[i] + distance_tmp[a] + distance_tmp[b]
        ans = min(ans, result)
    return ans
