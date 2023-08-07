class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ['{', '(', '[']
        closing = ['}', ')', ']']

        for i in s:
            if i in opening:
                stack.append(i)
            if i in closing:
                if (i == "}" and stack.pop() != "{"):
                    return False
                if i == ")" and stack.pop() != "(":
                    return False
                if i == "]" and stack.pop() != "[":
                    return False
        
        if len(stack) != 0:
            return False
        return True



x=Solution()
s="()]"
x.isValid(s)