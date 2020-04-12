def sol(data, M, k):
    if k == M:
        for i in range(1, len(arr)):
            print(arr[i], end = ' ')
        print(end = '\n')
        return

    for i in range(N):
        if data[i] >= arr[-1]:
            arr.append(data[i])
            sol(data, M, k+1)
            arr.pop()

N, M = map(int, input().split(' '))
data = list(map(int, input(). split(' ')))
arr = [0]

data = sorted(data)

sol(data, M, 0)
