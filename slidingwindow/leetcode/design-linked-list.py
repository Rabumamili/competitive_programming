class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.dummy = Node(0)

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.dummy.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        curr = self.dummy.next
        self.dummy.next = Node(val)
        self.dummy.next.next = curr
        self.size += 1

    def addAtTail(self, val: int) -> None:
        curr = self.dummy
        while curr.next:
            curr = curr.next
        curr.next = Node(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        curr = self.dummy
        for _ in range(index):
            curr = curr.next
        temp = curr.next
        curr.next = Node(val)
        curr.next.next = temp
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        curr = self.dummy
        for _ in range(index):
            curr = curr.next
        temp = curr.next
        curr.next = temp.next
        self.size -= 1
