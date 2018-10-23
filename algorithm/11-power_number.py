def power_number(base, exponent):
    # 指数为0返回1
    if exponent == 0:
        return 1

    if exponent == 1:
        return base

    # 基数为0返回0
    if equal(base, 0):
        return 0

    isPosVal = 1
    if exponent < 0:
        exponent = -exponent
        isPosVal = -1

    result = 1
    for _ in range(exponent):
        result *= base

    if isPosVal == -1:
        return 1 / result
    return result

def PowerWithExponent(base, exponent):
    '''
    思想:a^n = (a^(n/2))^2
    '''
    if exponent == 0:
        return 1

    if exponent == 1:
        return base

    if equal(base, 0):
        return 0

    result = PowerWithExponent(base, exponent >> 1)
    result *= result
    # 奇数需要再乘以一次本身
    if exponent & 0x1 == 1:
        result *= base
    return result

def equal(num1, num2):
    '''
    判断在一定范围内的都为0
    '''
    if ((num1 - num2) > -0.0000001 and (num1 - num2) < 0.0000001):
        return True
    else:
        return False

print(power_number(0.2, 5))
print(power_number(-0.2, 5))
print(power_number(0.2, -5))
print(power_number(-0.0000000002, 5))
print(PowerWithExponent(0.2, 5))
