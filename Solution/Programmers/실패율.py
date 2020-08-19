def solution(N, stages):
    length = len(stages)
    result = []
    for i in range(1, N+1):
        player = stages.count(i)
        if length == 0:
            fail_rate = 0
        else:
            fail_rate = player / length
        result.append((i, fail_rate))
        length -= player
        
    result = sorted(result, key = lambda x: (-x[1], x[0]))
    answer = [i[0] for i in result]
    return answer
