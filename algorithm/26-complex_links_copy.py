class Node(object):
    def __init__(self, value, nextNode=None, siblingNode=None):
        self.value = value
        self.nextNode = nextNode
        self.siblingNode = siblingNode

def cloneNodes(headNode):
    pNode = headNode
    # 将所有node复制一份,按照A->A'的顺序排列
    while pNode != None:
        clonedNode = Node(pNode.value, pNode.nextNode, pNode.siblingNode)
        pNode.nextNode = clonedNode
        pNode = clonedNode.nextNode

def connectSiblingNode(headNode):
    pNode = headNode
    # 更改复制node的siblingNode为复制出来的node
    while pNode != None:
        clonedNode = pNode.nextNode
        if pNode.siblingNode != None:
            clonedNode.siblingNode = pNode.siblingNode.nextNode
        pNode = clonedNode.nextNode

def reconnectNodes(headNode):
    pNode = headNode
    clonedHead = None
    clonedNode = None

    if pNode != None:
        clonedHead = clonedNode = pNode.nextNode
        pNode.nextNode = clonedNode.nextNode
        pNode = pNode.nextNode

    while pNode != None:
        # 将复制的node传递给复制node的下一个节点
        clonedNode.nextNode = pNode.nextNode
        # 将复制node复制为下一个复制的节点
        clonedNode = clonedNode.nextNode
        # 将正常的下一个节点设为pNode的下一个节点
        pNode.nextNode = clonedNode.nextNode
        # 设置正常节点为下一个节点
        pNode = pNode.nextNode

    return clonedHead

def cloneLinks(headNode):
    cloneNodes(headNode)
    connectSiblingNode(headNode)
    return reconnectNodes(headNode)