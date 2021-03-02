k, n = map(int, input().split())
lan = []
for _ in range(k):
    lan.append(int(input()))

start = 1
end = max(lan)

result = 0
while start <= end:
    tmp = 0
    mid = (start + end) // 2
    for l in lan:
        tmp += (l // mid)
    if tmp < n:
        end = mid - 1
    else:
        start = mid + 1
        result = mid

print(result)
