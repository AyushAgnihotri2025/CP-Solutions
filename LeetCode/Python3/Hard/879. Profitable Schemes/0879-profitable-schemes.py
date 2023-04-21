class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (n+1) for _ in range(minProfit+1)]
        dp[0][0] = 1
        for i in range(len(group)):
            for j in range(minProfit, -1, -1):
                for k in range(n, group[i]-1, -1):
                    dp[min(j+profit[i], minProfit)][k] = (dp[min(j+profit[i], minProfit)][k] + dp[j][k-group[i]]) % MOD
        ans = 0
        for j in range(n+1):
            ans = (ans + dp[minProfit][j]) % MOD
        return ans