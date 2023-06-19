#User function Template for python3
from collections import deque
class Solution:
    def antiDiagonalPattern(self,matrix):
        # Code here
        n, direction, q, res = len(matrix), [[0, 1], [1, 0]], deque(), []
        q.append([0, 0, matrix[0][0]])
        
        while q:
            x, y, val = q.popleft()
            res.append(val)

            for x1, y1 in direction:
                x2, y2 = x+x1, y+y1
                if -1<x2<n and -1<y2<n and matrix[x2][y2]>-1:
                    q.append([x2, y2, matrix[x2][y2]])
                    matrix[x2][y2]=-1
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input()) 
        inp=list(map(int,input().split()))
        matrix=[]
        k = 0
        for i in range(n):
            row = []
            for j in range(n):
                row.append(inp[k])
                k += 1
            matrix.append(row)
        ob = Solution()
        ans = ob.antiDiagonalPattern(matrix)
        for i in ans:
            print(i,end=" ")
        print()


# } Driver Code Ends