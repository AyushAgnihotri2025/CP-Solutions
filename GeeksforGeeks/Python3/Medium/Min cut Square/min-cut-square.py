#User function Template for python3
class Solution:
	def minCut(self, M, N):
		# code here
        dp = [[float('inf')] * (N + 1) for _ in range(M + 1)]
        for i in range(1, min(M, N) + 1):
            dp[i][i] = 1
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if i == j:
                    dp[i][j] = 1
                else:
                    for k in range(1, i // 2 + 1):
                        dp[i][j] = min(dp[i][j], dp[k][j] + dp[i - k][j])
                    for k in range(1, j // 2 + 1):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[i][j - k])
        return dp[M][N]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		m,n = input().split()
		m,n = int(m),int(n)
		ob = Solution()
		ans = ob.minCut(m,n)
		print(ans)

# } Driver Code Ends