#User function Template for python3

import heapq

class Solution:
    def MinimumEffort(self, a):
        #code here
        m, n = len(a), len(a[0])
        X, Y = [1, 0, -1, 0], [0, 1, 0, -1]
        dist = [[float("inf")]*n for _r in range(m)]
        dist[0][0] = 0
        q = [(0, 0)]
        while q:
            i, j = heapq.heappop(q)
            for k in range(4):
                x = i + X[k]
                y = j + Y[k]
                if 0 <= x < m and 0 <= y < n and dist[x][y] > max(dist[i][j], abs(a[x][y] - a[i][j])):
                    dist[x][y] = max(dist[i][j], abs(a[x][y] - a[i][j]))
                    heapq.heappush(q, (x, y))
        return dist[m-1][n-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n,m=map(int,input().split())
        a=[]
        for i in range(n):
            li=list(map(int,input().split()))
            a.append(li)
        ob = Solution()
        ans = ob.MinimumEffort(a)
        print(ans)
        tc -= 1
# } Driver Code Ends