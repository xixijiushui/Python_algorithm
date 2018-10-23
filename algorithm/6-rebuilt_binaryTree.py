class Node(object):
    def __init__(self, value, leftNode=None, rightNode=None):
        self.value = value
        self.leftNode = leftNode
        self.rightNode = rightNode

def buildTree(pre, tin):
    if pre == []:
        return

    val = pre[0]
    index = tin.index(val)
    ltin = tin[0: index]
    rtin = tin[index + 1: ]
    lenLtin = len(ltin)
    lpre = pre[1: lenLtin + 1]
    rpre = pre[lenLtin + 1: ]
    root = Node(val)
    root.value = val
    root.leftNode = buildTree(lpre, ltin)
    root.rightNode = buildTree(rpre, rtin)
    return root

def print_back(root):
    if root.leftNode:
        print_back(root.leftNode)
    if root.rightNode:
        print_back(root.rightNode)
    print(root.value)

root = buildTree([1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6])
print_back(root)

