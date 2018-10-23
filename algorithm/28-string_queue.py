def permutation(ss):
    def dfs(s):
        if len(s) == '':
            return []
        if len(s) == 1:
            return [s]
        if len(s) == 2:
            return list(set([s[0] + s[1], s[1] + s[0]]))

        ans = set([])
        left = s[0]
        right = dfs(s[1:])
        for word in right:
            for i in range(len(word) + 1):
                ans.add(word[:i] + left + word[i:])
        return list(ans)
    if ss == '':
        return []
    return sorted(dfs(ss))

print(permutation('abc'))