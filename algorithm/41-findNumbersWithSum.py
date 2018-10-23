def findNumbersWithSum(data, sumNum):
    '''
    选取第一个和最后一个值,如果和大于sum,减小最大值,小于sum,增大最小值
    '''
    if len(data) < 1:
        return -1

    length = len(data)
    head = 0
    end = length - 1

    while head < end:
        curSum = data[head] + data[end]

        if curSum == sumNum:
            return (data[head], data[end])
        elif curSum < sumNum:
            head += 1
        else:
            end -= 1
    return -1

print(findNumbersWithSum([1, 2, 4, 6, 11, 15], 15))

def findContinuesSequence(sum):
    '''
    将最小值与最大值指向1和2,如果小,增加最大值,如果大,改变最小值
    '''
    if sum < 3:
        return

    small = 1
    big = 2
    middle = (1 + sum) / 2
    curSum = small + big

    while small < middle:
        if curSum == sum:
            printContinuesSequence(small, big)
        while curSum > sum and small < middle:
            curSum -= small
            small += 1

            if curSum == sum:
                printContinuesSequence(small, big)
        big += 1
        curSum += big

def printContinuesSequence(small, big):
    for i in range(small, big+1):
        print(i, end=' ')
    print()

findContinuesSequence(9)
findContinuesSequence(4)