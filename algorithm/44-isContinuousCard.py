def isContinuous(numbers):
    if not numbers:
        return 0
    numbers.sort()

    # 统计0的个数,当0的个数小于需要补充的个数或有连续的两个非0数,则为不连续
    zeros = numbers.count(0)
    for i, v in enumerate(numbers[:-1]): # 只遍历到倒数第二个防止越界
        if v != 0:
            if numbers[i + 1] == v:
                return False
            zeros -= (numbers[i + 1] - numbers[i] - 1)
            if zeros < 0:
                return False
    return True

print(isContinuous([5, 3, 0, 0, 1]))
