import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))

    sum_val = 0
    prev = 0
    length = len(food_times)

    while sum_val + ((q[0][0] - prev) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_val += (now - prev) * length
        length -= 1
        prev = now

    result = sorted(q, key=lambda x:x[1])
    return result[(k - sum_val) % length][1]
