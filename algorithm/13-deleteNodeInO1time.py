class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def deleteNode(headNode, toBeDeleteNode):
    if (not headNode or not toBeDeleteNode):
        return

    # 要删除的节点不是尾节点
    if toBeDeleteNode.next != None:
        node = toBeDeleteNode.next
        toBeDeleteNode.val = node.val
        toBeDeleteNode.next = node.next

        del node
    elif headNode == toBeDeleteNode:
        # 只有一个节点
        del headNode
    else:
        # 有多个节点且是尾节点
        while headNode.next != toBeDeleteNode:
            headNode = headNode.next
        headNode.next = None
        del toBeDeleteNode

