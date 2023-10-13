class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if(not self.stack):
            self.stack.append([val,val])
        else:
            cur_min = min(self.stack[-1][1],val)
            self.stack.append([val,cur_min])


    def pop(self) -> None:
        return self.stack.pop()[0]
        

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
