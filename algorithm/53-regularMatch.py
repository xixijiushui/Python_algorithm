class Solution(object):
    def __init__(self):
        self.dic = {}

    def match(self, s, p):
        if (s, p) in self.dic:
            return self.dic[(s, p)]

        if p == '':
            return s == ''

        if len(p) == 1 or p[1] != '*':
            self.dic[(s[1:], p[1:])] = self.match(s[1:], p[1:])
            return len(s) > 0 and (p[0] == '.' or p[0] == s[0]) and self.dic[(s[1:], p[1:])]

        while len(s) and (p[0] == '.' or p[0] == s[0]):
            self.dic[s, p[2:]] = self.match(s, p[2:])
            if self.match(s[:], p[2:]):
                return True
            s = s[1:]
        self.dic[s, p[2:]] = self.match(s, p[2:])
        return self.dic[(s, p[2:])]

s = Solution()
print(s.match('bbbbbabc', 'b*b.bc'))