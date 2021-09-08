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

n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges = sorted(edges)

result = 0
max_cost = 0
for edge in edges:
    c, a, b = edge
    if find(a) != find(b):
        union(a, b)
        result += c
        max_cost = c

print(result - max_cost)
