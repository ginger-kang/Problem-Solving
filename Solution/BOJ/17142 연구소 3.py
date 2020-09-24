from collections import deque
import itertools
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def spread(virus):
    global ans
    
    q = deque()
    visited = [[-1] * n for _ in range(n)]
    for i in virus:
        q.append(i)
        visited[i[0]][i[1]] = 0
    new_board = copy.deepcopy(board)
    max_val = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n or new_board[nx][ny] == 1:
                continue
            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                if new_board[nx][ny] == 0:
                    max_val = max(max_val, visited[nx][ny])
                q.append((nx,ny))

    if check(visited):
        ans.append(max_val)

def check(board):
    count = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == -1:
                count += 1
    if count == wall_count:
        return True
    else:
        return False

n, m = map(int, input().split(' '))
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

virus = []
ans = []
wall_count = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            virus.append((i, j))
        if board[i][j] == 1:
            wall_count += 1

select_virus = list(itertools.combinations(virus, m))
result = int(1e9)
for i in select_virus:
    spread(i)

if not ans:
    print(-1)
else:
    for i in ans:
        if i != -1:
            result = min(result, i)
    print(result)
        
