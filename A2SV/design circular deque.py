class MyCircularDeque:

    def __init__(self, k: int):
        self.max = k
        self.data = [None]*self.max
        self.size = 0
        self.rear = 0
        self.front = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull(): return False
        self.front = (self.front - 1 +self.max) % self.max
        self.data[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull(): return False
        self.data[self.rear] = value
        self.rear = (self.rear + 1) % self.max
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty(): return False
        self.data[self.front] = None
        self.front = (self.front + 1) % self.max
        self.size -=1
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty(): return False
        self.rear = (self.rear - 1 +self.max) % self.max
        self.data[self.rear]=None
        self.size -=1
        return True

    def getFront(self) -> int:
        if self.isEmpty(): return -1
        return self.data[self.front]

    def getRear(self) -> int:
        if self.isEmpty(): return -1
        return self.data[self.rear-1]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max