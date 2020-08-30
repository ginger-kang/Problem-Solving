def sol(n, r, c):
    global count
    
    # 최소단위(배열 원소 하나씩 검사할 때)
    if n == 2:
        if r == x and c == y:
            print(count)
            return
        count += 1
        if r == x and c+1 == y:
            print(count)
            return
        count += 1
        if r+1 == x and c == y:
            print(count)
            return
        count += 1
        if r+1 == x and c+1 == y:
            print(count)
            return
        count += 1
        return
        
    sol(n//2, r, c)
    sol(n//2, r, c+n//2)
    sol(n//2, r+n//2, c)
    sol(n//2, r+n//2, c+n//2)

n, x, y = map(int, input().split())
count = 0
sol(2**n, 0, 0)

