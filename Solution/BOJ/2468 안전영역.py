import sys
sys.setrecursionlimit(100000)

maxTall = 0

def getSafeArea(x, y, k):
    check[x][y] = True
    for dx, dy in (-1,0),(1,0),(0,-1),(0,1):
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if check[nx][ny] == False and maps[nx][ny] > k:
            getSafeArea(nx, ny, k)
    
if __name__ == "__main__":
    n = int(input())
    maps = [list(map(int, input().split(' '))) for _ in range(n)]
    
    for i in range(n):
        maxTall = max(max(maps[i]), maxTall)

    result = 0
    for k in range(maxTall):
        check = [[False]*n for _ in range(n)]
        safeArea = 0
        for i in range(n):
            for j in range(n):
                if check[i][j] == False and maps[i][j] > k:
                    getSafeArea(i, j, k)
                    safeArea += 1
        
        result = max(result, safeArea)

    print(result)
