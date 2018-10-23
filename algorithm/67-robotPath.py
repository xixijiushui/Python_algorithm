def movingCount(threshold, rows, cols):
    memories = set()

    def dfs(i, j):
        def judge(i, j):
            return sum(map(int, list(str(i)))) + sum(map(int, list(str(j)))) <= threshold

        if not judge(i, j) or (i, j) in memories:
            return

        memories.add((i, j))
        if i != rows - 1:
            dfs(i + 1, j)
        if j != cols - 1:
            dfs(i, j + 1)
    dfs(0, 0)
    return len(memories)

print(movingCount(18, 20, 20))