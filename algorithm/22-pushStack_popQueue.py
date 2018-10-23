def isPopOrder(pushV, popV):
    stack = []
    while popV:
        # 当要弹出的值和要压栈的值相同,则出栈
        if pushV and pushV[0] == popV[0]:
            pushV.pop(0)
            popV.pop(0)
        # 当stack保存有值且最后一个值为出栈队列的第一个值时,stack出栈最后一个值, popv出栈第一个值
        elif stack and stack[-1] == popV[0]:
            stack.pop()
            popV.pop(0)
        # 如果还有多余的数,将其加到stack中
        elif pushV:
            stack.append(pushV.pop(0))
        # 如果没有多余的数,也不满足条件,则证明不存在
        else:
            return False
    return True

print(isPopOrder([1, 2, 3, 4, 5], [4, 5, 3, 1, 2]))
print(isPopOrder([], []))
print(isPopOrder(None, None))
