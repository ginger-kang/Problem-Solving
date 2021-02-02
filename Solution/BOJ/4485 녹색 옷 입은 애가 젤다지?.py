import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dijkstra(x, y, graph):
    q = []
    heapq.heappush(q, (graph[0][0], (x,y)))
    distance[y][x] = graph[0][0]
    while q:
        dist, curr = heapq.heappop(q)
        curr_x, curr_y = curr
        if distance[curr_y][curr_x] < dist:
            continue
        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = dist + graph[ny][nx]
            if cost < distance[ny][nx]:
                distance[ny][nx] = cost
                heapq.heappush(q, (cost, (nx, ny)))

problem_count = 1
while True:
    n = int(input())
    if n == 0:
        break
    graph = []
    distance = [[INF] * n for _ in range(n)]
    for _ in range(n):
        input_data = list(map(int, input().split()))
        graph.append(input_data)
    dijkstra(0, 0, graph)

    print("Problem {}: {}".format(problem_count, distance[n-1][n-1]))
    problem_count += 1
