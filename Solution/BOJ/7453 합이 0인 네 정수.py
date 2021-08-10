import sys
input = sys.stdin.readline

n = int(input())
A, B, C, D = [], [], [], []

for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB, CD = {}, {}
for a in A:
    for b in B:
        if AB.get(a+b) is None:
            AB[a+b] = 1
        else:
            AB[a+b] += 1

ans = 0
for c in C:
    for d in D:
        ans += AB.get(-(c+d), 0)

print(ans)
