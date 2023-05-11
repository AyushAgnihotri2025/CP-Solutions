import heapq
from collections import deque
class Solution:

    #Function to find minimum time required to rot all oranges. 
	def orangesRotting(self, grid):
		#Code here
		n,m = len(grid),len(grid[0])
        row,col = [0,-1,0,1],[-1,0,1,0]
        visited = []
        lvl = 0
        for i in range(n) :
            for j in range(m) :
                if grid[i][j] == 2 :
                    visited.append([i,j,lvl])
        return self.bfs(grid,n,m,row,col,visited)
        
        
    def bfs(self,mat,n,m,row,col,visited) :
        q = deque()
        for val in visited :
            q.append(val)
        max_lvl = 0
        while len(q) > 0 :
            temp = q.popleft()
            i,j,lvl = temp[0],temp[1],temp[2]
            if mat[i][j] == 2 :
                for k in range(len(row)) :
                    if i+row[k] < 0 or i+row[k] > n -1 or j+col[k] < 0 or j + col[k] > m-1 :
                        continue
                    elif mat[i+row[k]][j+col[k]] == 1 :
                        mat[i+row[k]][j+col[k]] = 2
                        q.append([i+row[k],j+col[k],lvl+1])
                        max_lvl = max(max_lvl,lvl+1)
        for i in range(n) :
            for j in range(m) :
                if mat[i][j] == 1 :
                    return -1
        return max_lvl


#{ 
 # Driver Code Starts
from queue import Queue

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.orangesRotting(grid)
		print(ans)

# } Driver Code Ends