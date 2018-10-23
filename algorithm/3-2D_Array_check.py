
def findIsExist(array, target):
    '''
    有序的二维数组,判断指定数字是否存在
    :param array: 有序二维数组
    :param target: 指定数字
    :return: 是否存在
    从最右上角/左下角开始,大于目标删除列,小于目标删除行
    '''
    if len(array) == 0 or len(array[0]) == 0:
        return False

    j = 0
    i = len(array[0]) - 1
    while (j < len(array[0]) and i >= 0):
        if array[j][i] == target:
            return True
        elif array[j][i] < target:
            j += 1
        else:
            i -= 1
    return False

array = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
print(findIsExist(array, 5))