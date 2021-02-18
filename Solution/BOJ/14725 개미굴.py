class Node:
    def __init__(self, data=None):
        self.data = data
        self.child = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head
        for s in string:
            if not s in curr_node.child:
                curr_node.child[s] = Node(s)
            curr_node = curr_node.child[s]

    def ant(self, cnt, curr_node):
        if cnt == 0:
            curr_node = self.head
        for child in sorted(curr_node.child.keys()):
            print(cnt * '-' + child)
            self.ant(cnt + 2, curr_node.child[child])

trie = Trie()
n = int(input())
for _ in range(n):
    input_data = input().split()[1:]
    trie.insert(input_data)

trie.ant(0, None)
