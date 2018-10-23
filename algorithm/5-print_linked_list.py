class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

def print_linked_list(node):
    '''
    从尾到头打印链表.
    方法1:先保存到栈,再打印
    :param node: 首节点
    '''
    ret = []
    while node:
        ret.append(node)
        node = node.next
    while len(ret) != 0:
        print(ret[-1].value)
        ret.pop()

def print_linked_list2(node):
    '''
    方法2:递归打印,先让后面的打印,优点:代码短 缺点:链表非常长,函数调用层级很深,可能会导致函数调用栈溢出
    :param node: 节点
    '''
    if node.next != None:
        print_linked_list2(node.next)
    print(node.value)

node1 = Node(5)
node2 = Node(2)
node1.next = node2
node3 = Node(3)
node2.next = node3
print_linked_list2(node1)