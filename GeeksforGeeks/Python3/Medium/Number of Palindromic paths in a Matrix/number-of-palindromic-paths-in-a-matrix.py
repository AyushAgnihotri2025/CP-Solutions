#User function Template for python3

class Solution:
    def solve(self, ma, i1, j1, i2, j2, dp):
        n = len(ma)
        m = len(ma[0])

        if (i1 >= n or j1 >= m or i2 < 0 or 
                j2 < 0 or i1 > i2 or j1 > j2 or ma[i1][j1] != ma[i2][j2]):
            return 0
            
        if (i1 == i2 and j1 == j2 or i1 == i2 and j1 + 1 == j2 or 
                j1 == j2 and i1 + 1 == i2):
            return 1
        
        x = i1 * n + j1
        y = i2 * n + j2
        if x in dp and y in dp[x]:
            return dp[x][y]
        
        ans = 0
        ans = (ans + self.solve(ma, i1+1, j1, i2-1, j2, dp)) % self.M
        ans = (ans + self.solve(ma, i1+1, j1, i2, j2-1, dp)) % self.M
        ans = (ans + self.solve(ma, i1, j1+1, i2-1, j2, dp)) % self.M
        ans = (ans + self.solve(ma, i1, j1+1, i2, j2-1, dp)) % self.M
        
        if not x in dp:
            dp[x] = {}
        if not y in dp[x]:
            dp[x][y] = ans
        
        return ans

	def countOfPalindromicPaths(self, matrix):
		# Code here
        dp = {}
        n = len(matrix)
        for i in range(n):
            if matrix[i][-1] == ' ':
                matrix[i].pop()
        
        m = len(matrix[0])
        self.M = int(1e9+7)
        
        return self.solve(matrix, 0, 0, n - 1, m - 1, dp)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		matrix = []
		for _ in range(n):
			cur  = input()
			temp = []
			for __ in cur:
				temp.append(__)
			matrix.append(temp)
		obj = Solution()
		ans = obj.countOfPalindromicPaths(matrix)
		print(ans)

# } Driver Code Ends