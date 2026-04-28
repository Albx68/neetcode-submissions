class Solution:
    def isValid(self, s: str) -> bool:
        closingtoopen = {'}':'{',']':'[',')':'('}
        stack = []
        for c in s:
            if c in closingtoopen:
                if stack and stack[-1] == closingtoopen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
