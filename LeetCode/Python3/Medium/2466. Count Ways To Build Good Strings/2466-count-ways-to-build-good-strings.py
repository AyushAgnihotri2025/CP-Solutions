MOD = 10**9 + 7

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        result = 0
        dp = [0]*(high+1)
        dp[0] = 1
        for i in range(1, high+1):
            if i >= zero:
                dp[i] = (dp[i]+dp[i-zero])%MOD
            if i >= one:
                dp[i] = (dp[i]+dp[i-one])%MOD
            if i >= low:
                result = (result+dp[i])%MOD
        return result