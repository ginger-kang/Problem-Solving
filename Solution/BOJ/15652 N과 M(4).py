N, M = map(int, input().split(' '))

def sol(num, check, k):
    if k == M:
        for i in range(1, len(num)):
            print(num[i], end = ' ')
        print(end = '\n')
        return

    for i in range(N):
        if i+1 >= num[-1]:    
            num.append(i+1)
            sol(num, check, k+1)
            num.pop()

num = [0]
result = []
check = [False] * M

sol(num, check, 0)
