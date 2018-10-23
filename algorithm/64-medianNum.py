from heapq import *

class MedianFinder(object):
    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        # 存入small的是负值,则保证了第一个的绝对值为最大的
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            # 取出来要将符号转变成正值存入large
            heappush(large, -heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        # 将large中最小的值与small中最小的负值(-负值==+正值)相减/2得到中位数
        return (large[0] - small[0]) / 2.0

median = MedianFinder()
median.addNum(1)
median.addNum(2)
median.addNum(3)
median.addNum(4)
median.addNum(5)
median.addNum(6)
print(median.findMedian())