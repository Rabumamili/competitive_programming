# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def calculateSum(root, curSum):
            if root is None:
                return 0

            curSum = curSum * 10 + root.val

            if root.left is None and root.right is None:
                return curSum

            return calculateSum(root.left, curSum) + calculateSum(root.right, curSum)

        return calculateSum(root, 0)