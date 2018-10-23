class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def reverse_link(headNode):
    reversedHead = None
    pNode = headNode
    pPrevNode = None
    while pNode != None:
        pNext = pNode.next

        if pNext == None:
            reversedHead = pNode

        pNode.next = pPrevNode
        pPrevNode = pNode
        pNode = pNext
    return reversedHead