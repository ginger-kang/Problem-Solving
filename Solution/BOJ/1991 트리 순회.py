def pre_order(node):
    print(node.value, end='')
    if node.left != '.':
        pre_order(bt[node.left])
    if node.right != '.':
        pre_order(bt[node.right])

def in_order(node):
    if node.left != '.':
        in_order(bt[node.left])
    print(node.value, end='')
    if node.right != '.':
        in_order(bt[node.right])

def post_order(node):
    if node.left != '.':
        post_order(bt[node.left])
    if node.right != '.':
        post_order(bt[node.right])
    print(node.value, end='')
    
class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

n = int(input())
bt = {}
for _ in range(n):
    node_data = input().split(' ')
    #print(node_data)
    bt[node_data[0]] = Node(node_data[0], node_data[1], node_data[2])

pre_order(bt['A'])
print()
in_order(bt['A'])
print()
post_order(bt['A'])
