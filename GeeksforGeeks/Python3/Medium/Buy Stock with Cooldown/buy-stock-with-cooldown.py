#User function Template for python3

class Solution:
    def maximumProfit(self, prices, n):
        #Code here
        dp = [[0 for _ in range(2)] for _ in range(n + 2)]
        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                profit = 0
                if buy == 0:
                    profit = max(0 + dp[ind + 1][0], -prices[ind] + dp[ind + 1][1])
                if buy == 1:
                    profit = max(0 + dp[ind + 1][1], prices[ind] + dp[ind + 2][0])
                dp[ind][buy] = profit
        return dp[0][0]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n=int(input())
        prices = list(map(int, input().split()))
        ob = Solution()
        print(ob.maximumProfit(prices, n))
# } Driver Code Ends