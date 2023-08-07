class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = []
        rev = []

        for i in s:
            if i == ")":
                x = stack.pop()
                while x != "(":
                    rev.append(x)
                    x = stack.pop()
                stack += rev
                rev = []
            else: 
                stack.append(i)
        return ''.join(stack)



x = Solution()
s= "wnb(((z()qw)eyt)(bx(()ye)))"
print(x.reverseParentheses(s))