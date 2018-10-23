def hasPath(matrix, rows, cols, path):
    def dfs(memories, r, c, s):
        if s == '':
            return True

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for k in range(4):
            # 遍历获取周边的四个点
            x = dx[k] + r
            y = dy[k] + c
            # 满足x,y有效且值相同
            if x >= 0 and x < rows and y >=0 and y < cols and memories[x][y] and matrix[x*cols+y] == s[0]:
                # 同第一个点的处理方式
                memories[x][y] = False
                if dfs(memories[:], x, y, s[1: ]):
                    return True
                memories[x][y] = True
        return False

    if path == '':
        return True
    memories = [[True for c in range(cols)] for r in range(rows)]
    for r in range(rows):
        for c in range(cols):
            # 遍历数据获取第一个值的起点
            if matrix[r*cols+c] == path[0]:
                # 将当前起点设置为不可选取
                memories[r][c] = False
                # 找到完整路径返回True
                if dfs(memories[:], r, c, path[1:]):
                    return True
                # 找不到路径,则将当前点设为可选,重新寻找第一个点
                memories[r][c] = True
    return False

print(hasPath(['a', 'b', 'c', 'e', 's', 'f', 'c', 's', 'a', 'd', 'e', 'e'], 3, 4, 'bcced'))