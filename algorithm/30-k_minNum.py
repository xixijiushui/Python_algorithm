import heapq
import time

def getLeastKNumbers(tinput, k):
    start = time.time()
    heaps = []
    ret = []
    for num in tinput:
        heapq.heappush(heaps, num)

    if k > len(heaps):
        return []

    for i in range(k):
        ret.append(heapq.heappop(heaps))
    end = time.time()
    print(ret)
    print(start - end)
    print('*' * 10)

    start = time.time()
    heaps = []
    ret = []
    for num in tinput:
        heapq.heappush(heaps, num)

    if k > len(heaps):
        return []

    print(heapq.nsmallest(k, heaps))
    end = time.time()
    print(start - end)
    print('*' * 10)

    start = time.time()
    newInput = sorted(tinput)
    print(newInput)
    ret = []
    for i in range(k):
        ret.append(newInput.pop(0))
    end = time.time()
    print(ret)
    print(start - end)
    print('*' * 10)

    return ret

print(getLeastKNumbers([1, 9, 2, 8, 3, 7, 4, 6, 5], 4))