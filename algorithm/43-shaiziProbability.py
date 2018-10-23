g_maxValue = 6

def printProbability(number):
    if number < 1:
        return

    maxSum = number * 6
    pProbabilities = []
    # 将可能的大小列成列表
    for i in range(number, maxSum + 1):
        pProbabilities.append(0)

    probability(number, pProbabilities)

    # 所有情况的次数
    total = pow(g_maxValue, number)
    for i in range(number, maxSum + 1):
        ratio = pProbabilities[i - number] / total
        print(i, ratio)

def probability(number, pProbabilities):
    for i in range(1, g_maxValue + 1):
        probability1(number, number, i, pProbabilities)

def probability1(original, current, sum, pProbabilities):
    if current == 1:
        pProbabilities[sum - original] += 1
    else:
        for i in range(1, g_maxValue + 1):
            probability1(original, current - 1, i + sum, pProbabilities)

printProbability(4)