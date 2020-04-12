def keisyaro(x):
    for i in range(N):
        visited = [False] * N
        current_height = 0
        prev_height = 0
        
        for j in range(N):
            prev_height = current_height
            current_height = maps[i][j]
            height = current_height - prev_height
            
            if height == 0:
                continue
            elif height == 1:
                


N, L = map(int, input(). split(' '))
for _ in range(N):
    maps = list(map(int, input().split(' ')))

cnt = 0
for i in range(N):
    cnt += keisyaro_col(i)
