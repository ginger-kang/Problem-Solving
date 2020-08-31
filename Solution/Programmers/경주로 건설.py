from collections import deque

# 동남북서
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
    
def racing(n, x, y, board, cost, direction):
    cost[y][x] = 0
    q = deque()
    q.append((0,x,y,0))
    q.append((0,x,y,1))
    while q:
        curr_cost, x, y, d = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            next_cost = 0
            if nx < 0 or ny < 0 or nx >= n or ny >= n or board[ny][nx] == 1:
                continue
            if i == d:
                new_cost = 100
            else:
                new_cost = 600
            next_cost = new_cost + curr_cost
            if cost[ny][nx] == -1 or cost[ny][nx] >= next_cost:
                cost[ny][nx] = next_cost
                q.append((next_cost, nx, ny, i))
    
def solution(board):
    n = len(board)
    cost = [[-1] * n for _ in range(n)]
    racing(n, 0, 0, board, cost, 0)
    print(cost)
    return cost[n-1][n-1]
