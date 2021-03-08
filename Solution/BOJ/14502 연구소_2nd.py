import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(count):
    global result
    
    if count == 3:
        for i in range(n):
            for j in range(m):
                tmp[i][j] = board[i][j]
        for i in range(n):
            for j in range(m):
                if tmp[i][j] == 2:
                    spread_virus(j, i)
        result = max(result, get_safe_area())
        return
        
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] += 1
                count += 1
                dfs(count)
                board[i][j] -= 1
                count -= 1
                

def spread_virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < m and ny >= 0 and ny < n:
            if tmp[ny][nx] == 0:
                tmp[ny][nx] = 2
                spread_virus(nx, ny)
    
def get_safe_area():
    count = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                count += 1
    return count

n, m = map(int, input().split())
board = []
result = 0
for _ in range(n):
    input_data = list(map(int, input().split()))
    board.append(input_data)
tmp = [[0] * m for _ in range(n)]
dfs(0)
print(result)
