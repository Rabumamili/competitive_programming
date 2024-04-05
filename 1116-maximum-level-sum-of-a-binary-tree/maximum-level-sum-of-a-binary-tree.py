# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        level = 0
        maxi = float("-inf")
        while queue:
            level +=1
            n = len(queue)
            sums = 0
            for i in range(n):
                valu = queue.popleft()
                if valu:
                    sums+=valu.val
                if valu and valu.left:
                    queue.append(valu.left)
                if valu and valu.right:
                    queue.append(valu.right)
            if maxi < sums:
                maxi = sums
                res = level
        return res


