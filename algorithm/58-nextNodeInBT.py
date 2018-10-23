class Node(object):
    def __init__(self, value, leftNode=None, rightNode=None, parentNode=None):
        self.value = value
        self.leftNode = leftNode
        self.rightNode = rightNode
        self.parentNode = parentNode

def getNext(pNode):
    if pNode == None:
        return None

    # 如果有右子树,找到右子数的左节点
    if pNode.rightNode:
        tmpNode = pNode.rightNode
        while tmpNode.leftNode:
            tmpNode = tmpNode.leftNode
        return tmpNode

    # p是结点, p是左节点,返回父节点 p是右节点,返回父节点有右子树的节点
    p = pNode.parentNode
    while p and p.rightNode == pNode:
        pNode = p
        p = p.parentNode
    return p

rootNode = Node('a')
nodeb = Node('b')
nodec = Node('c')
noded = Node('d')
nodee = Node('e')
nodef = Node('f')
nodeg = Node('g')
nodeh = Node('h')
nodei = Node('i')

rootNode.leftNode = nodeb
rootNode.rightNode = nodec

nodeb.leftNode = noded
nodeb.rightNode = nodee

nodee.leftNode = nodeh
nodee.rightNode = nodei

nodec.leftNode = nodef
nodec.rightNode = nodeg

nodeh.parentNode = nodee
nodei.parentNode = nodee

noded.parentNode = nodeb
nodee.parentNode = nodeb

nodef.parentNode = nodec
nodeg.parentNode = nodec

nodeb.parentNode = rootNode
nodec.parentNode = rootNode

print(getNext(nodee).value)