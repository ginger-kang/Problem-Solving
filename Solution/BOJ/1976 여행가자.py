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
board = []
for _ in range(n):
    input_data = list(map(int, input().split()))
    board.append(input_data)

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i
    
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            union(i+1, j+1)

travel = list(map(int, input().split()))
result = []
for i in travel:
    result.append(find(i))

if len(set(result)) > 1:
    print('NO')
else:
    print('YES')
