# class Solution:
#     def evalRPN(self, tokens) -> int:
#         ops = ['*', '+', '-', '/']
#         n = len(tokens)
#         i = 0
#         while i < n:
#             if tokens[i] in ops:
#                 tokens [i] = tokens[i-2] + tokens[i] + tokens[i-1]
#                 tokens [i] = str(int(eval(tokens [i])))
#                 tokens.pop(i-1)
#                 tokens.pop(i-2)
#                 i -= 2
#                 n -= 2
#             i += 1
        # return int(float(tokens[0]))


class Solution:
    def evalRPN(self, tokens) -> int:
        ops = ['*', '+', '-', '/']
        
        stack = []

        for i in tokens:
            if i in ops:
                x = stack.pop()
                res = str(int(eval(stack.pop() + i + x)))
                stack.append(res)
                continue
            
            stack.append(i)

        return(int(stack[0]))




