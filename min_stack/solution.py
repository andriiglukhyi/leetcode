class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.bucket = []
        self.min = None
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.bucket.append([x, self.min])
        if self.min is None:
            self.min = x
        elif x < self.min:
            self.min = x

    def pop(self):
        """
        :rtype: void
        """
        x = self.bucket.pop()
        if x[0] == self.min:
            self.min = x[1]
        

    def top(self):
        """
        :rtype: int
        """
        return self.bucket[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()