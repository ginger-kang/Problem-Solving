import sys
input = sys.stdin.readline

def init(idx, start, end):
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]
    mid = (start+end)//2
    tree[idx] = init(idx*2, start, mid) + init(idx*2+1, mid+1, end)

    return tree[idx]

def query(idx, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[idx]

    mid = (start+end)//2
    return query(idx*2, start, mid, left, right) + query(idx*2+1, mid+1, end, left, right)

def update(idx, start, end, k, diff):
    if k < start or k > end:
        return

    tree[idx] += diff
    
    if start != end:
        mid = (start+end)//2
        update(idx*2, start, mid, k, diff)
        update(idx*2+1, mid+1, end, k, diff)

n, m, k = map(int, input().split())
arr = []
tree = [0] * 4000000
for _ in range(n):
    arr.append(int(input()))

init(1, 0, n-1)
for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        b -= 1
        diff = c - arr[b]
        arr[b] = c
        update(1, 0, n-1, b, diff)
    else:
        print(query(1, 0, n-1, b-1, c-1))
               
