# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
 
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(node):
            if not node:
                return 0, True
            
            lh, lb = check(node.left)
            rh, rb = check(node.right)
            
            balanced = lb and rb and abs(lh - rh) <= 1
            height = max(lh, rh) + 1
            
            return height, balanced
        
        height, balanced = check(root)
        return balanced