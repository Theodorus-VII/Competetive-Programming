class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ['{', '(', '[']
        closing = ['}', ')', ']']

        for i in s:
            if i in opening:
                stack.append(i)
            elif i in closing:
                if len(stack) == 0:
                    return False
                if (i == "}" and stack.pop() != "{"):
                    return False
                if i == ")" and stack.pop() != "(":
                    return False
                if i == "]" and stack.pop() != "[":
                    return False
            
        if len(stack) != 0:
            return False
        return True