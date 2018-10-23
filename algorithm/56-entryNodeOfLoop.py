class Solution(object):
    def hasCycle(self, head):
        '''
        找到环内节点,一快一慢,如有环,则一定在环内重合
        '''
        if head == None or head.next == None:
            return False

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return None

    def entryNode(self, head):
        '''
        找到环内节点,先获取环的长度,一个节点先走环的长度,另外一个出发,则在入口处重合
        '''
        if self.hasCycle(head) == None:
            return None

        meetingNode = self.hasCycle(head)
        nodesInLoop = 1
        pNode = meetingNode
        while pNode.next != meetingNode:
            pNode = pNode.next
            nodesInLoop += 1

        pNode1 = head
        pNode2 = head
        for i in range(nodesInLoop):
            pNode1 = pNode1.next

        while pNode1 != pNode2:
            pNode1 = pNode1.next
            pNode2 = pNode2.next
        return pNode1