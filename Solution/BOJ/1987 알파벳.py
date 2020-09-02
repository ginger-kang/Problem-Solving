import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]

def alpha():
    global ans
    q = set([(0,0,board[0][0])])
    while q:
        x, y, alphas = q.pop()
        #print(alphas)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if not board[nx][ny] in alphas:
                q.add((nx, ny, alphas + board[nx][ny]))
                ans = max(ans, len(alphas)+1)
            
r, c = map(int, input().split(' '))
board = []
for _ in range(r):
    board.append(input())
    
ans = 1
alpha()
print(ans)
