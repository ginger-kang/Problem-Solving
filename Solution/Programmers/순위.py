def solution(n, results):
    wins = {}  # 내가 이긴 선수들
    loses = {}  # 내가 진 선수들
    for i in range(1, n+1):
        wins[i] = set()
        loses[i] = set()
    
    for i in range(1, n+1):
        for result in results:
            if result[0] == i:
                wins[i].add(result[1])
            if result[1] == i:
                loses[i].add(result[0])
        for winner in loses[i]:
            wins[winner].update(wins[i])
        for loser in wins[i]:
            loses[loser].update(loses[i])
    
    ans = 0
    for i in range(1, n+1):
        if len(wins[i]) + len(loses[i]) == n-1:
            ans += 1
    return ans
