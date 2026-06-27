class MinStack:

    def __init__(self):
        self.stack = []
        self.minval = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.minval:
            prev_min = self.minval[-1]
            self.minval.append(min(prev_min, val))

        else:    
            self.minval.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minval.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minval[-1]

        
