def find(parent, x):
    if parent[x] != x:
        return find(parent, parent[x])
    return parent[x]
    
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    parent = [0] * (n+1)
    for i in range(1, n+1):
        parent[i] = i
    
    costs = sorted(costs, key=lambda x:x[2])
        
    ans = []
    for cost in costs:
        a, b, c = cost
        parent_a = find(parent, a)
        parent_b = find(parent, b)
        if parent_a == parent_b:
            continue
        else:
            ans.append(c)
            if len(ans) == n-1:
                return sum(ans)
            union(parent, a, b)
            
    return sum(ans)
