#User function Template for python3

class Solution:
	def totalWays(self, N, K):
		# Code here
        if N<K:
            return 0
        MOD = 10**9+7
        n, m = N-1, K-1
        if n-m < m:
            m = n-m
        ans = 1
        for i in range(1, m+1):
            ans = (ans * (n-(i-1)) * pow(i, MOD-2, MOD)) % MOD
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, k = input().split()
		n = int(n)
		k = int(k)
		ob = Solution()
		ans = ob.totalWays(n, k)
		print(ans)

# } Driver Code Ends