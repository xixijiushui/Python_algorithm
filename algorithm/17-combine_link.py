class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def mergeLinks(headNode1, headNode2):
    if headNode1 == None:
        return headNode2

    if headNode2 == None:
        return headNode1

    mergedHead = None

    if headNode1.val < headNode2.val:
        mergedHead = headNode1
        mergedHead.next = mergeLinks(headNode1.next, headNode2)
    else:
        mergedHead = headNode2
        mergedHead.next = mergeLinks(headNode1, headNode2.next)
    return mergedHead