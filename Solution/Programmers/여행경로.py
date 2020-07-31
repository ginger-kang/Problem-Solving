def travel(tickets):
    t_dict = {}
    for ticket in tickets:
        if ticket[0] in t_dict:
            t_dict[ticket[0]].append(ticket[1])
        else:
            t_dict[ticket[0]] = [ticket[1]]
    
    tmp = ['ICN']
    result = []
    while tmp:
        if tmp[-1] in t_dict and len(t_dict[tmp[-1]]) > 0:
            tmp.append(t_dict[tmp[-1]].pop())
        else:
            result.append(tmp.pop())
    result.reverse()
    return result
    
def solution(tickets):
    tickets = sorted(tickets, reverse=True)
    ans = travel(tickets)
    return ans
