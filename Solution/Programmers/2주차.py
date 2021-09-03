def check(arr, target):
    result = arr.count(target)
    if result > 1:
        return False
    return True


def solution(board):
    n = len(board)
    scores = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            scores[j].append(board[i][j])

    avgs = []
    for i in range(n):
        max_val = max(scores[i])
        min_val = min(scores[i])
        tmp = 0
        cnt = 0
        for j in range(n):
            if i == j:
                if scores[i][j] == max_val and check(scores[i], max_val):
                    continue
                if scores[i][j] == min_val and check(scores[i], min_val):
                    continue
            tmp += scores[i][j]
            cnt += 1
        avgs.append(tmp / cnt)

    ans = ""
    for avg in avgs:
        if avg >= 90:
            ans += "A"
        elif avg >= 80:
            ans += "B"
        elif avg >= 70:
            ans += "C"
        elif avg >= 50:
            ans += "D"
        else:
            ans += "F"

    return ans
