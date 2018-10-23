def moreThanHalfNum(numbers):
    if checkInvalidArray(numbers):
        return 0

    # 保存一个值和引用次数,如果下一个值相同,引用次数+1,不相同,引用次数-1,当引用次数为0,下个值重复此过程,最后有值的一定是超过半数的
    length = len(numbers)
    result = numbers[0]
    times = 1
    for number in numbers[1:]:
        if times == 0:
            result = number
            times = 1
        elif number == result:
            times += 1
        else:
            times -= 1

    if not checkMoreThanHalf(numbers, length, result):
        return 0
    return result

def checkInvalidArray(numbers):
    if numbers == None or len(numbers) <= 0:
        return True

def checkMoreThanHalf(numbers, length, number):
    times = 0
    for list_number in numbers:
        if list_number == number:
            times += 1

    if times * 2 <= length:
        return False
    return True

print(moreThanHalfNum([1, 2, 3, 2, 1, 2, 2]))