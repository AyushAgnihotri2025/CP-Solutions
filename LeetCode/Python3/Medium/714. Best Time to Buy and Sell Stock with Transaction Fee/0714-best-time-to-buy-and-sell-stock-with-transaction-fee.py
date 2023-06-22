class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        min_p = prices[0] + fee
        res = 0
        for p in prices:
            if min_p < p:
                res += p-min_p
                min_p = p
            elif p+fee < min_p:
                min_p = p + fee
        return res