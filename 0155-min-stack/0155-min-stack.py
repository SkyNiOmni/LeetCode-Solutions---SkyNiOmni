class MinStack:

    def __init__(self):
        self.stack = []
        self.sort = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.sort:
            self.sort.append(value)
        elif self.sort[-1] >= value:
            self.sort.append(value)

    def pop(self) -> None:
        if self.sort:
            if self.stack[-1] == self.sort[-1]:
                self.sort.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return(self.stack[-1])

    def getMin(self) -> int:
        if self.sort:
            return(self.sort[-1])
        else:
            return(None)


        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()