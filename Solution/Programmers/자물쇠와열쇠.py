import copy

def unlock(m, n, key, lock, tmp_lock):
    k = 0
    while True:
        if k == (n+m-1)**2:
            break
        copy_tmp_lock = copy.deepcopy(tmp_lock)
        x = k % (n+m-1)
        y = k // (n+m-1)
        for i in range(y, y+m):
            for j in range(x, x+m):
                if copy_tmp_lock[i][j] == 1 and key[i-y][j-x] == 1:
                    break
                if copy_tmp_lock[i][j] == 0 and key[i-y][j-x] == 1:
                    copy_tmp_lock[i][j] = 1
                
        result = 0
        for i in range(m-1, n+m-1):
            for j in range(m-1, n+m-1):
                result += copy_tmp_lock[i][j]
    
        if result == n**2:
            return True
        else:
            k+=1
            
    return False

def rotation_key(m, key):
    rotationed = []
    for i in range(m):
        tmp = []
        for j in range(m-1, -1, -1):
            tmp.append(key[j][i])
        rotationed.append(tmp)

    return rotationed

def solution(key, lock):
    n = len(lock)
    m = len(key)
    
    tmp_lock = [[0] * (2*m+n-2) for _ in range(2*m+n-2)]
    for i in range(m-1, n+m-1):
        for j in range(m-1, n+m-1):
            tmp_lock[i][j] = lock[i-(m-1)][j-(m-1)]

    cnt = 0
    while cnt < 5:
        flag = unlock(m, n, key, lock, tmp_lock)
        if flag:
            return True
        key = rotation_key(m, key)
        cnt += 1
            
    return False
