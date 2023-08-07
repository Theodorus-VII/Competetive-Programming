class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.index = 0
        self.deque = dequ

    def insertFront(self, value: int) -> bool:
        pass

    def insertLast(self, value: int) -> bool:
        pass

    def deleteFront(self) -> bool:
        pass

    def deleteLast(self) -> bool:
        pass

    def getFront(self) -> int:
        pass

    def getRear(self) -> int:
        pass

    def isEmpty(self) -> bool:
        pass        


    def isFull(self) -> bool:
        if self.index == self.size:
            return True


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()