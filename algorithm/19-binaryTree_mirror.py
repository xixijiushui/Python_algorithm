class binaryTreeNode(object):
    def __init__(self, value, leftNode=None, rightNode=None):
        self.value = value
        self.leftNode = leftNode
        self.rightNode = rightNode

def mirrorRecursively(rootNode):
    if rootNode == None:
        return

    if rootNode.leftNode == None and rootNode.rightNode == None:
        return

    rootNode.leftNode, rootNode.rightNode = rootNode.rightNode, rootNode.leftNode

    if rootNode.leftNode:
        mirrorRecursively(rootNode.leftNode)

    if rootNode.rightNode:
        mirrorRecursively(rootNode.rightNode)