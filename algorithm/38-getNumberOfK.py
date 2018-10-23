def getNumberOfK(data, k):
    number = 0

    length = len(data)
    if data != None and len(data) > 0:
        first = getFirstK(data, length, k, 0, length - 1)
        last = getLastK(data, length, k, 0, length - 1)

        if first > -1 and last > -1:
            number = last - first + 1
    return number

def getFirstK(data, length, k, start, end):
    if start > end:
        return -1

    middleIndex = (start + end) // 2
    middleData = data[middleIndex]

    if middleData == k:
        if (middleIndex > 0 and data[middleIndex - 1] != k) or middleIndex == 0:
            return middleIndex
        else:
            end = middleIndex - 1
    elif middleData > k:
        end = middleIndex - 1
    else:
        start = middleIndex + 1
    return getFirstK(data, length, k, start, end)

def getLastK(data, length, k, start, end):
    if start > end:
        return -1

    middleIndex = (start + end) // 2
    middleData = data[middleIndex]

    if middleData == k:
        if (middleIndex < length - 1 and data[middleIndex + 1] != k) or middleIndex == length - 1:
            return middleIndex
        else:
            start = middleIndex + 1
    elif middleData < k:
        start = middleIndex + 1
    else:
        end  = middleIndex - 1
    return getLastK(data, length, k, start, end)

print(getNumberOfK([1, 2, 3, 3, 3, 3, 4, 5], 3))