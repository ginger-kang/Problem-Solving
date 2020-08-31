n, m = map(int, input().split(' '))
setA = set()
setB = set()
for _ in range(n):
    setA.add(input())
for _ in range(m):
    setB.add(input())

result = list(setA&setB)
print(len(result))
for i in sorted(result):
    print(i)
