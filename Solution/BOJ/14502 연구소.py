import copy

arr = []
virusList = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
maxVal = 0

def spreadVirus(x, y, copy_arr):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if copy_arr[nx][ny] == 0:
            copy_arr[nx][ny] = 2
            spreadVirus(nx, ny, copy_arr)

def setWall(start, wallCount):
    global maxVal
    
    if wallCount == 3:
        copy_arr = copy.deepcopy(arr)
        for i in range(len(virusList)):
            (virusX, virusY) = virusList[i]
            spreadVirus(virusX, virusY, copy_arr)

        maxVal = max(maxVal, getSafeArea(copy_arr))
        return
        
    for i in range(start, n*m):
        x = i // m
        y = i % m

        if arr[x][y] == 0:
            arr[x][y] = 1
            setWall(i+1, wallCount+1)
            arr[x][y] = 0

def getSafeArea(copy_arr):
    area = 0
    for i in range(n):
        for j in range(m):
            if copy_arr[i][j] == 0:
                area += 1

    return area

if __name__ == "__main__":
    n, m = map(int, input().split(' '))

    for _ in range(n):
        arr.append(list(map(int, input().split(' '))))

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                virusList.append((i,j))

    setWall(0, 0)
    print(maxVal)
    
