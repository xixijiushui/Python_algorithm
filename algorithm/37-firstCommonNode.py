class Node(object):
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

def firstCommonNode(headNode1, headNode2):
    length1 = getListLength(headNode1)
    length2 = getListLength(headNode2)

    pHeadLong, pHeadShort = (headNode1, headNode2) if length1 > length2 else (headNode2, headNode1)

    nLengthDif = abs(length1 - length2)

    for _ in range(nLengthDif):
        pHeadLong = pHeadLong.nextNode

    while pHeadLong != None and pHeadShort != None and pHeadLong != pHeadShort:
        pHeadLong = pHeadLong.nextNode
        pHeadShort = pHeadShort.nextNode

    pFirstCommomNode = pHeadLong
    return pHeadLong

def getListLength(headNode):
    pNode = headNode
    length = 0
    while pNode != None:
        length += 1
        pNode = pNode.nextNode
    return length

node = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node.nextNode = node4
node4.nextNode = node5

node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node5

node5.nextNode = node6

# commonNode = firstCommonNode(node, node1)
commonNode = firstCommonNode(None, None)
print(commonNode.value if commonNode else None)
