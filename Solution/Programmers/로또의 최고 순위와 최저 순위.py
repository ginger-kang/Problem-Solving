result = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}

def solution(lottos, win_nums):
    ans = [0, 0]
    zero = lottos.count(0)
    count = 0
    
    for lotto in lottos:
        if lotto in win_nums:
            count += 1
    
    ans[0] = result[count + zero]
    ans[1] = result[count]
    
    return ans
