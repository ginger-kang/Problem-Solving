import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def sol(start):
    q = []
    heapq.heappush(q, (0,start))
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

v, e = map(int, input().split(' '))
k = int(input())
graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)
for _ in range(e):
    u, v, w = list(map(int, input().split(' ')))
    graph[u].append((v, w))

sol(k)

for i in range(1, len(distance)):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
