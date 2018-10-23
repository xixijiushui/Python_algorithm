def printMaxOfnDigits(n):
    '''
    用字符串形式打印,防止大数
    :param n:
    :return:
    '''
    if n <= 0:
        return

    number = ['0'] * n
    while not Increment(number):
        PrintNumber(number)

def Increment(number):
    # 从后往前遍历,首次+1,如果大于==10且不是第0位,则将本身做0处理,将上一位+1
    # 如果第0位的值为10,则达到最大值
    isOverflow = False
    nTakeOver = 0
    nLength = len(number)
    for i in range(nLength - 1, -1, -1):
        nSum = int(number[i]) + nTakeOver
        if i == nLength - 1:
            nSum += 1
        if nSum >= 10:
            if i == 0:
                isOverflow = True
            else:
                nSum -= 10
                nTakeOver = 1
                number[i] = str(nSum)
        else:
            number[i] = str(nSum)
            break
    return isOverflow

def PrintNumber(number):
    isBeginning = True
    nLength = len(number)

    for i in range(nLength):
        if isBeginning and number[i] != '0':
            isBeginning = False

        if not isBeginning:
            print(number[i], end='')

    print()

# printMaxOfnDigits(3)

def Print1ToMaxOfNDigits(n):
    if n <= 0:
        return

    number = ['0'] * n
    for i in range(10):
        number[0] = str(i)
        Print1ToMaxOfNDigitsRecursively(number, n, 0)

def Print1ToMaxOfNDigitsRecursively(number, length, index):
    if index == length - 1:
        PrintNumber(number)
        return

    for i in range(10):
        number[index + 1] = str(i)
        Print1ToMaxOfNDigitsRecursively(number, length, index + 1)

Print1ToMaxOfNDigits(3)