class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        clopen = { ")":"(", "}":"{", "]":"[" }

        for i in s:
            if i in clopen:
                if stack and stack[-1] == clopen[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        if not stack:
            return True
        else:
            return False

