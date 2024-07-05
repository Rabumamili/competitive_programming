# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        cP = []
        prev = head
        curr = head.next
        index = 1
        
        while curr and curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or (curr.val < prev.val and curr.val < curr.next.val):
                cP.append(index)
                
            prev = curr
            curr = curr.next
            index += 1
        if len(cP) < 2:
            return [-1, -1]

        minDistance = float('inf')
        for i in range(1, len(cP)):
            minDistance = min(minDistance, cP[i] - cP[i - 1])
        
        maxDistance = cP[-1] - cP[0]
        
        return [minDistance, maxDistance]