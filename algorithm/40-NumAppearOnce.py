def findNumsAppearOnce(data):
    '''
    原理:当只有一个不同的数时,将所有的值进行异或,相同的值异或为0
    当两个数时,必然最少有一个二进制异或值为1.将其分为两组,求每组的异或值
    '''
    if data == None or len(data) < 2:
        return

    # 异或求和,相同的数字异或为0,剩下的值为没有重复数字的异或和
    ans = 0
    for num in data:
        ans = num ^ ans

    num1, num2 = 0, 0
    flag = 1

    # 获取异或和二进制中最右边的1代表的值
    while ans:
        if ans % 2 == 0:
            ans = ans >> 1
            flag = flag << 1
        else:
            break
    # 遍历数据,当数据二进制中与最右边1代表的值有与关系时,将其放在一组进行异或
    for num in data:
        if num & flag:
            num1 = num1 ^ num
        else:
            num2 = num2 ^ num
    return num1, num2

print(findNumsAppearOnce([1, 2, 8, 4, 2, 1]))
