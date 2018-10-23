
def minPatches(nums, n):
    sum, ans, index = 0, 0, 0

    # 如果有值并且第一个为0, 设置sum和index为1
    if len(nums) > 0 and nums[0] == 1:
        sum = 1
        index = 1

    # 循环求的最大和小于n
    while sum < n:
        # 判断下一个元素是否大于当前和,即m+1,不满足就不需要添加新元素
        while index < len(nums) and nums[index] <= (sum + 1):
            sum += nums[index]
            index += 1

        # 满足m+1的条件,则判断原数组中是否存在m+1的元素,不存在则添加
        if sum < n:
            if index < len(nums) and nums[index] == (sum + 1):
                index += 1
            else:
                ans += 1
            sum = 2 * sum + 1
    return ans

print(minPatches([2, 4], 20))