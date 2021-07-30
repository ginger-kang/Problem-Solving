def solution(money):
    # 첫 번째 집을 털었을 때 -> 마지막 집을 못털게 됨
    dp = []
    dp.append(money[0])
    dp.append(dp[0])
    for i in range(2, len(money) - 1):
        dp.append(max(dp[i-1], dp[i-2] + money[i]))
    tmp = max(dp)
    
    # 첫 번째 집을 털지 않았을 때
    dp = []
    dp.append(0)
    dp.append(money[1])
    for i in range(2, len(money)):
        dp.append(max(dp[i-1], dp[i-2] + money[i]))
    
    return max(tmp, max(dp))