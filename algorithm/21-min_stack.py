class Solution(object):
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, value):
        self.stack.append(value)
        if len(self.minStack) == 0 or value < self.minStack[-1]:
            self.minStack.append(value)
        elif value >= self.minStack[-1]:
            self.minStack.append(self.minStack[-1])

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        assert len(self.minStack) > 0, '没有值,说个球'

        return self.minStack[-1]

s = Solution()
s.push(3)
s.push(2)
s.push(4)
s.push(1)
print(s.min())
s.pop()
print(s.min())