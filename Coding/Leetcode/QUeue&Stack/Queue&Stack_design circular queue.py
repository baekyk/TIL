class MyCircularQueue:

    def __init__(self, k: int):
        self.circular = []
        self.head = 0
        self.lenth = k
        
    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.circular.append(value)
        return True

        
    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.head +=1
        return True

    def Front(self) -> int:
        if self.isEmpty() : return -1
        return self.circular[self.head]

    def Rear(self) -> int:
        if self.isEmpty() : return -1
        return self.circular[len(self.circular)-1]

    def isEmpty(self) -> bool:
        return len(self)==0

    def isFull(self) -> bool:
        return len(self)==self.lenth
    
    def __len__(self):
        return len(self.circular) - self.head


class MyCircularQueue2:

    def __init__(self, k: int):
        self.circular = [None]*k
        self.head = 0
        self.tail = 0
        
    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.circular[self.tail] = value
        self.tail = (self.tail + 1) % len(self.circular)
        return True

        
    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.circular[self.head] = None
        self.head = (self.head + 1) % len(self.circular)
        return True

    def Front(self) -> int:
        if self.isEmpty() : return -1
        return self.circular[self.head]

    def Rear(self) -> int:
        if self.isEmpty() : return -1
        return self.circular[self.tail-1]

    def isEmpty(self) -> bool:
        return self.head == self.tail and self.circular[self.head] is None

    def isFull(self) -> bool:
        return self.head == self.tail and self.circular[self.head] is not None