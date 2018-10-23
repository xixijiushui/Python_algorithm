import time

def minNumberInRatateArray(rotateArray):
    start_time = time.time()
    if rotateArray == []:
        return 0
    lenNum = len(rotateArray)
    start = 0
    end = lenNum - 1
    while start < (end - 1):
        # 中间值>开始值,说明还在大的范围
        # 中间值<最后值,说明在小的范围
        mid = (start + end) // 2
        if rotateArray[mid] < rotateArray[mid - 1]:
            end_time = time.time()
            print('***')
            print(start_time - end_time)
            return rotateArray[mid]

        if rotateArray[mid] > rotateArray[start]:
            start = mid
        elif rotateArray[mid] < rotateArray[end]:
            end = mid
    num = min(rotateArray[start], rotateArray[end])
    end_time = time.time()
    print('***')
    print(start_time - end_time)
    return num

def minNumberInRotateArray1(rotateArray):
    start_time = time.time()
    # write code here
    if rotateArray == []:
        return 0
    _len = len(rotateArray)
    left = 0
    right = _len - 1
    while left <= right:
        mid = int((left + right) >> 1)
        if rotateArray[mid] < rotateArray[mid - 1]:
            end_time = time.time()
            print('***')
            print(start_time - end_time)
            return rotateArray[mid]
        if rotateArray[mid] >= rotateArray[right]:
            # 说明在【mid，right】之间
            left = mid + 1
        else:
            # 说明在【left，mid】之间
            right = mid - 1
    num = rotateArray[mid]
    end_time = time.time()
    print('***')
    print(start_time - end_time)
    return num


print(minNumberInRatateArray([4]))
print(minNumberInRotateArray1([4]))