# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: ListNode):
        # Initialize the m x n matrix with -1
        matrix = [[-1] * n for _ in range(m)]
        
        # Spiral traversal boundaries
        top, bottom, left, right = 0, m - 1, 0, n - 1
        
        # Current node in the linked list
        curr = head
        
        # Continue filling the matrix until the list runs out or the matrix is full
        while curr and top <= bottom and left <= right:
            # Move left to right across the top row
            for j in range(left, right + 1):
                if curr:
                    matrix[top][j] = curr.val
                    curr = curr.next
            top += 1
            
            # Move top to bottom down the right column
            for i in range(top, bottom + 1):
                if curr:
                    matrix[i][right] = curr.val
                    curr = curr.next
            right -= 1
            
            # Move right to left across the bottom row
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    if curr:
                        matrix[bottom][j] = curr.val
                        curr = curr.next
                bottom -= 1
            
            # Move bottom to top up the left column
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    if curr:
                        matrix[i][left] = curr.val
                        curr = curr.next
                left += 1
        
        return matrix