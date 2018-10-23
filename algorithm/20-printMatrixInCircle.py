
def printMatrixClockwisely(numbers, columns, rows):
    if numbers == None or columns <= 0 or rows <= 0:
        return

    start = 0
    while columns > start * 2 and rows > start * 2:
        printMatrixInCircle(numbers, columns, rows, start)
        start += 1

def printMatrixInCircle(numbers, columns, rows, start):
    endX = columns - start - 1
    endY = rows - start - 1

    # 从左到右打印一行
    for i in range(start, endX + 1):
        print(numbers[start][i])

    # 从上到下打印一列
    if start < endY:
        for i in range(start+1, endY + 1):
            print(numbers[i][endX])

    # 从右到左打印一行
    if start < endX and start < endY:
        for i in range(endX-1, start-1, -1):
            print(numbers[endY][i])

    # 从下到上打印一列
    if start < endX and start < endY:
        for i in range(endY - 1, start, -1):
            print(numbers[i][start])

# printMatrixClockwisely([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 4, 4)
printMatrixClockwisely([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], 4, 3)