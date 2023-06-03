
from typing import List
class Solution:
    def minimumCostOfBreaking(self,X : List[int], Y : List[int],M : int, N : int) -> int:
        # code here
        nv=1
        nh=1
        tc=0
        X.sort()
        Y.sort()
        i=M-2
        j=N-2
        while i>=0 and j>=0:
            if X[i]>=Y[j]:
                tc+=nv*X[i]
                nh+=1
                i-=1
            else:
                tc+=nh*Y[j]
                nv+=1
                j-=1
        if i<0:
            while j>=0:
                tc+=nh*Y[j]
                nv+=1
                j-=1   
        if j<0:
            while i>=0:
                tc+=nv*X[i]
                nh+=1
                i-=1
        return tc

#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        m = a[0]
        n = a[1]
        
        tmp=IntArray().Input(a[0]-1) + IntArray().Input(a[1]-1)
        X = tmp[:m-1]
        Y = tmp[m-1:]
        
        obj = Solution()
        res = obj.minimumCostOfBreaking(X, Y,m,n)
        
        print(res)
        

# } Driver Code Ends