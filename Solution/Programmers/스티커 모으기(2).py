def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    
    dp = []
    dp.append(sticker[0])
    dp.append(dp[0])
    for i in range(2, len(sticker) - 1):
        dp.append(max(dp[i-1], dp[i-2] + sticker[i]))
    
    tmp = max(dp)
    dp = []
    dp.append(0)
    dp.append(sticker[1])
    for i in range(2, len(sticker)):
        dp.append(max(dp[i-1], dp[i-2] + sticker[i]))
    
    return max(tmp, max(dp))