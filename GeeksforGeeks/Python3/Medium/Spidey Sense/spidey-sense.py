from collections import deque

class Solution:
    def findDistance(self, matrix, n, m):
        # Your code goes here
        ans = [[-1] * m for _ in range(n)]
        q = deque()
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 'B':
                    ans[i][j] = 0
                    q.append((i, j))
        
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        while len(q) > 0:
            x, y = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if not (nx >= 0 and nx < n and ny >= 0 and ny < m):
                    continue
                if matrix[nx][ny] == 'O' and ans[nx][ny] == -1:
                    ans[nx][ny] = ans[x][y] + 1
                    q.append((nx, ny))
        
        return ans





#{ 
 # Driver Code Starts
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        size = input().strip().split()
        m = int(size[0])
        n = int(size[1])
        matrix=[]
        for _ in range(m):
            matrix.append( [ x for x in input().strip().split() ] )
        obj = Solution() 
        result = obj.findDistance(matrix,m,n)
        for i in result:
            for j in i:
                print(j, end=' ')
            print()
# } Driver Code Ends