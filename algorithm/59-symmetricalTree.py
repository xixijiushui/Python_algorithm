def isSymmetrical(pRoot):
    if pRoot == None:
        return True

    return symmetrical(pRoot.leftNode, pRoot.rightNode)

def symmetrical(leftNode, rightNode):
    if leftNode == None and rightNode == None:
        return True

    if leftNode and rightNode:
        return leftNode.value == rightNode.value and symmetrical(leftNode.rightNode, rightNode.leftNode) and \
               symmetrical(leftNode.leftNode, rightNode.rightNode)
    else:
        return False