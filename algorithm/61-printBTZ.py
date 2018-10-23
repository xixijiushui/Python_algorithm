class Node(object):
    def __init__(self, value, leftNode=None, rightNode=None):
        self.value = value
        self.leftNode = leftNode
        self.rightNode = rightNode

def printBT(pRoot):
    if pRoot == None:
        return

    stack = [pRoot]
    tmp = [pRoot]
    addSorted = 0

    while stack:
        stack.append(None)
        for node in tmp:
            if node.leftNode:
                stack.append(node.leftNode)
            if node.rightNode:
                stack.append(node.rightNode)

        ret = []
        index = 0
        for node in stack:
            index += 1
            if node == None:
                break
            else:
                ret.append(node.value)

        if addSorted % 2 != 0:
            ret.reverse()
        for i in ret:
            print(i, end=' ')
        print('')

        stack = stack[index: ]
        tmp = stack.copy()
        addSorted += 1

rootNode = Node(8)
node6 = Node(6)
node10 = Node(10)
node5 = Node(5)
node7 = Node(7)
node9 = Node(9)
node11 = Node(11)
rootNode.leftNode = node6
rootNode.rightNode = node10
node6.leftNode = node5
node6.rightNode = node7
node10.leftNode = node9
node10.rightNode = node11

printBT(rootNode)