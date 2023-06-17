#User function Template for python3
class Solution:
	def minStepToDeleteString(self, s):
		# code here
		dp = [[-1 for _ in range(len(s) + 1)] for _ in range(len(s)+ 1)]
        def solve(s , i , j , dp):
            if i > j :
                return 0
            if i == j :
                return 1
            if dp[i][j] != -1 : return dp[i][j]
            a1 , a2 , a3 = 1e9 , 1e9 , 1e9
            a1 = 1 + solve(s , i + 1 , j , dp)
            if s[i] == s[i + 1]:
                a2 = 1 + solve(s , i + 2 , j , dp)
            for k in range(i + 2 , j + 1):
                if s[i] == s[k] :
                    a3 = min(a3 , solve(s , i + 1 , k - 1 , dp) + solve(s , k + 1 , j , dp))
            dp[i][j] = min(a1 , a2 , a3)
            return dp[i][j]
        return solve(s , 0 , len(s)-1 , dp)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution()
		ans = ob.minStepToDeleteString(s)
		print(ans)
# } Driver Code Ends