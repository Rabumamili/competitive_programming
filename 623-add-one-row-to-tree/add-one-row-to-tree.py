# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:    
        if depth==1:
            return TreeNode(val, root, None)
        queue=deque([root])
        level = 0
        while queue:
            if level +1  == depth-1:
                break
            n = len(queue)
            for i in range(n):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1

        for node in queue:
            node_left=node.left
            node_right=node.right

            node.left=TreeNode(val, node_left, None)
            node.right=TreeNode(val, None, node_right)

        return root 