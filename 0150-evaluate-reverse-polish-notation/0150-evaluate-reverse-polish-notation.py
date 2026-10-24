class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        
        stack = []
        operands = {"+": operator.add ,
                    "-": operator.sub ,
                    "*": operator.mul , 
                    "/": lambda a,b: int(a/b), }
        
        for i in tokens:
            if i in operands:
                right = stack[-1]
                stack.pop()
                left = stack[-1]
                stack.pop()
                stack.append(operands[i](left, right))
                continue
            stack.append(int(i))
        
        return(stack[0])
