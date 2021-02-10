import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

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
            if nx < 0 or nx >= n or ny < 0 or ny >= n or crash[ny][nx] != INF:
                continue
            if board[ny][nx] == 1:
                crash[ny][nx] = prev_crash
                heapq.heappush(q, (prev_crash, (nx, ny)))
            else:
                next_crash = prev_crash + 1
                crash[ny][nx] = next_crash
                heapq.heappush(q, (next_crash, (nx, ny)))

n = int(input())
board = []
for _ in range(n):
    tmp = []
    input_data = input()
    for i in input_data:
        if i != '\n':
            tmp.append(int(i))
    board.append(tmp)

crash = [[INF] * n for _ in range(n)]
dijkstra(0, 0, crash)
print(crash[n-1][n-1])
