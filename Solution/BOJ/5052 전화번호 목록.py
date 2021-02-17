import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data=None):
        self.data = data
        self.child = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head
        for ch in string:
            if ch not in curr_node.child:
                curr_node.child[ch] = Node(ch)
            curr_node = curr_node.child[ch]
        curr_node.data = string

    def search(self, string):
        curr_node = self.head
        for ch in string:
            if ch in curr_node.child:
                curr_node = curr_node.child[ch]
        if len(curr_node.child) != 0:
            return False
        return True

t = int(input())
for _ in range(t):
    n = int(input())
    trie = Trie()
    phone = []
    for _ in range(n):
        phone_number = input().strip()
        phone_number.replace(" ", "")
        trie.insert(phone_number)
        phone.append(phone_number)

    flag = True
    for p in phone:
        if not trie.search(p):
            flag = False

    if flag:
        print('YES')
    else:
        print('NO')
    
