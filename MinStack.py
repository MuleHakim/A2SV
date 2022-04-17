class MinStack:

    def __init__(self):
        self.myStack = []

    def push(self, val: int) -> None:
        self.myStack.append(val)

    def pop(self) -> None:
        self.myStack.pop()

    def top(self) -> int:
        return self.myStack[-1]

    def getMin(self) -> int:
        
        return min(self.myStack)
