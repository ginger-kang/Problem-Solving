def sol(data, check, M, k):
    if k == M:
        if not  in tmp_s:
            for i in arr:
                print(i, end = ' ')
                tmp.append(i)
            tmp.append(' ')
            print()
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
data.sort()
check = [False] * N
arr = []
tmp = []

sol(data,check,M,0)
