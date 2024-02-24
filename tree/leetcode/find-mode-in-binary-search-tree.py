# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        self.modes = []
        self.current_val = None
        self.current_count = 0
        self.max_count = 0
 
        def inorder_traversal(node):
            nonlocal self
            if node:
                inorder_traversal(node.left)

                # Process current node's value
                if node.val == self.current_val:
                    self.current_count += 1
                else:
                    self.current_val = node.val
                    self.current_count = 1

                # Update mode information
                if self.current_count == self.max_count:
                    self.modes.append(node.val)
                elif self.current_count > self.max_count:
                    self.max_count = self.current_count
                    self.modes = [node.val]

                inorder_traversal(node.right)

        # Start in-order traversal
        inorder_traversal(root)

        return self.modes