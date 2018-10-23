import bisect

def inversePairs(data):
    data.reverse()
    L = []
    ret = 0
    for d in data:
        pos = bisect.bisect_left(L, d)
        L.insert(pos, d)
        ret += pos
    return ret

print(inversePairs([7, 5, 5, 6, 4]))