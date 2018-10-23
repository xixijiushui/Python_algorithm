def addSum(num1, num2):
    '''
    第一步:异或,忽略进位
    第二部:按位与,得到进位的位置
    每次循环,将进位提上去
    '''
    unit = num1 ^ num2
    carry_bit = num1 & num2

    while carry_bit != 0:
        temp_a  = unit
        temp_b = carry_bit << 1
        unit = temp_a ^ temp_b
        carry_bit = temp_a & temp_b
    return unit

print(addSum(7, 15))
