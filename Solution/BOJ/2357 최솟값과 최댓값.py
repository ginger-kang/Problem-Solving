import sys
input = sys.stdin.readline

def init_min(idx, start, end):
    if start == end:
        tree_min[idx] = arr[start]
        return tree_min[idx]

    mid = (start+end)//2
    tree_min[idx] = min(init_min(idx*2, start, mid), init_min(idx*2+1, mid+1, end))

    return tree_min[idx]

def init_max(idx, start, end):
    if start == end:
        tree_max[idx] = arr[start]
        return tree_max[idx]

    mid = (start+end)//2
    tree_max[idx] = max(init_max(idx*2, start, mid), init_max(idx*2+1, mid+1, end))

    return tree_max[idx]

def query_min(idx, start, end, left, right):
    if end < left or right < start:
        return int(1e9)
    if left <= start and end <= right:
        return tree_min[idx]

    mid = (start+end)//2
    return min(query_min(idx*2, start, mid, left, right), query_min(idx*2+1, mid+1, end, left, right))

def query_max(idx, start, end, left, right):
    if end < left or right < start:
        return 0
    if left <= start and end <= right:
        return tree_max[idx]

    mid = (start+end)//2
    return max(query_max(idx*2, start, mid, left, right), query_max(idx*2+1, mid+1, end, left, right))

n, m = map(int, input().split())
arr = []
tree_min = [0] * (n*4)
tree_max = [0] * (n*4)
for _ in range(n):
    arr.append(int(input()))

init_min(1, 0, n-1)
init_max(1, 0, n-1)

for _ in range(m):
    a, b = map(int, input().split())
    print(query_min(1, 0, n-1, a-1, b-1), end=' ')
    print(query_max(1, 0, n-1, a-1, b-1))
