class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def in_order(node, level):
    global place
    global idx
    
    if node.left != None:
        in_order(tree[node.left], level + 1)
    place[level].append(idx)
    idx += 1
    if node.right != None:
        in_order(tree[node.right], level + 1)

N = int(input())
tree = {}
place = [[] for _ in range(N)]
idx = 1
parent = [False] * N
for _ in range(N):
    val, left, right = map(int, input().split())
    if left == -1:
        left = None
    else:
        parent[left - 1] = True
    if right == -1:
        right = None
    else:
        parent[right - 1] = True
    tree[val] = Node(val, left, right)

root = parent.index(False) + 1
in_order(tree[root], 0)

max_width = 0
max_level = 0 
for level, nodes in enumerate(place):
    if nodes:
        width = nodes[-1] - nodes[0] + 1
        if max_width < width:
            max_width = width
            max_level = level + 1
            
print(max_level, max_width)
