class Node(object):
    def __init__(self, value, leftNode=None, rightNode=None):
        self.value = value
        self.leftNode = leftNode
        self.rightNode = rightNode

def convert(rootNode):
    pLastNode = None
    convertNode(rootNode, pLastNode)

    pHeadNode = pLastNode
    while pHeadNode != None and pHeadNode.leftNode != None:
        pHeadNode = pHeadNode.leftNode

    return pHeadNode


def convertNode(rootNode, pLastNode):
    if rootNode == None:
        return

    pCurrentNode = rootNode

    if pCurrentNode.leftNode != None:
        convertNode(pCurrentNode.leftNode, pLastNode)

    pCurrentNode.leftNode = pLastNode
    if pLastNode != None:
        pLastNode.rightNode = pCurrentNode

    pLastNode = pCurrentNode

    if pCurrentNode.rightNode != None:
        convertNode(pCurrentNode.rightNode, pLastNode)
