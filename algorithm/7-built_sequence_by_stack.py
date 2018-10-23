class Solution(object):
    '''
    用两个栈实现队列:
    一个栈添加(先进后出)
    当pop时,另外一个栈接受pop出的数据(顺序为后->前),此时pop出的为最前面的数据
    '''
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if len(self.stack2):
            return self.stack2.pop()

        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()