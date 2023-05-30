#User function Template for python3

class Solution:
    def findPar(self,a,par):
        if a==par[a]:
            return a
        parentNode=self.findPar(par[a],par)
        return parentNode

    #Function to merge two nodes a and b.
    def union_(self,a,b,par,rank1):
        # code here
        p1=self.findPar(a,par)
        p2=self.findPar(b,par)
        if rank1[p1]>rank1[p2]:
            par[p2]=p1
        elif rank1[p2]>rank1[p1]:
            par[p1]=p2
        else:
            par[p2]=p1
            rank1[p1]+=1
        
    #Function to check whether 2 nodes are connected or not.
    def isConnected(self,x,y,par,rank1):
        # code here
        p1=self.findPar(x,par)
        p2=self.findPar(y,par)
        return p1==p2

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        q = int(input())

        par = [i for i in range(n+1)] # parent of ith node is initialized as i.
        rank1 = [1 for i in range(n+1)] # rank is initialized as 1 fo every node
        obj = Solution()
        for i in range(q):
            task,u,v = map(str,input().strip().split())
            u = int(u)
            v = int(v)

            if task == 'U':
                obj.union_(u,v,par,rank1)
            else:
                if obj.isConnected(u,v,par,rank1):
                    print(1)
                else:
                    print(0)


# } Driver Code Ends