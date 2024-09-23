# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
 

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
         
        def dfs_tree(tree_node, list_node):
            if list_node is None:
                return True   
            if tree_node is None:
                return False   
           
            if tree_node.val == list_node.val:
                return dfs_tree(tree_node.left, list_node.next) or dfs_tree(tree_node.right, list_node.next)
            
            return False   
 
        def dfs(tree_node):
            if tree_node is None:
                return False
            
           
            if dfs_tree(tree_node, head):
                return True
            
             
            return dfs(tree_node.left) or dfs(tree_node.right)

        
        return dfs(root)
