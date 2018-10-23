class Node(object):
    def __init__(self, value, leftNode=None, rightNode=None):
        self.value = value
        self.leftNode = leftNode
        self.rightNode = rightNode

def serialize(root):
    vals = []

    def doit(node):
        if node:
            vals.append(str(node.value))
            doit(node.leftNode)
            doit(node.rightNode)
        else:
            vals.append('#')

    doit(root)
    return ' '.join(vals)

def deserialize(s):
    def doit():
        val = next(vals)
        if val == '#':
            return None
        node = Node(int(val))
        node.leftNode = doit()
        node.rightNode = doit()
        return node
    vals = iter(s.split())
    return doit()