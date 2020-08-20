import sys
sys.setrecursionlimit(10**6)

answer = [[], []]

def pre_order(node):
    global answer
    answer[0].append(node.value)
    if node.left != None:
        pre_order(node.left)
    if node.right != None:
        pre_order(node.right)
        
def post_order(node):
    global answer
    if node.left != None:
        post_order(node.left)
    if node.right != None:
        post_order(node.right)
    answer[1].append(node.value)
                        
class Node:
    def __init__(self, x, y, value):
        self.value = value
        self.x = x
        self.y = y
        self.left = None
        self.right = None

def solution(nodeinfo):
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    nodeinfo = sorted(nodeinfo, key = lambda x: [-x[1], x[0]])
    
    level = 0
    for i in nodeinfo:
        level = max(level, i[1])
    
    level_queue = [[] for _ in range(level+1)]
    for i in nodeinfo:
        level_queue[i[1]].append(i)
    
    root_node = None
    for i in range(len(level_queue)-1, -1, -1):
        while level_queue[i]:
            x, y, idx = level_queue[i].pop(0)
            if root_node == None:
                root_node = Node(x, y, idx)
            else:
                current_node = root_node
                while True:
                    if x < current_node.x:
                        if current_node.left == None:
                            current_node.left = Node(x, y, idx)
                            break
                        else:
                            current_node = current_node.left
                    if x > current_node.x:
                        if current_node.right == None:
                            current_node.right = Node(x, y, idx)
                            break
                        else:
                            current_node = current_node.right
    pre_order(root_node)
    post_order(root_node)
    
    return answer
