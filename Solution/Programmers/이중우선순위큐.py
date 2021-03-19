import heapq

def solution(operations):
    maxheap = []
    minheap = []
    for op in operations:
        cmd, data = op.split()
        if cmd == 'I':
            num = int(data)
            heapq.heappush(minheap, num)
            heapq.heappush(maxheap, (-num, num))
        else:
            if not minheap:
                continue
            if data == '1':
                maxVal = heapq.heappop(maxheap)[1]
                minheap.remove(maxVal)
            else:
                minVal = heapq.heappop(minheap)
                maxheap.remove((-minVal, minVal))
    #print(maxheap, minheap)
    if not maxheap or not minheap:
        return [0, 0]
    else:
        return [maxheap[0][1], minheap[0]]
