class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        res=0
        def dfs(i,j):
            if grid[i][j]=="1":
                grid[i][j]="x"
                if j<n-1:
                    dfs(i,j+1)
                if j>0:
                    dfs(i,j-1)
                if i>0:
                    dfs(i-1,j)
                if i<m-1:
                    dfs(i+1,j)
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    res+=1
                    dfs(i,j)
        return res