def sol(t, k):
    if k == m:
        a = ''
        for i in tmp:
            a += str(i) + ' '
        if a not in b:
            b.append(a)
        return
    
    for i in range(n):
        if visit[i] == 0:
            if arr[i] >= t:
                visit[i] = 1
                t = arr[i]
                tmp[k] = arr[i]
                sol(t, k+1)
                visit[i] = 0
            


n, m = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
arr = sorted(arr)
visit = [False] * n
tmp = [0] * m
b = []

sol(0,0)

for i in b:
    print(i.rstrip())
    
