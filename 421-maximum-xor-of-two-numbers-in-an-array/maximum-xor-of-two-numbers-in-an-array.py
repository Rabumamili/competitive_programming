class TrieNode:
    def __init__(self):
        self.left = None  # bit 0
        self.right = None  # bit 1

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # Build the Trie
        root = TrieNode()
        for num in nums:
            node = root
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if bit == 0:
                    if not node.left:
                        node.left = TrieNode()
                    node = node.left
                else:
                    if not node.right:
                        node.right = TrieNode()
                    node = node.right

        # Find the maximum XOR
        max_xor = 0
        for num in nums:
            node = root
            xor = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if bit == 0:
                    if node.right:
                        node = node.right
                        xor |= (1 << i)
                    else:
                        node = node.left
                else:
                    if node.left:
                        node = node.left
                        xor |= (1 << i)
                    else:
                        node = node.right
            max_xor = max(max_xor, xor)

        return max_xor