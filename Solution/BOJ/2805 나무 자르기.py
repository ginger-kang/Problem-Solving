n, m = map(int, input().split(' '))
tree = list(map(int, input().split(' ')))

left = 0
right = max(tree)
result = 0
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for t in tree:
        if t > mid:
            cnt += (t - mid)
    if cnt < m:
        right = mid - 1
    else:
        result = mid
        left = mid + 1
print(result)
