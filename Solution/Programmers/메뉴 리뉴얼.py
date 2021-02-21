import itertools

def solution(orders, course):
    result = []
    for i in course:
        menu = {}
        for order in orders:
            order = sorted(list(order))
            comb_order = list(itertools.combinations(order, i))
            for c in comb_order:
                if menu.get(c) == None:
                    menu[c] = 1
                else:
                    menu[c] += 1
        menus = sorted(menu.items(), key = lambda x:x[1], reverse=True)
        if menus:
            maxCnt = menus[0][1]
        for menu in menus:
            if menu[1] < maxCnt:
                break
            if menu[1] == maxCnt and maxCnt >= 2:
                result.append(list(menu[0]))
                
    for i in range(len(result)):
        result[i] = ''.join(result[i])
    
    result_set = set(result)
    return sorted(list(result_set))
