class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        m, n = len(words), len(words[0])
        l = len(target)
        d = [{} for i in range(n)]
        for i in range(m):
            for j in range(n):
                c = words[i][j]
                d[j][c] = d[j].get(c, 0) + 1
        @lru_cache(None)
        def dfs(i, j):
            if j == l:
                return 1
            elif n - i < l - j:
                return 0
            if target[j] not in d[i]:
                return dfs(i + 1, j)
            return (dfs(i + 1, j) + d[i][target[j]] * dfs(i + 1, j + 1)) % mod
        mod = 10 ** 9 + 7
        return dfs(0, 0)