class MyCircularQueue:
 
    def __init__(self, k):
        self.queue = [None] * k
        self.max_size = k
        self.front = -1
        self.rear = -1

    def enQueue(self, value):
        if self.isFull():
            return False
        elif self.isEmpty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = value
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        elif self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self):
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self):
        return self.front == -1 and self.rear == -1

    def isFull(self):
        return (self.rear + 1) % self.max_size == self.front


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()