class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def findKthToTail(headNode, k):
    if headNode == None or k == 0:
        return None

    frontNode = headNode

    # 第一个往前走k-1次,第二个开始出发,第一个到终点,则第二个距离终点k
    for i in range(k - 1):
        if frontNode.next != None:
            frontNode = frontNode.next
        else:
            return None

    behindNode = headNode
    while frontNode.next != None:
        frontNode = frontNode.next
        behindNode = behindNode.next

    return behindNode
