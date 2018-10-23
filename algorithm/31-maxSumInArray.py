def findCreatestSumOfSubArray(pData):
    if pData == None or len(pData) == 0:
        return 0

    nCurSum = 0
    nGreatestSum = 0
    for data in pData:
        if nCurSum <= 0:
            nCurSum = data
        else:
            nCurSum += data

        if nCurSum > nGreatestSum:
            nGreatestSum = nCurSum
    return nGreatestSum

# print(findCreatestSumOfSubArray([1, -2, 3, 10, -4, 7, 2, -5]))
print(findCreatestSumOfSubArray([-1, -2, -3, -10, -4, -7, -2, -5]))