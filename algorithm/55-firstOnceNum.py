class Solution(object):
    def __init__(self):
        self.memory = {}
        self.queue = []

    def insertStr(self, s):
        for char in s:
            self.insert(char)

    def firstAppearingOnce(self):
        while len(self.queue) and self.memory[self.queue[0]] > 1:
            self.queue.pop(0)
        return self.queue[0] if len(self.queue) else '#'

    def insert(self, char):
        number = self.memory.get(char, 0)
        self.memory[char] = number + 1
        if self.memory[char] == 1:
            self.queue.append(char)

s = Solution()
s.insertStr('google')
print(s.firstAppearingOnce())