#User function Template for python3

class Solution:
    def countWays(self, m, n, p, arr):
        # code here
        m = m-p
        if sum(arr)>m:
            return -1
        mod = int(1e9+7)
        dp = [[0 for i in range(m+1)] for j in range(n)]
        for i in range(1,m+1):
            dp[0][i] = 1 if i>=arr[0] else 0
        for i in range(1,n):
            for j in range(m+1):
                if j>=arr[i]:
                    dp[i][j] = dp[i-1][j-arr[i]]+dp[i][j-1]
            dp[i][j] = dp[i][j]%mod
        return dp[n-1][m]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        m, n, p = [int(x) for x in input().split()]
        arr = input().split()
        for i in range(n):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.countWays(m, n, p, arr))
# } Driver Code Ends