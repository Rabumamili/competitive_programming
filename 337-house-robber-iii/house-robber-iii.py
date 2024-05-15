# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
 
        def dp(node):
            if not node:
                return (0, 0)
            
            left_inc, left_exc = dp(node.left)
            right_inc, right_exc = dp(node.right)

            include = node.val + left_exc + right_exc
            
            exclude = max(left_inc, left_exc) + max(right_inc, right_exc)
            
            return (include, exclude)
        
        result = dp(root)
        return max(result)
            
                