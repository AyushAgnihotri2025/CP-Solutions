#User function Template for python3

from collections import deque

class Solution:
    def helpaterp(self, hospital):
        # code here
        q = deque()
        n = len(hospital)
        m = len(hospital[0])
        
        for i in range(n):
            for j in range(m):
                if hospital[i][j] == 2:
                    q.append((i, j, 0))
        ans = 0
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        while len(q) > 0:
            k = len(q)
            for i in range(k):
                x, y, d = q.popleft()
                ans = d
                for j in range(4):
                    nx = x + dx[j]
                    ny = y + dy[j]
                    if nx >= 0 and nx < n and ny >= 0 and ny < m and hospital[nx][ny] == 1:
                        hospital[nx][ny] = 2
                        q.append((nx, ny, d+1))
        
        for line in hospital:
            if 1 in line:
                return -1
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        
        rc=input().split() #row and column
        r=int(rc[0])    
        c=int(rc[1])
        
        
        hospital=[]
        
        for i in range(r):
            hospital.append([int(j) for j in input().split()])
            
        ob = Solution()        
        print(ob.helpaterp(hospital))

# } Driver Code Ends