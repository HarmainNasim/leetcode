class MinStack:
    def __init__(self):
        self.stack= [] 
        self.min_Stack=[]
    # @param x, an integer
    def push(self, x):
        self.stack.append(x)
        if self.min_Stack:
            self.min_Stack.append(min(x, self.min_Stack[-1]))
        else:
            self.min_Stack.append(x)


    # @return nothing
    def pop(self):
        if self.stack:
            self.stack.pop()
            self.min_Stack.pop()
        else:
            pass
            
    # @return an integer
    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return -1


    # @return an integer
    def getMin(self):
        if self.min_Stack:
            return self.min_Stack[-1]
        else :
            return -1
        

