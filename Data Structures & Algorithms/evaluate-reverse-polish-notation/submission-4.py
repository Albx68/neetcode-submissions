class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operands = []
        operations = '+-/*'
        for t in tokens:
            if t in operations:
                b = operands.pop()
                a = operands.pop()

                if t == '+':
                    c = a+b
                elif t == '-':
                    c = a-b
                elif t == '/':
                    c = a/b
                else:
                    c=a*b
                operands.append(int(c))
            else:
                operands.append(int(t))
        
        return operands[-1]