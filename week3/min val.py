class MinStack:

    def __init__(self):
        self.stack = []
        self.length = 0
        self.min = []
        self.mlength = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.length +=1
        if len(self.min) == 0:
            self.min.append(val)
            self.mlength +=1

        elif self.min[self.mlength - 1] >= val:
            self.min.append(val)
            self.mlength +=1


    def pop(self) -> None:
        temp = self.stack[self.length - 1]
        self.stack[self.length - 1] = None
        if temp == self.min[self.mlength - 1]:
            self.min.pop()
            self.mlength -=1

        self.length -= 1

    def top(self) -> int:
        return self.stack[self.length - 1]

    def getMin(self) -> int:
        return self.min[self.length - 1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(3)
obj.push(4)
obj.push(3)
obj.push(2)
obj.push(6)
obj.push(1)



# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()