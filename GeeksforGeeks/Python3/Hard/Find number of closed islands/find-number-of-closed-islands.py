#User function Template for python3

class Solution:
	def dfs(self,matrix, visited, x, y, n, m):
        if (x < 0 or y < 0 or
            x >= n or y >= m or
            visited[x][y] == True or
            matrix[x][y] == 0):
            return
        visited[x][y] = True
        self.dfs(matrix, visited, x + 1, y, n, m)
        self.dfs(matrix, visited, x, y + 1, n, m)
        self.dfs(matrix, visited, x - 1, y, n, m)
        self.dfs(matrix, visited, x, y - 1, n, m)
        
        
    def closedIslands(self, matrix, N, M):
        #Code here
        visited = [[False for i in range(M)] for j in range(N)]
        for i in range(N):
            for j in range(M):
                if ((i * j == 0 or i == N - 1 or
                    j == M - 1) and matrix[i][j] == 1 and visited[i][j] == False):
                    self.dfs(matrix, visited, i, j, N, M)
        result = 0       
        for i in range(N):
            for j in range(M):
                if (visited[i][j] == False and matrix[i][j] == 1):
                    result += 1
                self.dfs(matrix, visited, i, j, N, M)
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N, M = map(int,input().split())
        matrix = []
        for i in range(N):
            nums = list(map(int,input().split()))
            matrix.append(nums)
        obj = Solution()
        print(obj.closedIslands(matrix, N, M))
# } Driver Code Ends