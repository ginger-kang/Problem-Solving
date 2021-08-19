import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    q = []
    for i in works:
        heapq.heappush(q, -i)
    
    while n > 0:
        maxVal = -heapq.heappop(q)
        maxVal -= 1
        heapq.heappush(q, -maxVal)
        n -= 1
        
    ans = 0
    for _ in range(len(q)):
        val = heapq.heappop(q)
        ans += val ** 2
    
    return ans