def deleteDuplication(phead):
    '''
    如果值相同,则遍历到下一个不相同的值,删除中间的数据
    '''
    if phead == None:
        return

    pPreNode = None
    pNode = phead

    while pNode != None:
        pNext = pNode.next
        needDelete = False
        if pNext != None and pNext.value == pNode.value:
            needDelete = True

        if not needDelete:
            pPreNode = pNode
            pNode = pNode.next
        else:
            value = pNode.value
            pToBeDel = pNode
            while pToBeDel != None and pToBeDel.value == value:
                pNext = pToBeDel.next
                del pToBeDel
                pToBeDel = pNext

            if pPreNode == None:
                phead = pNext
            else:
                pPreNode.next = pNext
            pNode = pNext