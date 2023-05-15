

class Solution:
    def solver(self, x, y):
        if x<0 or x>=self.row or y<0 or y>=self.col or grid[x][y]=='O': return 0
        grid[x][y] = "O"
        for x1, y1 in [[-1, 0], [0, -1], [0, 1], [1, 0]]: self.solver(x+x1, y+y1)

    #Function to find the number of 'X' total shapes.
	def xShape(self, grid):
		#Code here
        self.row, self.col, area = len(grid), len(grid[0]), 0

        for i in range(self.row):
            for j in range(self.col):
                if grid[i][j]=="X":
                    self.solver(i, j)
                    area+=1
        return area


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = [['#' for i in range(m)] for j in range(n)]
		for i in range(n):
			s = input().strip()
			for j in range(m):
				grid[i][j] = s[j]
		obj = Solution()
		ans = obj.xShape(grid)
		print(ans)
# } Driver Code Ends