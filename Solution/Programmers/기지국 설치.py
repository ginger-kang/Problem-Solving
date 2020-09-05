import math

def solution(n, stations, w):
    apart = []
    apart.append(stations[0]-w-1)
    for i in range(len(stations)-1):
        apart.append(((stations[i+1]-w-1) - (stations[i]+w+1))+1)
    apart.append(n - (stations[-1]+w))
    
    answer = 0
    for i in apart:
        if i <= 0:
            continue
        answer += math.ceil(i / (w*2+1))
    return answer
