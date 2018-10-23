class Node(object):
    def __init__(self, value, leftNode=None, rightNode=None):
        self.value = value
        self.leftNode = leftNode
        self.rightNode = rightNode

ret = []

def findPath(root, exceptNumber):
    if root == None:
        return

    dfs(root, exceptNumber, [])


def dfs(root, exceptNumber, tmp):
    global ret
    if root:
        # 如果是叶结点,则判断值与期望值是否相同,相同则添加
        if root.leftNode == None and root.rightNode == None:
            if root.value == exceptNumber:
                tmp.append(root.value)
                ret.append(tmp[:])
        else:
            # 不是叶结点,则将期望值减去节点值,将左右节点分别作为root值传入
            tmp.append(root.value)
            dfs(root.leftNode, exceptNumber - root.value, tmp[:])
            dfs(root.rightNode, exceptNumber - root.value, tmp[:])

node = Node(10)
node1 = Node(5)
node2 = Node(4)
node3 = Node(7)
node4 = Node(12)
node5 = Node(0)

node.leftNode = node1
node.rightNode = node4
node1.leftNode = node2
node1.rightNode = node3
node4.leftNode = node5

findPath(root=node, exceptNumber=22)
print(ret)