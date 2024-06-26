# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        lst = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            lst.append(root.val)
            inorder(root.right)
        
        inorder(root)
        def build_tree(tree_lst):
            if not tree_lst:
                return
            idx = len(tree_lst) // 2
            val = tree_lst[idx]
            
            node = TreeNode(val)
            node.left = build_tree(tree_lst[0:idx])
            node.right = build_tree(tree_lst[idx+1:])
            return node
        return build_tree(lst)