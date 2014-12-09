class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        #pay attention that here should be x <= instead of x <. We should NOT ignore duplicates, otherwise pop() will cause errors
        if len(self.minstack) == 0 or x <= self.minstack[-1]:
            self.minstack.append(x)

    # @return nothing
    def pop(self):
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        self.stack.pop()

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        return self.minstack[-1]
        