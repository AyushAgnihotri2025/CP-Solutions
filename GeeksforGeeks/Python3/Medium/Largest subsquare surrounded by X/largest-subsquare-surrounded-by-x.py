#User function Template for python3

class Solution:
    def largestSubsquare(self,N,A):
        h = [[0 for i in range(N)] for j in range(N)]
        v = [[0 for i in range(N)] for j in range(N)]
        for i in range(N):
            for j in range(N):
                if A[i][j] == 'O':
                    h[i][j] = 0
                    v[i][j] = 0
                else:
                    if j == 0:
                        h[i][j] = 1
                    else:
                        h[i][j] = h[i][j-1] + 1
                    if i == 0:
                        v[i][j] = 1
                    else:
                        v[i][j] = v[i-1][j] + 1
        max_val = 0
        for i in range(N-1, -1, -1):
            for j in range(N-1, -1, -1):
                small = min(h[i][j], v[i][j])
                while small > max_val:
                    if h[i-small+1][j] >= small and v[i][j-small+1] >= small:
                        max_val = small
                    small -= 1
        return max_val

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        a=[]
        for i in range(N):
            s=list(map(str,input().strip().split()))
            a.append(s)
        ob=Solution()
        print(ob.largestSubsquare(N,a))
# } Driver Code Ends