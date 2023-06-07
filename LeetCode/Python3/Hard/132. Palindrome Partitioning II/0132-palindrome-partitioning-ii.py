class Solution:
    def minCut(self, s: str) -> int:
        N = len(s)
        dp = [-1] + [N] * N
        for i in range(2 * N - 1):
            l = i // 2
            r = l + (i & 1)
            while 0 <= l and r < N and s[l] == s[r]:
                dp[r + 1] = min(dp[r + 1], dp[l] + 1)
                l -= 1
                r += 1
        return dp[-1]