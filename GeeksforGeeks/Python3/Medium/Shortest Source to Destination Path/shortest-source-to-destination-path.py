#User function Template for python3

class Solution:
    def shortestDistance(self,N,M,A,X,Y):
        #code here
        if A[0][0] == 0:
            return -1
        ans = -1
        queue = [(0,0,0)]
        while len(queue) > 0:
            (i,j,level) = queue.pop(0)
            if (i,j) == (X,Y):
                ans = level
                break
            for dx in (-1,1):
                u = i+dx
                v = j
                if 0<=u<N and A[u][v] == 1:
                    queue.append((u,v,level+1))
                    A[u][v] = 0
            for dy in (-1,1):
                u = i
                v = j+dy
                if 0<=v<M and A[u][v] == 1:
                    queue.append((u,v,level+1))
                    A[u][v] = 0
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split())
        a=[]
        for i in range(N):
            s=list(map(int,input().strip().split()))
            a.append(s)
        x,y=map(int,input().strip().split())    
        ob=Solution()
        print(ob.shortestDistance(N,M,a,x,y))
        
# } Driver Code Ends