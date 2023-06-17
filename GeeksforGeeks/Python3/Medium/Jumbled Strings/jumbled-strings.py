#User function Template for python3

class Solution:
	def TotalWays(self, str):
		# Code here
		mod = int(1e9+7)
        s2 = "GEEKS"
        dp = [[0 for i in range(len(s2)+1)] for j in range(len(str)+1)]
        dp[0][0] = 1
        for i in range(1,len(str)+1):
            dp[i][0] = 1
        for i in range(1,len(str)+1):
            for j in range(1,len(s2)+1):
                if str[i-1] == s2[j-1]:
                    dp[i][j] = (dp[i-1][j-1]+dp[i-1][j])%mod
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(str)][len(s2)]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution()
		ans = ob.TotalWays(str)
		print(ans)
# } Driver Code Ends