import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    time[start] = 0
    while q:
        dist, curr = heapq.heappop(q)
        for i in graph[curr]:
            cost = dist + i[1]
            if cost < time[i[0]]:
                time[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

t = int(input())
for _ in range(t):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    time = [INF] * (n+1)
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append([a, s])

    dijkstra(c)
    cnt = 1
    com = 0
    for i in time:
        if i != INF:
            if com < i:
                com = i
            cnt += 1
    print(cnt - 1, com)
