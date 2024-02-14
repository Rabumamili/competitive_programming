# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
  def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    Node_a = headA
    Node_b = headB

    while Node_a != Node_b:
        if Node_a:
            Node_a = Node_a.next
        else:
            Node_a = headB
        if Node_b:
            Node_b = Node_b.next 
        else:
            Node_b= headA

    return Node_b
