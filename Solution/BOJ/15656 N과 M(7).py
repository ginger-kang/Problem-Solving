def sol(data, M, k):
    if k == M:
        for i in arr:
            print(i, end = ' ')
        print(end = '\n')
        return

    for i in range(N):
        arr.append(data[i])
        sol(data, M, k+1)
        arr.pop()

N, M = map(int, input().split(' '))
data = list(map(int, input(). split(' ')))
arr = []

data = sorted(data)

sol(data, M, 0)
