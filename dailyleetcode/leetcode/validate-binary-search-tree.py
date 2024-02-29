# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root,mn, maxi):
            if not root:
                return True
        
            if mn!= None and root.val <= mn:
                return False
            if maxi!= None and root.val >= maxi:
                return False

            return validate(root.left,mn,root.val) and validate(root.right,root.val,maxi)

        return validate(root,None,None)