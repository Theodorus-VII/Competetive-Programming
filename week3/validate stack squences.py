class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        x=len(popped) - 1
        stack = []
        j = 0
        for i in pushed:
            stack.append(i)
            while (j <= x and len(stack)!=0 and popped[j] == stack[len(stack) - 1]):
                stack.pop()
                j += 1

        if len(stack)==0:
            return True
        return False

x=Solution()
pushed  = [1,0]
popped = [1,0]
x.validateStackSequences(pushed, popped)