def sol(y,x):
    global cnt
    color = ['B', 'W']
    idx = 0
    
    for i in range(y, y+7):
        for j in range(x, x+7):
            if board[i][j] != color[idx]:
                idx = (idx%2)-1
        

for i in range(n):
    for j in range(m):
        if j+7 < m and i+7 < c:
            sol(i, j)

n, m = map(int, input().split(' '))
board = [input() for_ in range(n)]
    
