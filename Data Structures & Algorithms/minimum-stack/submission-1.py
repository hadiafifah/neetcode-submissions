class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    ## Core logic for getMin
    # append val to top of stack and if minstack is not empty, get
    # the minimum value between the last minimum from the minStack and the current
    # this compares the top of the stack with the top of minStack
    # where minStack is simply the last min value each time a value is
    # added to the stack
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            val = min(val, self.minStack[-1])

        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:  
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


