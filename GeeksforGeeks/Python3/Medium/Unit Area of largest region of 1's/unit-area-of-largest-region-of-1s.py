

class Solution:
    def helper(self, i, j):
        if i<0 or i>=self.row or j<0 or j>=self.col or grid[i][j]==0: return 0
        
        grid[i][j] = 0
        
        ul = self.helper(i-1, j-1)
        u = self.helper(i-1, j)
        ur = self.helper(i-1, j+1)
        l = self.helper(i, j-1)
        r = self.helper(i, j+1)
        dl = self.helper(i+1, j-1)
        d = self.helper(i+1, j)
        dr = self.helper(i+1, j+1)
        
        return 1+ul+u+ur+l+r+dl+d+dr

    #Function to find unit area of the largest region of 1s.
	def findMaxArea(self, grid):
		#Code here
        self.row, self.col = len(grid), len(grid[0])
        area = 0
        for i in range(self.row):
            for j in range(self.col):
                if grid[i][j]: area = max(area, self.helper(i, j))
        return area



#{ 
 # Driver Code Starts


if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n, m = map(int, input().split())
        grid = []
        for _ in range(n):
            a = list(map(int, input().split()))
            grid.append(a)
        obj = Solution()
        ans = obj.findMaxArea(grid)
        print(ans)

# } Driver Code Ends