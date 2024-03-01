# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
 
        column_nodes = {}

        # Perform a depth-first search to populate the hashmap
        def dfs(node, row, column):
            if node is None:
                return
            if column in column_nodes:
                column_nodes[column].append((row, node.val))
            else:
                column_nodes[column] = [(row, node.val)]
            dfs(node.left, row + 1, column - 1)
            dfs(node.right, row + 1, column + 1)

        
        dfs(root, 0, 0)

        # Sort the nodes within each column based on their row values
        sorted_columns = sorted(column_nodes.keys())
        result = []
        for column in sorted_columns:
            sorted_nodes = sorted(column_nodes[column], key=lambda x: (x[0], x[1]))
            result.append([val for i, val in sorted_nodes])

        return result