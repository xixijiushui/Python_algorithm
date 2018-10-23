

def findContentChildren(g, s):
    '''
    获取最多几个孩子满足
    :param g: 孩子的满意程度
    :param s: 饼干的大小程度
    :return: 最多几个人满足
    '''
    g = sorted(g)
    s = sorted(s)
    i = 0
    # 使用贪心算法,按从小到大排序,不满足就换大饼干,满足则孩子也+1
    for j in range(len(g)):
        if not (i < len(g) and j < len(s)):
            break
        if g[i] <= s[j]:
            i += 1
    return i


print(findContentChildren([1, 3, 2], [1, 5, 3]))