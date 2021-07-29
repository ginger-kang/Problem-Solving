def solution(rows, columns, queries):
    board = [[] for _ in range(rows)]
    num = 1
    for i in range(rows):
        for _ in range(columns):
            board[i].append(num)
            num += 1
    
    ans = []
    for query in queries:
        up, left, down, right = query[0]-1, query[1]-1, query[2]-1, query[3]-1
        tmp = board[up][left]
        minval = tmp
        
        for y in range(up, down):
            val = board[y+1][left]
            board[y][left] = val
            minval = min(minval, val)
        
        for x in range(left, right):
            val = board[down][x+1]
            board[down][x] = val
            minval = min(minval, val)
        
        for y in range(down, up, -1):
            val = board[y-1][right]
            board[y][right] = val
            minval = min(minval, val)
        
        for x in range(right, left, -1):
            val = board[up][x-1]
            board[up][x] = val
            minval = min(minval, val)
        
        board[up][left+1] = tmp
        ans.append(minval)
    
    return ans
        