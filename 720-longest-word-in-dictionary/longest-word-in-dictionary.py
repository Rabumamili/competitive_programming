
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.longest_word = ""
    
    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def dfs(self, node, path):
        # Check if the current node forms a valid word
        if len(path) > len(self.longest_word) or (len(path) == len(self.longest_word) and path < self.longest_word):
            self.longest_word = path

        for char, next_node in node.children.items():
            if next_node.is_end_of_word:
                self.dfs(next_node, path + char)

 
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in sorted(words):
            trie.insert(word)
      
        trie.dfs(trie.root, "")
        
        return trie.longest_word