import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
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
                path[i[0]] = []
                for p in path[curr]:
                    path[i[0]].append(p)
                path[i[0]].append(i[0])
                heapq.heappush(q, (cost, i[0]))
    
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

path = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
path[start].append(start)
dijkstra(start)

print(distance[end])
print(len(path[end]))
for i in path[end]:
    print(i, end= ' ')
