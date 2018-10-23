import heapq

def printMinNumber(numbers):
    heaps = []
    maxLen = 0
    for number in numbers:
        maxLen += len(str(number))

    # 将数据存入headpq中,保存数据格式:(当前数据+第一位*缺少的长度,当前数据),按照大小排序
    for number in numbers:
        n = str(number)
        heapq.heappush(heaps, (int(n + (maxLen - len(n)) * n[0]), number))

    ret = ''
    # 遍历,最先推出的是第一位最小的值,然后将其组合起来
    while heaps:
        ret += str(heapq.heappop(heaps)[1])
    return int(ret) if len(ret) else ''

def compare(str1, str2):
    t = str1 + str2
    s = str2 + str1
    if t > s:
        return 1
    elif t < s:
        return -1
    else:
        return 0

from functools import cmp_to_key
def printMinNumber1(numbers):
    if not numbers:
        return ""

    numbers = list(map(str, numbers))
    tmpNumbers = sorted(numbers, key=cmp_to_key(lambda x,y: int(x+y) - int(y+x)))
    return '0' if tmpNumbers[0] == '0' else ''.join(tmpNumbers)

print(printMinNumber([32, 3, 321]))
print(printMinNumber1([32, 3, 321]))
