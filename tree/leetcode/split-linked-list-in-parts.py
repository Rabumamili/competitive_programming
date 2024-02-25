# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
   
        # Count the length of the linked list
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        
         
        part_size, remainder = length//k, length%k
        
        # Split the linked list into k parts
        result = []
        current = head
        for i in range(k):
            part_head = current
            part_length = part_size + (1 if i < remainder else 0)
            
            for j in range(part_length - 1):
                if current:
                    current = current.next
            
            if current:
                next_node = current.next
                current.next = None
                current = next_node
            
            result.append(part_head)
        
        return result
 
