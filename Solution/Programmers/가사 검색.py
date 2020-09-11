class Node:
    def __init__(self, data=None):
        self.data = data
        self.child = {}
        self.length = {}

class Trie:
    def __init__(self):
        self.head = Node(None)
        
    def insert(self, string):
        curr_node = self.head
        length = len(string)
        
        if not length in curr_node.length:
            curr_node.length[length] = 1
        else:
            curr_node.length[length] += 1
            
        for char in string:
            if not char in curr_node.child:
                curr_node.child[char] = Node(char)
            curr_node = curr_node.child[char]
            length -= 1
            if not length in curr_node.length:
                curr_node.length[length] = 1
            else:
                curr_node.length[length] += 1
    
    def search(self, query, wild):
        curr_node = self.head
        
        for char in query:
            if char in curr_node.child:
                curr_node = curr_node.child[char]
            else:
                return 0
        
        if not wild in curr_node.length:
            return 0
        else:
            return curr_node.length[wild]
    
        
def solution(words, queries):
    pre_trie = Trie()
    inv_trie = Trie()
    
    for i in words:
        pre_trie.insert(i)
        inv_trie.insert(i[::-1])
    
    result = []
    for q in queries:
        if q[0] != '?':
            question = q.find('?')
            query = q[:question]
            wild = len(q[question:])
            result.append(pre_trie.search(query, wild))
        else:
            q = q[::-1]
            question = q.find('?')
            query = q[:question]
            wild = len(q[question:])
            result.append(inv_trie.search(query, wild))
    
    return result
