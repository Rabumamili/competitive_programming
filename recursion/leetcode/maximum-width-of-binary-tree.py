# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    
        def backtrack(node, level, position, left):
            if not node:
                return 0
            
            if level >= len(left):
                left.append(position)
            else:
                left[level] = min(left[level], position)
            
            return max(position - left[level] + 1,
                    backtrack(node.left, level + 1, position * 2, left),
                    backtrack(node.right, level + 1, position * 2 + 1, left))
        
        return backtrack(root, 0, 0, [])