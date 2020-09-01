import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split(' '))

result = 0
for i in range(n):
    if a[i] > 0:
        a[i] -= b
        result += 1

    if a[i] > 0:
        result += int(a[i]/c)   
        if a[i] % c != 0:
            result += 1

print(result)
