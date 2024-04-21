# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not k: 
            return [target.val]

        adj_list = defaultdict(list) 

        q = [root]
        while q:
            level = []

            node = q.pop(0)

            if node.right:
                q.append(node.right)
                adj_list[node.right].append(node)
                adj_list[node].append(node.right)
            if node.left:
                q.append(node.left)
                adj_list[node.left].append(node)
                adj_list[node].append(node.left)

        self.sol = []
 
        visited = set([target])
        q = [(target, 0)]
        while q:
            node, distance = q.pop(0)
            if distance == k:
                self.sol.append(node.val)
            else:
                for edge in adj_list[node]:
                    if edge not in visited:
                        visited.add(edge)
                        q.append((edge, distance + 1))
                
        return self.sol
       
 