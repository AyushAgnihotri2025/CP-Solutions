#User function Template for python3

class Solution:
    def maximumProfit(self, prices, n, fee):
        #Code here
        dp=[[0]*2 for i in range(n+1)]
        dp[n][0]=dp[n][1]=0
        for idx in range(n-1,-1,-1):
            for buy in range(0,2):
                profit=0
                if buy:
                    profit=max(-prices[idx]-fee+dp[idx+1][0],0+dp[idx+1][1])
                else:
                    profit=max(prices[idx]+dp[idx+1][1],0+dp[idx+1][0])
                dp[idx][buy]=profit
        return dp[0][1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n=int(input())
        prices = list(map(int, input().split()))
        fee=int(input())
        ob = Solution()
        print(ob.maximumProfit(prices, n, fee))
# } Driver Code Ends