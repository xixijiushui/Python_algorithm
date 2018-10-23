import heapq

def getUglinessNumber(index):
    if index < 1:
        return 0
    heaps = []
    heapq.heappush(heaps, 1)
    lastNum = None
    idx = 1
    while idx <= index:
        curNum = heapq.heappop(heaps)
        while curNum == lastNum:
            curNum = heapq.heappop(heaps)
        lastNum = curNum
        idx += 1
        heapq.heappush(heaps, curNum*2)
        heapq.heappush(heaps, curNum*3)
        heapq.heappush(heaps, curNum*5)
    return lastNum

print(getUglinessNumber(1500))