
def fibonacci(n):
    results = [0, 1]
    if n < 2:
        return results[n]

    for i in range(n-1):
        results.append(results[-1] + results[-2])
    return results[-1]

print(fibonacci(5))


# 特殊算法: [f(n)    f(n-1)]   --  [1 1] ^(n-1)
#          [f(n-1)  f(n-2)]  --  [1 0]
import numpy as np
a = np.array([[1, 1], [1, 0]])
s = a
n = 5
for i in range(n-2):
    s = np.dot(s, a)
print(s[0][0])


# 跳台阶(实际就是斐波那契)
# 跳一次,剩下的跳法为f(n-1),跳两次,剩下的跳法为f(n-2), 则f(n)=f(n-1)+f(n-2)
def jumpFloor(number):
    '''
    n = 1 : 1
    n = 2 : 2
    n = 3 : dp[n-2] + dp[n-1]
    '''
    if number == 1 or number == 2:
        return number

    dp = [1, 2]
    for i in range(number-2):
        dp.append(dp[-1] + dp[-2])
    return dp[-1]
print(jumpFloor(5))

# 变态跳台阶
# 可跳任意级台阶, 归纳证明f(n)=2^(n-1)
def jumpFloorBT(number):
    return pow(2, number - 1)

def jumpFloorBT2(number):
    # write code here
    if number == 1 or number == 2:
        return number
    ret = sum_ = 3
    for i in range(number - 2):
        ret = sum_ + 1
        sum_ += ret
    return ret

print(jumpFloorBT(5))
print(jumpFloorBT2(5))
