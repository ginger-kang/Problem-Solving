def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
m = int(input())
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

computers = []
for _ in range(m):
    a, b, c = map(int, input().split())
    computers.append((c, a, b))

computers = sorted(computers)

ans = 0
for computer in computers:
    c, a, b = computer
    if find(a) != find(b):
        ans += c
        union(a, b)

print(ans)
