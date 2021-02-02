n = int(input())
data = [0]
for _ in range(n):
    input_data = list(map(int, input().split()))
    data.append(input_data)

for day, dt in enumerate(data):
    if dt == 0:
        continue
    t, p = dt
    for i in range(1, day):
        if i + data[i][0] <= day:
            data[day][1] = max(data[day][1], data[i][1] + p)

ans = 0
for day, dt in enumerate(data):
    if dt == 0:
        continue
    t, p = dt
    if day + t > n + 1:
        continue
    ans = max(ans, p)
print(ans)
