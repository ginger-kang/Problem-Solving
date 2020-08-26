import itertools

def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    
    cases = list(itertools.permutations(dist, len(dist)))
    
    answer = len(dist)+1
    for i in range(length):
        for case in cases:
            count = 1
            current = weak[i] + case[count-1]
            for w in range(i, i+length):
                if weak[w] > current:
                    count += 1
                    if count > len(dist):
                        break
                    current = weak[w] + case[count-1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    else:
        return answer
