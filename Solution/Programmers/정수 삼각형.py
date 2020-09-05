def solution(triangle):
    dp = [[] for _ in range(len(triangle))]
    dp[0].append(triangle[0][0])
    dp[1].append(dp[0][0] + triangle[1][0])
    dp[1].append(dp[0][0] + triangle[1][1])
    for i in range(2, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i].append(dp[i-1][0] + triangle[i][j])
            elif j == len(triangle[i]) - 1:
                dp[i].append(dp[i-1][-1] + triangle[i][j])
            else:
                dp[i].append(max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j])
    
    return max(dp[-1])
