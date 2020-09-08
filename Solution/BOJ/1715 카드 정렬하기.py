import heapq

n = int(input())
card = []
for _ in range(n):
    card.append(int(input()))

h = []
for i in card:
    heapq.heappush(h, i)

result = 0
while len(h) >= 2:
    a = heapq.heappop(h)
    b = heapq.heappop(h)

    tmp = a + b
    result += tmp

    heapq.heappush(h, tmp)

print(result)
