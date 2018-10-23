
def numberOf1(n):
    '''
    位右移值,与1做与运算
    :param n:
    :return:
    '''
    ans = 0
    if n < 0:
        n = n & 0xffffffff
    while n:
        ans += n & 1
        n >>= 1
    return ans

def numberOf1New2(n):
    '''
    有多少位数,循环多少次
    用2的整数次值和对象做与运算
    '''
    count = 0
    flag = 1
    while flag:
        if n & flag:
            count += 1
        flag = flag << 1
    return count

def numberOf1New(n):
    '''
    有多少个1,需要循环多少次
    原理:n-1与n做与运算,即把最右边的1去掉
    '''
    count = 0
    while n:
        count += 1
        n = (n - 1) & n
    return count

print(numberOf1(-9))
print(numberOf1 (-9))
print(numberOf1New(1))