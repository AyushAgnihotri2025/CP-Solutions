#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def totalWays(self, n, m, grid):
        # Code here
        dp=[[-1]*m for _ in range(n)]
        return self.f(n-1,m-1,grid,dp)%(10**9+7)
    
    def f(self,i,j,grid,dp):
        if i==0 and j==0 and grid[i][j]==0:
            return 1
        if i==0 and j==0 and grid[i][j]==1:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        up=0
        left=0
        if i-1 >=0 and grid[i-1][j]==0:
            up=self.f(i-1,j,grid,dp)
        if j-1 >=0 and grid[i][j-1]==0:
            left=self.f(i,j-1,grid,dp)
        dp[i][j]=left+up
        return dp[i][j]


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, m = list(map(int, input().split()))
        grid = [list(map(int, input().split())) for _ in range(n)]
        ob = Solution()
        res = ob.totalWays(n, m, grid)
        print(res)
# } Driver Code Ends