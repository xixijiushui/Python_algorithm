class Node(object):
    def __init__(self, value, leftNode=None, rightNode=None):
        self.value = value
        self.leftNode = leftNode
        self.rightNode = rightNode

def kthNode(pRoot):
    if pRoot == None or k == 0:
        return None

    return kthNodeCore(pRoot)

k = 5

def kthNodeCore(pRoot):
    global k
    target = None
    if pRoot.leftNode != None:
        target = kthNodeCore(pRoot.leftNode)

    if target == None:
        if k == 1:
            target = pRoot
        k -= 1
    if target == None and pRoot.rightNode != None:
        target = kthNodeCore(pRoot.rightNode)
    return target

rootNode = Node(5)
node3 = Node(3)
node2 = Node(2)
node4 = Node(4)
node7 = Node(7)
node6 = Node(6)
node8 = Node(8)
rootNode.leftNode = node3
rootNode.rightNode = node7
node3.leftNode = node2
node3.rightNode = node4
node7.leftNode = node6
node7.rightNode = node8

print(kthNode(rootNode).value)