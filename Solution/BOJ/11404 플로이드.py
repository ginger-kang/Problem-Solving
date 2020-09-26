INF = int(1e9)

n = int(input())
m = int(input())
bus = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            bus[i][j] = 0

for _ in range(m):
    a, b, cost = map(int, input().split(' '))
    if cost < bus[a][b]:
        bus[a][b] = cost

'''
for i in range(1, n+1):
    for j in range(1, n+1):
        print(bus[i][j], end=' ')
    print()
'''

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            bus[i][j] = min(bus[i][j], bus[i][k] + bus[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if bus[i][j] == INF:
            print(0, end=' ')
        else:
            print(bus[i][j], end=' ')
    print()
