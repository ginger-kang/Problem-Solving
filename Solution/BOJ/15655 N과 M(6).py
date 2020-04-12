def sol(data, check, M, k):
    if k == M and arr == sorted(arr):
        for i in arr:
            print(i, end = ' ')
        print(end = '\n')
        return

    for i in range(N):
        if check[i] == False:
            arr.append(data[i])
            check[i] = True
            sol(data, check, M, k+1)
            check[i] = False
            arr.pop()

N, M = map(int, input().split(' '))
data = list(map(int, input().split(' ')))
check = [False]*N

arr = []
data = sorted(data)

sol(data, check, M, 0)
