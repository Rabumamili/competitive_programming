# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
 
        if not lists:
            return None
        
        def mergeTwoLists(l1, l2):
        
            dummy = ListNode()
            current = dummy
           
            while l1 and l2:
                if l1.val < l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
         
            current.next = l1 if l1 else l2
            
            return dummy.next
      
        def mergeLists(lists, start, end):
            if start == end:
                return lists[start]
            mid = (start + end) // 2
            left = mergeLists(lists, start, mid)
            right = mergeLists(lists, mid + 1, end)
            return mergeTwoLists(left, right)
        
        
        return mergeLists(lists, 0, len(lists) - 1)