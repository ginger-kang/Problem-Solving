import heapq
import sys

input = sys.stdin.readline

n = int(input())

max_heap = []
min_heap = []
ans = []
for _ in range(n):
    num = int(input())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-num, num))
    else:
        heapq.heappush(min_heap, (num, num))

    if min_heap and max_heap[0][1] > min_heap[0][1]:
        left = heapq.heappop(max_heap)[1]
        right = heapq.heappop(min_heap)[1]
        heapq.heappush(max_heap, (-right, right))
        heapq.heappush(min_heap, (left, left))

    ans.append(max_heap[0][1])

for i in ans:
    print(i)
