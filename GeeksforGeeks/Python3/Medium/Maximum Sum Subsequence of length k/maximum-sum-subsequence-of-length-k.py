#User function Template for python3

class Solution:
	def max_sum(self, a, k):
		# Code here
        n = len(a)
        dp = [[-1 for i in range(k)] for j in range(n)]
        for i in range(n):
            dp[i][0] = a[i]
            for j in range(1,k):
                for l in range(i):
                    if a[l]<=a[i] and dp[l][j-1]!=-1:
                        dp[i][j] = max(dp[i][j],dp[l][j-1]+a[i])
        m = -1
        for i in range(n):
            m = max(m,dp[i][k-1])
        return m

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, k = input().split()
		n = int(n)
		k = int(k)
		a = list(map(int,input().split()))
		ob = Solution()
		ans = ob.max_sum(a, k)
		print(ans)
# } Driver Code Ends