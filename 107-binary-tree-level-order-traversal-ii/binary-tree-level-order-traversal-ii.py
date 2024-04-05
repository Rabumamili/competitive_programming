# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        ans = []
        while queue:
            n = len(queue)
            temp = []
            for i in range(n):
                valu = queue.popleft()
                if valu:
                    temp.append(valu.val)
                if valu and valu.left:
                    queue.append(valu.left)
                if valu and valu.right:
                    queue.append(valu.right)
            if temp:
                ans.append(temp)
 
        return ans[::-1]