def treeDepth(pRoot):
    if pRoot == None:
        return 0

    nLeft = treeDepth(pRoot.leftNode)
    nRight = treeDepth(pRoot.rightNode)

    return max(nLeft + 1, nRight + 1)

# 会重复遍历
def isBalanced(pRoot):
    if pRoot == None:
        return True

    left = treeDepth(pRoot.leftNode)
    right = treeDepth(pRoot.rightNode)
    diff = abs(left - right)

    if diff > 1:
        return False

    return isBalanced(pRoot.leftNode) and isBalanced(pRoot.rightNode)

# 遍历一次
def isBalancedOnce(pRoot, pDepth):
    if pRoot == None:
        pDepth = 0
        return True

    left, right = (0, 0)
    if isBalancedOnce(pRoot.leftNode, left) and isBalancedOnce(pRoot.rightNode, right):
        diff = abs(left - right)
        if diff <= 1:
            pDepth = 1 + (left if left > right else right)
            return True
    return False