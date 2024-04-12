# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        todelete = set(to_delete)
        forest = []
        def dfs(node, todelete, isroot):
            if not node:
                return 
            if node.val in todelete:
                dfs(node.left, todelete, True)
                dfs(node.right, todelete, True)
            else:
                if node.left:
                    if node.left.val in todelete:
                        dfs(node.left,todelete, True)
                        node.left = None
                    else:
                        dfs(node.left, todelete, False)
                if node.right:
                    if node.right.val in todelete:
                        dfs(node.right, todelete, True)
                        node.right = None
                    else:
                        dfs(node.right, todelete, False)
                if isroot:
                    forest.append(node)

        dfs(root, todelete, True)
        return forest
           

        