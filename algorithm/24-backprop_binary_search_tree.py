def vertifySequenceOfBST(sequence):
    if len(sequence) == 0:
        return False

    # 获取最后一个的值
    root = sequence[-1]

    # 获取小于root值的index(既为左节点)
    i = 0
    for node in sequence[: -1]:
        if node > root:
            break
        i += 1

    # 将index到-1的值与root相比,当有值小于root,则是False
    for node in sequence[i: -1]:
        if node < root:
            return False

    left = True
    if i > 1:
        left = vertifySequenceOfBST(sequence[:i])

    right = True
    if i < len(sequence) - 2 and left:
        right = vertifySequenceOfBST(sequence[i+1: -1])

    return right

print(vertifySequenceOfBST([5, 7, 6, 9, 11, 10, 8]))
print(vertifySequenceOfBST([7, 4, 6, 5]))