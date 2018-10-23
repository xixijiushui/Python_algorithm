class Node(object):
    def __init__(self, value, leftNode=None, rightNode=None):
        self.value = value
        self.leftNode = leftNode
        self.rightNode = rightNode

def printBinaryTree(root):
    ret = []
    if root == None:

        return ret
    ret.append(root)
    while len(ret) > 0:
        rootNode = ret[0]
        print(rootNode.value)
        if rootNode.leftNode:
            ret.append(rootNode.leftNode)
        if rootNode.rightNode:
            ret.append(rootNode.rightNode)
        ret.pop(0)

rootNode = Node(1)
rootNode1 = Node(2)
rootNode2 = Node(3)
rootNode.leftNode = rootNode1
rootNode.rightNode = rootNode2
rootNode3 = Node(4)
rootNode4 = Node(5)
rootNode5 = Node(6)
rootNode1.leftNode = rootNode4
rootNode2.leftNode = rootNode3
rootNode2.rightNode = rootNode5

printBinaryTree(rootNode)
