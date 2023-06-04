#User function Template for python3

class Solution:
    def countWays(self, n, Sum):
        # code here
        dp = [[0 for i in range(Sum+1)] for i in range(n+1)]
        dp[0][0] = 1
        for i in range(1, Sum+1):
            dp[0][i] = 0
        for i in range(1, n+1):
            dp[i][0] = 0
        MOD = 10**9 + 7
        for i in range(1, n+1):
            for j in range(1, Sum+1):
                for digit in range(10):
                    if i == 1 and digit == 0:
                        continue
                    if j >= digit:
                        dp[i][j] = (dp[i][j] + dp[i-1][j-digit]) % MOD
        return dp[n][Sum] if dp[n][Sum] > 0 else -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        arr = input().split()
        n = int(arr[0])
        Sum = int(arr[1])
        
        ob = Solution()
        print(ob.countWays(n, Sum))
# } Driver Code Ends