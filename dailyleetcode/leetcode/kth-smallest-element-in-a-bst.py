# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.result = None
        self.inorderTraversal(root)
        return self.result

    def inorderTraversal(self, root):
        if root is None:
            return

        self.inorderTraversal(root.left)
        self.k -= 1
        
        if self.k == 0:
            self.result = root.val
            return
        
        self.inorderTraversal(root.right)