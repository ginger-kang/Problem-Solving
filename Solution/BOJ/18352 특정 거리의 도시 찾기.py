from collections import deque

n, m, k, x = list(map(int, input().split(' ')))
citys = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split(' '))
    citys[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0
q = deque()
q.append(x)
while q:
    v = q.popleft()
    for e in citys[v]:
        if distance[e] == -1:
            distance[e] = distance[v] + 1
            q.append(e)

flag = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        flag = True

if flag == False:
    print(-1)
