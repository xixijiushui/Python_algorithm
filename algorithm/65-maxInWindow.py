def maxInWindow(num, size):
    if size == 0:
        return []

    ret = []
    stack = []

    for pos in range(len(num)):
        # 如果最后一个值小于当前值,则删除
        while (stack and stack[-1][0] < num[pos]):
            stack.pop()
        # 将目前的值添加到列表(可能是后面的最大值)
        stack.append((num[pos], pos))
        # 当索引大于size-1时
        if pos >= size-1:
            # 如果第一个的索引差距大于size则删除第一个
            while (stack and stack[0][1] <= pos-size):
                stack.pop(0)
            # 第一个始终为有效的最大值
            ret.append(stack[0][0])
    return ret

print(maxInWindow([2, 3, 4, 2, 6, 2, 5, 1], 3))