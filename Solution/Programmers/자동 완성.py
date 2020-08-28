class Node:
    def __init__(self, char, data = None):
        self.char = char
        self.data = data
        self.count = 0
        self.next = {}

class Trie:
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        current_node = self.head
        for char in string:
            current_node.count += 1
            if char not in current_node.next:
                current_node.next[char] = Node(char)
            current_node = current_node.next[char]
        current_node.data = string
        current_node.count += 1
    
    def search(self, string):
        current_node = self.head
        
        for char in string:
            if char in current_node.next:
                current_node = current_node.next[char]
            else:
                return False
        
        if current_node.count == 1:
            return True
        else:
            return False

def solution(words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    answer = 0
    for word in words:
        flag = False
        for i in range(1, len(word)+1):
            if trie.search(word[:i]):
                answer += len(word[:i])
                flag = True
                break
        
        if not flag:
            answer += len(word)
    return answer
