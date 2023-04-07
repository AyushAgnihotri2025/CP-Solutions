class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # Define a DFS helper function
        def dfs(i, j):
            # If i or j is out of bounds or cell is not a land or already visited, return
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
                return
            
            # Mark cell as visited and explore neighbors
            grid[i][j] = -1
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        # Explore land cells from boundary cells
        for i in range(len(grid)):
            dfs(i, 0)
            dfs(i, len(grid[0])-1)
        for j in range(len(grid[0])):
            dfs(0, j)
            dfs(len(grid)-1, j)
        
        # Count the number of land cells that are not visited
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count += 1

        return count