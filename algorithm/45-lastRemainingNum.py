def lastRemainingNumber(n, m):
    '''
    删除第k个数,则接下来的排序则为k+1...n-1,0...k-1,转换下起始点为(k+m-1)%n,循环操作取最后一个值
    '''
    if n < 1 or m < -1:
        return -1

    start = 0
    arr = [i for i in range(n)]
    while len(arr) > 1:
        k = (start + m - 1) % n
        arr.pop(k)
        n -= 1
        start = k
    return arr[0]

print(lastRemainingNumber(5, 3))