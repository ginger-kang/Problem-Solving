def sol():
    for i in range(1, n+1):
        temp = 0
        for j in graph[i]:
            temp = max(temp, time[j])
        time[i] += temp

n = int(input())
graph = [[] for _ in range(n+1)]
time = [0] * (n+1)

for i in range(1, n+1):
    input_data = list(map(int, input().split()))
    # 인덱스, 선행작업, 시간
    a, b, c = i, input_data[2:], input_data[0]
    time[a] = c
    for j in b:
        graph[a].append(j)

ans = 0
sol()
print(max(time))
