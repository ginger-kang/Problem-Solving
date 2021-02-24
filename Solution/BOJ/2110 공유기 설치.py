import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = []
for _ in range(n):
    data = int(input())
    house.append(data)
house = sorted(house)

maxval = house[-1]
minval = 1

result = 0
while minval <= maxval:
    mid = (minval + maxval) // 2
    tmp = house[0]
    count = 1
    for i in range(1, n):
        if house[i] >= tmp + mid:
            count += 1
            tmp = house[i]
    if count >= c:
        minval = mid + 1
        result = mid
    else:
        maxval = mid - 1
print(result)
