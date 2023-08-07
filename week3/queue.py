class MyQueue:

    def __init__(self):
        self.queue = []
        self.index = 0
        self.length = 0

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.length += 1

    def pop(self) -> int:
        if self.empty():
            return
        temp = self.queue[self.index]
        self.queue[self.index] = None
        self.index += 1
        return temp

    def peek(self) -> int:
        temp = self.queue[self.index]
        return temp

    def empty(self) -> bool:
        if self.index >= self.length:
            return True


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
x = 1
obj.push(x)
param_2 = obj.pop()
#param_3 = obj.peek()
#param_4 = obj.empty()