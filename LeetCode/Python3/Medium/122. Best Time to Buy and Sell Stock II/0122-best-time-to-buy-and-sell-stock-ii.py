class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        ans=[0]*2
        for i in range(n-1,-1,-1):
            curr=[0]*2
            for j in range(1,-1,-1):
                if j==1:
                    curr[j]=max(ans[j],ans[0]-prices[i])
                else:
                    curr[j]=max(ans[j],ans[1]+prices[i])
            ans=curr
        return ans[1]