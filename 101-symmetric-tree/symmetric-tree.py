# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        def Helper(root1, root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None:
                return False
            if root1.val != root2.val:
                return False
            return (Helper(root1.left, root2.right) and
                    Helper(root1.right, root2.left))

        if root is None:
            return True

        return Helper(root.left, root.right)