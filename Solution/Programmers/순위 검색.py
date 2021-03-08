from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    info_dict = {}
    for i in info:
        information = i.split(' ')
        keys = information[:-1]
        value = int(information[-1])
        for n in range(5):
            key_comb = list(combinations(keys, n))
            for k in key_comb:
                key = ''.join(k)
                if info_dict.get(key) is None:
                    info_dict[key] = [value]
                else:
                    info_dict[key].append(value)
                    
    for key in info_dict.keys():
        info_dict[key] = sorted(info_dict[key])
    
    result = []
    for q in query:
        q = q.replace('and ', '')
        q = q.split(' ')
        q_keys = q[:-1]
        q_value = int(q[-1])
        
        while '-' in q_keys:
            q_keys.remove('-')
        
        q_key = ''.join(q_keys)
        if not q_key in info_dict:
            result.append(0)
        else:
            values = info_dict[q_key]
            #print(values)
            result.append(len(values) - bisect_left(values, q_value))
    
    return result
