#User function Template for python3
class Solution:
	def minTimeForWritingChars(self, N, I, D, C):
		# code here
		dp = [0]*(N+1)
        dp[1] = I
        for i in range(2,N+1):
            dp[i] = dp[i-1]+I
            if i%2 == 0:
                dp[i] = min(dp[i],dp[i//2]+C)
            else:
                dp[i] = min(dp[i],dp[i//2 + 1]+C+D)
        return dp[-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N,I,D,C = input().split()
		N,I,D,C = int(N),int(I),int(D),int(C)
		ob = Solution()
		ans = ob.minTimeForWritingChars(N, I, D, C)
		print(ans)

# } Driver Code Ends