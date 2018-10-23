def recordOddEven(pData):
    if pData == None or len(pData) == 0:
        return

    start = 0
    end = len(pData) - 1

    while start < end:
        while start < end and pData[start] & 0x1 != 0:
            start += 1

        while start < end and pData[end] & 0x1 == 0:
            end -= 1

        if start < end:
            pData[start], pData[end] = pData[end], pData[start]

pData = [1, 2, 3, 4, 5]
recordOddEven(pData)
print(pData)