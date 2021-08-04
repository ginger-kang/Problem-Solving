def solution(routes):
    routes = sorted(routes, reverse=True)
    ans = 1
    tmp = routes[0][0]
    for i in range(1, len(routes)):
        enter, out = routes[i]
        if tmp <= out:
            continue
        else:
            tmp = enter
            ans += 1
    return ans