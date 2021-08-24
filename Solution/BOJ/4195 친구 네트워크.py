def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]

    print(number[x])


t = int(input())
for _ in range(t):
    f = int(input())
    parent = {}
    number = {}

    for _ in range(f):
        a, b = input().split(" ")
        if parent.get(a) is None:
            parent[a] = a
            number[a] = 1
        if parent.get(b) is None:
            parent[b] = b
            number[b] = 1

        union(a, b)
