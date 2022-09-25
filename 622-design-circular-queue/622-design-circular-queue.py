class MyCircularQueue:
    def __init__(self, k):
        self.queue = []
        self.size = k
        self.front = 0
        self.rear = 0
    def enQueue(self, value):
        if self.rear - self.front < self.size:
            self.queue.append(value)
            self.rear += 1
            return True
        else:
            return False
    def deQueue(self):
        if self.rear - self.front > 0:
            self.front += 1
            return True
        else:
            return False
    def Front(self):
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.front]
    def Rear(self):
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.rear - 1]
    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.rear - self.front == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()