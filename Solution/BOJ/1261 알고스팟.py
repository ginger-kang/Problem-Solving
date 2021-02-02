import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dijkstra(x, y, crash):
    q = []
    heapq.heappush(q, (0, (x, y)))
    crash[y][x] = 0
    while q:
        prev_crash, curr = heapq.heappop(q)
        curr_x, curr_y = curr
        if crash[curr_y][curr_x] < prev_crash:
            continue
        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n or crash[ny][nx] != INF:
                continue
            if graph[ny][nx] == 1:
                new_crash = prev_crash + 1
                crash[ny][nx] = new_crash
                heapq.heappush(q, (new_crash, (nx, ny)))
            else:
                crash[ny][nx] = prev_crash
                heapq.heappush(q, (prev_crash, (nx, ny)))

m, n = map(int, input().split())
graph = []
for _ in range(n):
    tmp = []
    input_data = input()
    for i in input_data:
        if i != '\n':
            tmp.append(int(i))
    graph.append(tmp)

crash = [[INF] * m for _ in range(n)]

dijkstra(0, 0, crash)
print(crash[n-1][m-1])
