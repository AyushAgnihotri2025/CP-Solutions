#User function Template for python3

class Solution:
    def primeRange(self,N,Q,A,R):
        #R is a 2D array of dimensions Qx2
        #code here
        s={}
        self.sieve(max(A),s) 
        l=[] 
        m=0 
        p=[]
        for i in A:
            if i in s:
                p.append(1)
                m+=1 
            else:
                p.append(0)
            l.append(m)
            
        g=[] 
        for i in R:
            g.append(l[i[1]-1]-l[i[0]-1]+p[i[0]-1])
        return g
    def sieve(self,n,s):
        l=[0]*(n+1) 
        p=2
        while p*p<=n:
            j=2*p
            if l[p]==0:
                for i in range(j,n+1,p):
                    l[i]=1 
            p+=1 
        for i in range (2,n+1):
            if l[i]==0:
                s[i]=1
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,Q=map(int,input().strip().split(" "))
        A=list(map(int,input().strip().split(" ")))
        R=[]
        for i in range(Q):
            temp=list(map(int,input().strip().split(" ")))
            R.append(temp)
        ob=Solution()
        ans=ob.primeRange(N,Q,A,R)
        for i in ans:
            print(i,end=" ")
        print()    
# } Driver Code Ends