def numberOf1Between1AndN(n):
    if n <= 0:
        return 0

    return numberOf1(n)

def numberOf1(n):
    if n == 0:
        return 0

    if n < 10:
        return 1

    strN = str(n)

    length = len(strN)

    # 假设为21345
    # 首位大于1,则以1开头的有10^(n-1)次
    if int(strN[0]) > 1:
        numFirstDigit = pow(10, length - 1)
    # 首位等于1,则以1开头的有n-10^(n-1) + 1次
    else:
        numFirstDigit = n - pow(10, length - 1) + 1

    # 除去首位后剩下的1的个数(1346~21345中除去万位为1的其他为1的个数)
    numOtherDigits = int(strN[0]) * (length - 1) * pow(10, length - 2)

    numberRecursive = numberOf1(int(strN[1:]))

    return numFirstDigit + numOtherDigits + numberRecursive

print(numberOf1Between1AndN(21235))