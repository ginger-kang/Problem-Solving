import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

result = []
p_a = 0
p_b = 0
while p_a < len(a) and p_b < len(b):
    if a[p_a] < b[p_b]:
        result.append(a[p_a])
        p_a += 1
    else:
        result.append(b[p_b])
        p_b += 1

if p_b == len(b):
    result += a[p_a:]
elif p_a == len(a):
    result += b[p_b:]

print(" ".join(map(str, result)))
