class Node(object):
    def __init__(self, value, leftNode=None, rightNode=None, parentNode=None):
        self.value = value
        self.leftNode = leftNode
        self.rightNode = rightNode
        self.parentNode = parentNode

# 1.二叉搜索树
def getLastCommonParent1(pRoot, pNode1, pNode2):
    # 二叉搜索树是按顺序排列好的,只有找到一个最小根值在两个数之间,则是公共节点
    if pRoot == None or pNode1 == None or pNode2 == None:
        return None

    if pRoot.value < pNode1.value and pRoot.value < pNode2.value:
        return getLastCommonParent1(pRoot.rightNode, pNode1, pNode2)
    elif pRoot.value > pNode1.value and pRoot.value > pNode2.value:
        return getLastCommonParent1(pRoot.leftNode, pNode1, pNode2)
    else:
        return pRoot

# 2.有指向父节点的普通树
def getLastCommonParent2(pRoot, pNode1, pNode2):
    # 有公共节点时,则len(node1) - index(commonNode1) = len(node2) - index(commonNode2),
    # 即len(node1)+index(commonNode2) = len(node2)+index(commonNode1)
    pa = pNode1
    pb = pNode2
    while pa != pb:
        pa = pNode2 if pa is None else pa.parentNode # 当到达根节点,切换到node2,一共走len(node1)+index(commonNode2)
        pb = pNode1 if pb is None else pb.parentNode # 当到达根节点,切换到node1,一共走len(node2)+index(commonNode1)
    return pa

# 3.没有指向父节点的普通树
def getLastCommonParent3(pRoot, pNode1, pNode2):
    path1 = []
    GetNodePath(rootNode, pNode1, path1)

    path2 = []
    GetNodePath(rootNode, pNode2, path2)

    return getLastCommondNode(path1, path2)

def GetNodePath(pRoot, pNode, path):
    path.append(pRoot)

    found = False

    if pRoot.value == pNode.value:
        found = True

    while (not found) and (pRoot.leftNode != None or pRoot.rightNode != None):
        if pRoot.leftNode != None:
            found = GetNodePath(pRoot.leftNode, pNode, path)
        if not found and pRoot.rightNode != None:
            found = GetNodePath(pRoot.rightNode, pNode, path)

    if not found:
        path.pop(-1)

    return found

def getLastCommondNode(path1, path2):
    pLast = path1[0]
    path1.pop(0)
    path2.pop(0)
    while len(path1) and len(path2):
        if path1[0] == path2[0]:
            pLast = path1[0]
        path1.pop(0)
        path2.pop(0)
    return pLast

rootNode = Node(5)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
rootNode.leftNode = node3
rootNode.rightNode = node7
node3.parentNode = rootNode
node7.parentNode = rootNode

node3.leftNode = node2
node2.parentNode = node3

node2.leftNode = node1
node1.parentNode = node2

node3.rightNode = node4
node4.parentNode = node3

node7.leftNode = node6
node6.parentNode = node7

node7.rightNode = node8
node8.parentNode = node7

print(getLastCommonParent1(rootNode, node1, node3).value)

print(getLastCommonParent2(rootNode, node1, node3).value)

print(getLastCommonParent3(rootNode, node1, node3).value)