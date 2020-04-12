N, M = map(int, input().split(' '))
num = []
result = []
check = [False] * M
def sol(num, check, k, cnt):
    if k == M:
        for i in num:
            print(i, end = ' ')
        print(end = '\n')
        return

    for i in range(N):
            num.append(i+1)
            sol(num, check, k+1, cnt+1)
            num.pop()

sol(num, check, 0, 0)
