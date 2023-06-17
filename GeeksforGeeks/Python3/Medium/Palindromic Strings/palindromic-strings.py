#User function Template for python3
class Solution:
	def isPossiblePalindrome(self, s, K):
		# code here
		n = len(s)
        dp = [[0 for i in range(n)] for j in range(n)]
        for gap in range(n):
            for i in range(n-gap):
                j = i+gap
                if i == j:
                    dp[i][j] = 0
                elif s[i] == s[j]:
                    if i+1 == j:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(dp[i+1][j],dp[i][j-1])+1
        c = dp[0][n-1]
        if c <= K:
            return 1
        return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		K = int(input())
		ob = Solution()
		ans = ob.isPossiblePalindrome(s,K)
		print(ans)

# } Driver Code Ends