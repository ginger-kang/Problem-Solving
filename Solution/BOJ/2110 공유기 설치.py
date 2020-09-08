n, c = list(map(int, input().split()))
house = []
for _ in range(n):
    house.append(int(input()))
house.sort()

right = house[-1] - house[0]
left = house[1] - house[0]

ans = 0
while left <= right:
    # 공유기 사이의 거리
    mid = (left + right) // 2
    value = house[0]
    count = 1
    for i in house:
        if i >= value + mid:
            count += 1
            value = i
    if count >= c:
        left = mid + 1
        ans = mid
    else:
        right = mid - 1
print(ans)
