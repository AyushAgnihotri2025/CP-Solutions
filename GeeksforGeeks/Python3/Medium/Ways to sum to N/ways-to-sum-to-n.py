#User function Template for python3

class Solution:
    def countWays(self, arr, m, n):
        # code here
        MOD = 10**9+7
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        for i in range(1,n+1):
            for coin in arr:
                if coin>i:
                    break
                dp[i] += dp[i-coin]%MOD if 0<=i-coin<=n+1 else 0
        return dp[n]%MOD

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        m,n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.countWays(arr, m, n))
# } Driver Code Ends