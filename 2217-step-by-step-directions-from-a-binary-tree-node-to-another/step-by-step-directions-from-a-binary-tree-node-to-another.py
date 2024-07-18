class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        #find the LCA of two nodes
        def findLCA(node, p, q):
            if not node or node.val == p or node.val == q:
                return node
            left = findLCA(node.left, p, q)
            right = findLCA(node.right, p, q)
            if left and right:
                return node
            return left if left else right

        # Helper function to find the path from a node to a given value
        def findPath(node, value, path):
            if not node:
                return False
            if node.val == value:
                return True
            path.append('L')
            if findPath(node.left, value, path):
                return True
            path.pop()
            path.append('R')
            if findPath(node.right, value, path):
                return True
            path.pop()
            return False

        lca = findLCA(root, startValue, destValue)
        
        start_path = []
        dest_path = []
        
        findPath(lca, startValue, start_path)
        findPath(lca, destValue, dest_path)
        
        # Convert the start path to "U" moves
        up_moves = 'U' * len(start_path)
        
        # Join the up moves with the destination path
        return up_moves + ''.join(dest_path)
