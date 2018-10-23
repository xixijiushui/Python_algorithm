class binaryTreeNode(object):
    def __init__(self, value, leftNode=None, rightNode=None):
        self.value = value
        self.leftNode = leftNode
        self.rightNode = rightNode

def hasSubTree(rootNode1, rootNode2):
    def subTree(rootNode1, rootNode2):
        if rootNode1 == None and rootNode2 == None:
            return True

        if rootNode1 == None or rootNode2 == None:
            return False

        if rootNode1.value == rootNode2.value:
            if rootNode2.leftNode == None and rootNode2.rightNode == None:
                return True
            if subTree(rootNode1.leftNode, rootNode2.leftNode) and subTree(rootNode1.rightNode, rootNode2.rightNode):
                return True
        return subTree(rootNode1.leftNode, rootNode2) or subTree(rootNode1.rightNode, rootNode2)

    if rootNode1 == None or rootNode2 == None:
        return False

    return subTree(rootNode1, rootNode2)
